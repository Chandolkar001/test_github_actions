#!/bin/sh -l

echo "Start process"
cd ..
cd ..
ls
pwd
python /app/secretscan_entry.py "$1" "$2" "$3" "$4"

