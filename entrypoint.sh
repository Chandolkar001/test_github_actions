#!/bin/sh -l

echo "Reading Parameters"

while getopts ":a:b:c:d:" opt; do
  case $opt in
    a)
      export TYPE_OF_SCAN="$OPTARG"
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

export CLIENT_REPO=$GITHUB_WORKSPACE
export SERVICE=github
cd /app
echo "Start scan"
./action_entrypoint

