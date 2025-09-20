#!/bin/bash
if ! command -v python &> /dev/null; then
    echo "Python is not installed or not in PATH."
    exit 1
fi

python passcraft.py "$@"