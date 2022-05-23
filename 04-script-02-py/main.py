#!/usr/bin/env python3

import os

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
#         print(prepare_result)
#         break

bash_command = ["cd /var/www/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()

for result in result_os.split('\n'):
    print(result)
    # if result.find('modified') != -1:
    #     prepare_result = result.replace('\tmodified:   ', '')
    #     print(os.path.abspath(prepare_result))
#        break