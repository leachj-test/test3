#!/usr/bin/env python3
"""
App Publishing Pipeline
Processes app submissions and validates them against SDK requirements
"""

import yaml
import sys
import json
from packaging import version


def load_config():
    """Load pipeline configuration"""
    with open('config/pipeline.yaml', 'r') as f:
        return yaml.safe_load(f)


def validate_app(app_data, config):
    """Validate app against SDK requirements"""
    app_sdk_version = app_data.get('sdk_version', '1.0.0')
    min_version = config['app_publishing']['sdk_requirements']['minimum_version']
    strict_check = config['app_publishing']['sdk_requirements']['strict_version_check']
    auto_drop = config['app_publishing']['publishing_rules']['auto_drop_old_versions']
    
    print(f"Validating app '{app_data.get('name', 'Unknown')}' with SDK version {app_sdk_version}")
    print(f"Minimum required version: {min_version}")
    print(f"Strict version check: {strict_check}")
    
    # This is the problematic version check that drops apps with previous SDK versions
    if strict_check and version.parse(app_sdk_version) < version.parse(min_version):
        if auto_drop:
            print(f"❌ App DROPPED: SDK version {app_sdk_version} is below minimum {min_version}")
            return False
        else:
            print(f"⚠️  App WARNING: SDK version {app_sdk_version} is below minimum {min_version}")
            return True
    
    print(f"✅ App APPROVED: SDK version {app_sdk_version} meets requirements")
    return True


def process_apps(apps):
    """Process a list of app submissions"""
    config = load_config()
    approved_apps = []
    dropped_apps = []
    
    for app in apps:
        if validate_app(app, config):
            approved_apps.append(app)
        else:
            dropped_apps.append(app)
    
    print(f"\n📊 Processing Summary:")
    print(f"   Approved: {len(approved_apps)} apps")
    print(f"   Dropped: {len(dropped_apps)} apps")
    
    if dropped_apps:
        print(f"\n📋 Dropped apps:")
        for app in dropped_apps:
            print(f"   - {app.get('name', 'Unknown')} (SDK {app.get('sdk_version', 'Unknown')})")
    
    return approved_apps, dropped_apps


def main():
    """Main pipeline execution"""
    # Sample app submissions with various SDK versions
    sample_apps = [
        {"name": "CoolWeatherApp", "sdk_version": "2.0.0", "platform": "ios"},
        {"name": "TaskManagerPro", "sdk_version": "2.1.0", "platform": "android"},
        {"name": "LegacyNotesApp", "sdk_version": "1.9.5", "platform": "ios"},
        {"name": "ModernChatApp", "sdk_version": "2.2.0", "platform": "web"},
        {"name": "OldCalculator", "sdk_version": "1.8.0", "platform": "android"},
    ]
    
    print("🚀 Starting App Publishing Pipeline")
    print("=" * 50)
    
    approved, dropped = process_apps(sample_apps)
    
    print("\n🎯 Pipeline completed")
    return len(dropped) == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)