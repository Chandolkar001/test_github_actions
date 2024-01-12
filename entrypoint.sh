#!/bin/sh -l

echo "Reading Parameters"

while getopts ":a:b:c:d:e:" opt; do
  case $opt in
    a)
      export SCAN_TYPE="$OPTARG"
      ;;
    b)
      export FILE_EXCLUSIONS="$OPTARG"
      ;;
    c)
      export REGEX_EXCLUSIONS="$OPTARG"
      ;;
    d)
      export HASH_EXCLUSIONS="$OPTARG"
      ;;
    e)
      export CUSTOM_REGEX="$OPTARG"
      ;;
  esac
done

export CLIENT_REPO=$GITHUB_WORKSPACE
# export CLIENT_REPO=$(pwd)
# echo "$(pwd)"
# cd ../..
# cd app/
# echo "$(pwd)"
cd /app
echo "Start scan"
python secretscan_entry.py --type "$SCAN_TYPE" --file "$FILE_EXCLUSIONS" --regex "$REGEX_EXCLUSIONS" --hash "$HASH_EXCLUSIONS" --cregex "$CUSTOM_REGEX" --code "$CLIENT_REPO"

