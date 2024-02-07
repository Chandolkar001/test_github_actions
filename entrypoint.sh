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
text="This is a Warning"
echo "::warning file=app.py,line=1,col=5::$text"
python action_entrypoint.py --type "$SCAN_TYPE"

