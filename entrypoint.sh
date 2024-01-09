#!/bin/sh -l

echo "Start scan"
cd ..
cd ..
echo "search for event.json"
find / -type f -name "event.json"
echo "what's in /github"
ls -R github/
cd app/
python secretscan_entry.py "$1" "$2" "$3" "$4"

