#!/usr/bin/env python3
import yaml
import json
from pynetgear import Netgear

config = yaml.load(open('/config/secrets.yaml'))
netgear = Netgear(host=config['netgear_host'], user=config['netgear_user'], password=config['netgear_pass'])

traffic = netgear.get_traffic_meter()

json_dict = {
    "today": traffic['NewTodayUpload'] + traffic['NewTodayDownload'],
    "yesterday": traffic['NewYesterdayUpload'] + traffic['NewYesterdayDownload'],
    "week": traffic['NewWeekUpload'][0] + traffic['NewWeekDownload'][0],
    "month": traffic['NewMonthUpload'][0] + traffic['NewMonthDownload'][0],
    "lastmonth": traffic['NewLastMonthUpload'][0] + traffic['NewLastMonthDownload'][0],
}

print(json.dumps(json_dict))
