#!/bin/sh -l

echo "Start process"
cd ..
cd ..
ls
cd app/
python secretscan_entry.py "$1" "$2" "$3" "$4"

