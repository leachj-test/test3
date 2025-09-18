# App Publishing Pipeline

This repository contains the app publishing pipeline that validates and processes app submissions.

## Problem

The current pipeline has a strict version check that automatically drops apps using previous SDK versions. This is causing legitimate apps to be rejected.

## Current Issues

- Apps with SDK versions below 2.1.0 are being automatically dropped
- The `strict_version_check` setting is too restrictive
- Developers are losing app submissions without proper warnings

## Files

- `config/pipeline.yaml` - Pipeline configuration with SDK requirements
- `scripts/publish_pipeline.py` - Main pipeline processing script
- `requirements.txt` - Python dependencies

## Usage

```bash
pip install -r requirements.txt
cd scripts
python publish_pipeline.py
```

## Configuration

The pipeline behavior is controlled by settings in `config/pipeline.yaml`:

- `minimum_version`: Required minimum SDK version  
- `strict_version_check`: Whether to enforce strict version requirements
- `auto_drop_old_versions`: Whether to automatically drop non-compliant apps