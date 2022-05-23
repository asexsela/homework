# Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"


## 1. Обязательная задача 1

### Есть скрипт:


```python

    #!/usr/bin/env python3
    a = 1
    b = '2'
    c = a + b

```

Какие значения переменным c,d,e будут присвоены? Почему?


| Вопрос  | Ответ |
| ------------- | ------------- |
| Какое значение будет присвоено переменной `c`?	  | TypeError: unsupported operand type(s) for +: 'int' and 'str'  |
| Как получить для переменной `c` значение 12?  | Нужно `a` привести к строковому типу `c = str(a) + b` |
| Как получить для переменной `c` значение 3?  | Нужно `b` привести к целочисленному типу `c = a + int(b)` |


## 2. Обязательная задача 2

Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?



```python
   #!/usr/bin/env python3

    import os

    bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
    result_os = os.popen(' && '.join(bash_command)).read()
    is_change = False
    for result in result_os.split('\n'):
        if result.find('modified') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
            print(prepare_result)
            break

```

## Ответ

```python

    #!/usr/bin/env python3

    import os

    bash_command = ["cd /var/www/netology/sysadm-homeworks", "git status"]
    result_os = os.popen(' && '.join(bash_command)).read()

    for result in result_os.split('\n'):
        if result.find('modified') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
            print(os.path.abspath(prepare_result))

```

## Вывод скрипта при запуске при тестировании:

```shell

    python3 04-script-02-py/main.py

    /var/www/netology/sysadm-homeworks/04-script-02-py/README.md
    /var/www/netology/sysadm-homeworks/04-script-02-py/main.py

```

## 3. Обязательная задача 3

Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.


## Ответ

```python
    #!/usr/bin/env python3

    import os

    print("Укажите абсолютный путь к репозиторию:")
    path = input('> ')

    os.chdir(path)
    bash_command = ["git status"]
    result_os = os.popen(' && '.join(bash_command)).read()

    for result in result_os.split('\n'):
        if result.find('modified') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
        print('\n'+path+prepare_result)

```

## Вывод скрипта при запуске при тестировании:

```shell
    python3 04-script-02-py/main.py

    Укажите абсолютный путь к репозиторию:
    > /var/www/netology/virt-homeworks

    /var/www/netology/virt-homeworks/README.md
```

## 4. Обязательная задача 4

Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел, занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: drive.google.com, mail.google.com, google.com.


## Ответ

```python
    #!/usr/bin/env python3

    import os
    import socket
    import json

    conf_file="./04-script-02-py/config.json"

    with open(conf_file) as json_data_file:
        conf = json.load(json_data_file)

    for host, ip in conf.items():
        new_ip=socket.gethostbyname(host)

        if (ip != new_ip):
            print ('[ERROR] {} IP mismatch: {} {}'.format(host,ip,new_ip))
            conf[host]=new_ip

    for host, ip in conf.items():
        print('{} - {}'.format(host,ip))

    with open(conf_file, "w") as json_data_file:
        json.dump(conf, json_data_file, indent=2)

```

### config.json
```json
    {
        "drive.google.com": "",
        "mail.google.com": "",
        "google.com": ""
    }
```
    


## Вывод скрипта при запуске при тестировании:

```shell

    python3 04-script-02-py/main.py

    [ERROR] drive.google.com IP mismatch:  64.233.162.194
    [ERROR] mail.google.com IP mismatch:  173.194.222.18
    [ERROR] google.com IP mismatch:  173.194.220.100
    drive.google.com - 64.233.162.194
    mail.google.com - 173.194.222.18
    google.com - 173.194.220.100
    
```