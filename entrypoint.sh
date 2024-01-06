#!/bin/bash

set -e

while getopts "a:b:c" o; do
    case "${o}" in
    a) 
        name=${OPTARG}
    ;;
    esac
done

echo "Name : $name"

python /app/entrypoint.py "$name"

