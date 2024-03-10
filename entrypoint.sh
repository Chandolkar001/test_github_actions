#!/bin/sh -l

echo "Reading Parameters"

while getopts ":a:b:c:d:" opt; do
  case $opt in
    a)
      export SCAN_TYPE="$OPTARG"
      ;;
    b) 
      export GITHUB_CONTEXT="$OPTARG"
      ;;
    c) 
      export AUTH_TOKEN="$OPTARG"
      ;;
    d) 
      export API_ENDPOINT="$OPTARG"
      ;;
  esac
done

echo $SCAN_TYPE
export CLIENT_REPO=$GITHUB_WORKSPACE
export SERVICE=github
cd /app
echo "Start scan"
./action_entrypoint

