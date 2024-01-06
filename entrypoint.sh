#!/bin/sh -l

echo "Hello $1"
python /app/entrypoint.py "$1"
cat /github/workspace/README.md
