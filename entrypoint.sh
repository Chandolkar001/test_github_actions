#!/bin/sh -l

echo "Start scan"
client_repo=$(pwd)
cd ../..
cd app/
echo "$client_repo"
python secretscan_entry.py "$1" "$2" "$3" "$4"

