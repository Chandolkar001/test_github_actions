#!/bin/sh -l

echo "Start scan"
client_repo=$GITHUB_WORKSPACE
cd ../..
cd app/
echo "$client_repo"
python secretscan_entry.py "$1" "$2" "$3" "$4"

