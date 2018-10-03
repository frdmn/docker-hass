#!/usr/bin/env bash
DOCKER_HOST=$(hostname -I | awk '{print $1}')

VALUE_KEYS=( upload download ping )
JSON="{"

for key in "${VALUE_KEYS[@]}"; do
    RESPONSE=$(curl -s ${DOCKER_HOST}:8086/query?db=speedtest --data-urlencode "q=SELECT * FROM ${key} ORDER BY DESC LIMIT 1")
    VALUE=$(echo "${RESPONSE}" | python2 -c "import sys, json; print json.load(sys.stdin)['results'][0]['series'][0]['values'][0][2]" 2> /dev/null)
    JSON+="\"${key}\":\"${VALUE}\","
done

JSON=${JSON::-1}
JSON+="}"

echo ${JSON}
exit 0
