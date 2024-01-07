#!/bin/sh -l

echo "Start"
ls
python /app/secretscan_entry.py "$1" "$2" "$3" "$4"

