#!/bin/sh -l

echo "Reading Parameters"

while getopts ":a:b:c:d:e:" opt; do
  case $opt in
    a)
      SCAN_TYPE="$OPTARG"
      ;;
    b)
      FILE_EXCLUSIONS="$OPTARG"
      ;;
    c)
      REGEX_EXCLUSIONS="$OPTARG"
      ;;
    d)
      HASH_EXCLUSIONS="$OPTARG"
      ;;
    e)
      CUSTOM_REGEX="$OPTARG"
      ;;
  esac
done

CLIENT_REPO=$GITHUB_WORKSPACE

echo "$(pwd)"
cd ../..
cd app/
echo "$(pwd)"

echo "Start scan"
python secretscan_entry.py --type "$SCAN_TYPE" --file "$FILE_EXCLUSIONS" --regex "$REGEX_EXCLUSIONS" --hash "$HASH_EXCLUSIONS" --cregex "$CUSTOM_REGEX" --code "$CLIENT_REPO"

