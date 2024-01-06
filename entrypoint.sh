#!/bin/bash

set -e

while getopts "a:c:" o; do
    case "${o}" in
    a) 
        name="${OPTARG}"
        ;;
    c)
        custom_option="${OPTARG}"
        ;;
    *)
        echo "Usage: $0 -a <name> -c <custom_option>"
        exit 1
        ;;
    esac
done

# Additional processing if needed
echo "Name: $name"
echo "Custom Option: $custom_option"

# Call Python script with the provided name
python /app/entrypoint.py "$name"
