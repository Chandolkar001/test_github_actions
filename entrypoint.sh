#!/bin/sh -l

echo "Start scan"
echo "$GITHUB_WORKSPACE"
client_repo=$(pwd)
cd ../..
cd app/
python secretscan_entry.py "$1" "$2" "$3" "$4"

