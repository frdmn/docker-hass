#!/usr/bin/env python3
import yaml
import json
import math
from pynetgear import Netgear

def convert_size(size_megas):
    size_bytes = size_megas * 1024 * 1024
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

config = yaml.load(open('/config/secrets.yaml'))
netgear = Netgear(host=config['netgear_host'], user=config['netgear_user'], password=config['netgear_pass'])

traffic = netgear.get_traffic_meter()

json_dict = {
    "today": convert_size(traffic['NewTodayUpload'] + traffic['NewTodayDownload']),
    "yesterday": convert_size(traffic['NewYesterdayUpload'] + traffic['NewYesterdayDownload']),
    "week": convert_size(traffic['NewWeekUpload'][0] + traffic['NewWeekDownload'][0]),
    "month": convert_size(traffic['NewMonthUpload'][0] + traffic['NewMonthDownload'][0]),
    "lastmonth": convert_size(traffic['NewLastMonthUpload'][0] + traffic['NewLastMonthDownload'][0])
}

print(json.dumps(json_dict))
