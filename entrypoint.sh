#!/bin/sh -l

echo "Reading Parameters"

while getopts ":a:b:" opt; do
  case $opt in
    a)
      export SCAN_TYPE="$OPTARG"
      ;;
    b) 
      export $GITHUB_CONTEXT="$OPTARG"
      ;;
  esac
done

export CLIENT_REPO=$GITHUB_WORKSPACE
cd /app
echo $GITHUB_CONTEXT
echo $SCAN_TYPE
echo "Start scan"
python action_entrypoint.py --type "$SCAN_TYPE"

