#!/usr/bin/env bash

PCWD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
SECRETSFILE="${PCWD}/../secrets.yaml"

if [[ $# -eq 0 ]] ; then
    echo 'Usage: _get_secret secret_key'
    exit 1
fi

MATCH=$(grep ^${1}: ${SECRETSFILE} | awk '{ print $2 }')

if [[ -z $MATCH ]]; then
    echo 'Error: key not found'
    exit 1
fi

echo $MATCH
exit 0
