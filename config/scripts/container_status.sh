#!/usr/bin/env bash
DOCKER_HOST=$(hostname -I | awk '{print $1}')
CONTAINER=${1}

if [[ -z ${CONTAINER} ]]; then
    echo "No argument (CONTAINER) given"
    exit 1
fi

ENGINE_RESPONSE=$(curl -s http://${DOCKER_HOST}:2375/v1.37/containers/${CONTAINER}/json)
STATE=$(echo "${ENGINE_RESPONSE}" | python2 -c "import sys, json; print json.load(sys.stdin)['State']['Status']" 2> /dev/null)

if [[ $? -ne 0 ]]; then
    echo "Invalid response from Docker Engine. Aborting..."
    exit 1
fi

echo ${STATE}
exit 0
