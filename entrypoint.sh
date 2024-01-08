#!/bin/sh -l

echo "Start secret scan"
cd ..
cd ..
ls github/workspace/
cd app/
python secretscan_entry.py "$1" "$2" "$3" "$4"

