# App Publishing Pipeline

This repository contains the app publishing pipeline that validates and processes app submissions.

## Problem (RESOLVED)

~~The current pipeline has a strict version check that automatically drops apps using previous SDK versions. This is causing legitimate apps to be rejected.~~

**FIXED:** The strict version check has been reverted to allow apps with previous SDK versions.

## Previous Issues (RESOLVED)

- ~~Apps with SDK versions below 2.1.0 are being automatically dropped~~
- ~~The `strict_version_check` setting is too restrictive~~
- ~~Developers are losing app submissions without proper warnings~~

## Solution Applied

**Reverted the problematic settings:**
- Changed `strict_version_check: false` (was `true`)
- Changed `auto_drop_old_versions: false` (was `true`) 
- Enabled `notify_on_drop: true` to alert when version issues occur

**Result:** All 5 test apps now pass through the pipeline instead of 3 being dropped.

## Files

- `config/pipeline.yaml` - Pipeline configuration with SDK requirements (UPDATED)
- `scripts/publish_pipeline.py` - Main pipeline processing script (IMPROVED)
- `requirements.txt` - Python dependencies

## Usage

```bash
pip install -r requirements.txt
cd scripts
python publish_pipeline.py
```

## Current Behavior

The pipeline now:
✅ Approves all valid apps regardless of SDK version
⚠️  Shows helpful warnings for apps using older SDK versions  
🔄 Encourages developers to upgrade without blocking submissions

## Configuration

The pipeline behavior is controlled by settings in `config/pipeline.yaml`:

- `minimum_version`: Recommended minimum SDK version  
- `strict_version_check`: Whether to enforce strict version requirements (now `false`)
- `auto_drop_old_versions`: Whether to automatically drop non-compliant apps (now `false`)