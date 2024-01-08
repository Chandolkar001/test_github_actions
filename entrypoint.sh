#!/bin/sh -l

echo "Start process"
ls -a
python secretscan_entry.py "$1" "$2" "$3" "$4"

