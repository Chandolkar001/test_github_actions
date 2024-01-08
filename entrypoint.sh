#!/bin/sh -l

echo "Start secret scan"
cd ..
cd ..
ls github/workspace/
find ~/ -type f -name "event.json"
cd app/
python secretscan_entry.py "$1" "$2" "$3" "$4"

