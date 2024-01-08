#!/bin/sh -l

echo "Start secret scan"
cd ..
cd ..
ls github/workspace/
python /app/secretscan_entry.py "$1" "$2" "$3" "$4"

