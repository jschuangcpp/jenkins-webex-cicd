#!/bin/sh

set -eu

echo "=================================="
echo "Building the Python application"
echo "=================================="

echo "Python version:"
python3 --version

echo "Checking Python syntax..."
python3 -m py_compile calculator.py notify_webex.py

echo "Build completed successfully."