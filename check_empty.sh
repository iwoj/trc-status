#!/bin/bash
# check_filesize.sh
# Purpose: exit with error if file size is zero

FILE=$1

# Does file exist?
if [ ! -f "$FILE" ]; then
    echo "ERROR: $FILE not found"
    exit 1
fi

# Is file empty?
if [ ! -s "$FILE" ]; then
    echo "ERROR: $FILE is empty"
    exit 1
fi

# OK
exit 0

