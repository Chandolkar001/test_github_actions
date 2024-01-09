#!/bin/sh -l

echo "Start scan"
cd ../..
python secretscan_entry.py "$1" "$2" "$3" "$4"

