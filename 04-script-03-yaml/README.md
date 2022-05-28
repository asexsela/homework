# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"


## 1. Обязательная задача 1

Мы выгрузили JSON, который получили через API запрос к нашему сервису:

```json
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```

Нужно найти и исправить все ошибки, которые допускает наш сервис


### Ответ:

```json
    { 
        "info": "Sample JSON output from our service\t",
        "elements": [
            { 
                "name": "first",
                "type": "server",
                "ip": 7175
            }, // тут не было запятой
            { 
                "name": "second",
                "type": "proxy",
                "ip": "71.78.22.43" // тут не было запятой и значение должно быть в кавычках
            }
        ]
    }
```


## 2. Обязательная задача 2

В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: { "имя сервиса" : "его IP"}. Формат записи YAML по одному сервису: - имя сервиса: его IP. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.


### Ваш скрипт:

```python

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

```

### Вывод скрипта при запуске при тестировании:

```shell
    [ERROR] mail.google.com IP mismatch: 209.85.233.83 209.85.233.19
    [ERROR] google.com IP mismatch: 173.194.222.113 173.194.222.101
    drive.google.com - 74.125.131.194
    mail.google.com - 209.85.233.19
    google.com - 173.194.222.101
```

### json-файл(ы), который(е) записал ваш скрипт:

```json
    {
        "drive.google.com": "74.125.131.194",
        "mail.google.com": "209.85.233.19",
        "google.com": "173.194.222.138"
    }
```

### yml-файл(ы), который(е) записал ваш скрипт:

```yaml
    ---
    drive.google.com: 74.125.131.194
    google.com: 173.194.222.138
    mail.google.com: 209.85.233.19
```