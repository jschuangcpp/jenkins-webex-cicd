#!/bin/sh

set -eu

echo "=================================="
echo "Running Python unit tests"
echo "=================================="

python3 -m unittest discover \
    -s tests \
    -p "test_*.py" \
    -v

echo "All Python unit tests completed successfully."