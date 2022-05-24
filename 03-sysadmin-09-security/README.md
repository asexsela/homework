# Домашнее задание к занятию "3.9. Элементы безопасности информационных систем"

1. Установите Bitwarden плагин для браузера. Зарегестрируйтесь и сохраните несколько паролей.


     **Ответ:** ![](https://github.com/asexsela/homework/blob/master/03-sysadmin-09-security/warden-install.png?raw=true)

2. Установите Google authenticator на мобильный телефон. Настройте вход в Bitwarden акаунт через Google authenticator OTP.

    **Ответ:** ![](https://github.com/asexsela/homework/blob/master/03-sysadmin-09-security/warden-two-step-auth.png?raw=true)

3. Установите apache2, сгенерируйте самоподписанный сертификат, настройте тестовый сайт для работы по HTTPS.

    **Ответ:**

```shell
    sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt

```

![](https://github.com/asexsela/homework/blob/master/03-sysadmin-09-security/apache2.png?raw=true)

![](https://github.com/asexsela/homework/blob/master/03-sysadmin-09-security/sert.png?raw=true)

4. Проверьте на TLS уязвимости произвольный сайт в интернете (кроме сайтов МВД, ФСБ, МинОбр, НацБанк, РосКосмос, РосАтом, РосНАНО и любых госкомпаний, объектов КИИ, ВПК ... и тому подобное).

    **Ответ:**

```shell
    ./testssl.sh -Z -p docs.google.com

    ###########################################################
        testssl.sh       3.1dev from https://testssl.sh/dev/
        (d931eb4 2022-05-14 13:57:46)

        This program is free software. Distribution and
                modification under GPLv2 permitted.
        USAGE w/o ANY WARRANTY. USE IT AT YOUR OWN RISK!

        Please file bugs @ https://testssl.sh/bugs/

    ###########################################################

    Using "OpenSSL 1.0.2-chacha (1.0.2k-dev)" [~183 ciphers]
    on alex-MS-7B89:./bin/openssl.Linux.x86_64
    (built: "Jan 18 17:12:17 2019", platform: "linux-x86_64")


    Start 2022-05-23 23:53:35        -->> 173.194.73.194:443 (docs.google.com) <<--

    Further IP addresses:   2a00:1450:4010:c0d::c2 
    rDNS (173.194.73.194):  lq-in-f194.1e100.net.
    Service detected:       HTTP


    Testing protocols via sockets except NPN+ALPN 

    SSLv2      not offered (OK)
    SSLv3      not offered (OK)
    TLS 1      offered (deprecated)
    TLS 1.1    offered (deprecated)
    TLS 1.2    offered (OK)
    TLS 1.3    offered (OK): final
    NPN/SPDY   grpc-exp, h2, http/1.1 (advertised)
    ALPN/HTTP2 h2, http/1.1, grpc-exp (offered)

    Testing for TLS_FALLBACK_SCSV Protection 

    TLS_FALLBACK_SCSV (RFC 7507)              Downgrade attack prevention supported (OK)


    Done 2022-05-23 23:53:41 [   7s] -->> 173.194.73.194:443 (docs.google.com) <<--

```

5. Установите на Ubuntu ssh сервер, сгенерируйте новый приватный ключ. Скопируйте свой публичный ключ на другой сервер. Подключитесь к серверу по SSH-ключу.

    **Ответ:**

```shell
    ssh-keygen

    ssh-copy-id admn@ip
    ssh -i key.pem admn@ip

    nano ~/.ssh/config

    ...
    Host servername.com
        HostName ip
        IdentityFile path to private key
        User admin
    ...

```


6. Переименуйте файлы ключей из задания 5. Настройте файл конфигурации SSH клиента, так чтобы вход на удаленный сервер осуществлялся по имени сервера.

    **Ответ:**

```shell
    nano ~/.ssh/config
    ...
    Host servername.com
        HostName ip
        IdentityFile path to private key
        User admin
    ...

    ssh servername.com

```

7. Соберите дамп трафика утилитой tcpdump в формате pcap, 100 пакетов. Откройте файл pcap в Wireshark.

    **Ответ:**

```shell
     sudo tcpdump -i enp34s0 -c 100 -w tcpdump_out.pcap

```
![](https://github.com/asexsela/homework/blob/master/03-sysadmin-09-security/wireshark.png?raw=true)