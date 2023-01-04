#!/bin/bash

if [ "x${1}" == "x" ]; then
	echo "usage:"
    echo "	${0} GitProjectPath"
	exit;
fi

GitProjectPath="/srv/gitlab/FT/mirrors/${1}"

cd $GitProjectPath

#git fetch --prune origin
#git push --mirror target

