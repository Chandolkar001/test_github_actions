#!/bin/sh -l

echo "Start scan"
cd ~/app
python secretscan_entry.py "$1" "$2" "$3" "$4"

