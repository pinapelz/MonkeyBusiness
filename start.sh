#!/bin/bash

ver="3.14"
py="python$ver"

# Ensure Python exists (uv still relies on system Python)
if ! command -v "$py" &> /dev/null; then
    echo "$py not found"
    exit 1
fi

if ! command -v uv &> /dev/null; then
    echo "uv not found"
    echo "Install with: pip install uv  OR  https://astral.sh/uv"
    exit 1
fi


if [ ! -d ".venv" ]; then
    echo "Creating virtual environment with uv..."
    uv venv .venv --python "$py"
fi

echo "Installing dependencies..."
uv pip install -r requirements.txt

.venv/bin/python pyeamu.py
