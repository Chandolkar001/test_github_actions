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
cd /app
echo $SCAN_TYPE
echo "Start scan"
python action_entrypoint.py --type "$SCAN_TYPE" --code "$CLIENT_REPO"

