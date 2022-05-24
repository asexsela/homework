#!/usr/bin/env python3

import os
import socket
import json

# a = 1
# b = '2'
# # c = str(a) + b
# c = a + int(b)

# print(c)


# bash_command = ["cd /var/www/netology/sysadm-homeworks", "git status"]
# result_os = os.popen(' && '.join(bash_command)).read()

# for result in result_os.split('\n'):
#     if result.find('modified') != -1:
#         prepare_result = result.replace('\tmodified:   ', '')
#         print(os.path.abspath(prepare_result))


# print("Укажите абсолютный путь к репозиторию:")
# path = input('> ')


# os.chdir(path)
# bash_command = ["git status"]
# result_os = os.popen(' && '.join(bash_command)).read()

# for result in result_os.split('\n'):
#     if result.find('modified') != -1:
#         prepare_result = result.replace('\tmodified:   ', '/')
#         print('\n'+path+prepare_result)


# conf_file="./04-script-02-py/config.json"

# with open(conf_file) as json_data_file:
#     conf = json.load(json_data_file)

# for host, ip in conf.items():
#     new_ip=socket.gethostbyname(host)

#     if (ip != new_ip):
#         print ('[ERROR] {} IP mismatch: {} {}'.format(host,ip,new_ip))
#         conf[host]=new_ip

# for host, ip in conf.items():
#     print('{} - {}'.format(host,ip))

# with open(conf_file, "w") as json_data_file:
#     json.dump(conf, json_data_file, indent=2)