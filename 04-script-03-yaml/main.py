#!/usr/bin/env python3

import json
import yaml
import socket

jconf="./config.json"
yconf="./config.yaml"

with open(jconf) as j_data:
    conf = json.load(j_data)

for host, ip in conf.items():
    new_ip =socket.gethostbyname(host)

    if (ip != new_ip):
        print ('[ERROR] {} IP mismatch: {} {}'.format(host, ip, new_ip))
        conf[host]=new_ip

for host, ip in conf.items():
    print('{} - {}'.format(host,ip))

with open(jconf, "w") as j_data:
    json.dump(conf, j_data, indent=2)

with open(yconf, "w") as y_data:
    y_data.write(yaml.dump(conf, explicit_start=True))