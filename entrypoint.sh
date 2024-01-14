#!/bin/sh -l

echo "Reading Parameters"

while getopts ":a:" opt; do
  case $opt in
    a)
      export SCAN_TYPE="$OPTARG"
      ;;
  esac
done

export CLIENT_REPO=$GITHUB_WORKSPACE
cd /app
echo "Start scan"
python action_entrypoint.py --type "$SCAN_TYPE" --code "$CLIENT_REPO"

