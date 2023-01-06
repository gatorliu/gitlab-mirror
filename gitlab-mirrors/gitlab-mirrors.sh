#!/bin/bash

if [ "x${1}" == "x" ]; then
	echo "usage:"
    echo "	${0} GitProjectPath"
	exit 1;
fi

echo "	${0} GitProjectPath"
GitProjectPath="/srv/gitlab/FT/mirrors/${1}"

cd $GitProjectPath

git fetch --prune origin
git push --mirror target

