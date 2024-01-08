#!/bin/sh -l

echo "Start process"

python /app/secretscan_entry.py "$1" "$2" "$3" "$4"

