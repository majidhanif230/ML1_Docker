#!/bin/bash

# Define directories
LOG_DIR="/c/bash/log"
OLD_FILES_DIR="/c/bash/old_files"
TMP_DIR="/c/bash/temp"

# Check if the 'old_files' directory exists, create it if not
if [ ! -d "$OLD_FILES_DIR" ]; then
    mkdir -p "$OLD_FILES_DIR"
fi

# Move .log files from /c/bash/temp to /c/bash/old_files
mv "$TMP_DIR"/*.log "$OLD_FILES_DIR" 2>/dev/null

# Ensure log directory exists
if [ ! -d "$LOG_DIR" ]; then
    mkdir -p "$LOG_DIR"
fi

# Log action with timestamp
echo "$(date) - Files moved to old_files" >> "$LOG_DIR/file_cleanup.log"
