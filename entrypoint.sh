#!/bin/sh -l

echo "Name: $1"
python /app/entrypoint.py "$1"
