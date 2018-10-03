#!/usr/bin/env python3
import yaml
import json
from pynetgear import Netgear

config = yaml.load(open('../../secrets.yaml'))
netgear = Netgear(host=config['netgear_host'], user=config['netgear_user'], password=config['netgear_pass'])

print(json.dumps(netgear.get_traffic_meter()))
