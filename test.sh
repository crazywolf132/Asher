#!/bin/bash

version=$(python -V 2>&1 | grep -Po '(?<=Python )')
parsedVersion=$(echo "${version//./}")
if [[ "$parsedVersion" -lt "300" && "$parsedVersion" -gt "27" ]]
then 
    echo "Valid version"
else
    echo "Invalid version"
fi
