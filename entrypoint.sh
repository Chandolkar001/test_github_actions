#!/bin/sh -l

echo "Reading Parameters"

while getopts ":a:b:c:d:e:f:g:h:" opt; do
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
    f)
      export CDX_ENDPOINT="$OPTARG"
      ;;
    g)
      export CDX_AUTH="$OPTARG"
      ;;
    h)
      export SECRET_KEY="$OPTARG"
      ;;
  esac
done

env
export CLIENT_REPO=$GITHUB_WORKSPACE
cd /app
echo $SCAN_TYPE
echo "Start scan"
python action_entrypoint.py --type "$SCAN_TYPE" --code "$CLIENT_REPO"

