# Домашнее задание к занятию "3.8. Компьютерные сети, лекция 3"

1. Подключитесь к публичному маршрутизатору в интернет. Найдите маршрут к вашему публичному IP

    **Ответ**: 

```shell
    telnet route-views.routeviews.org
    > username: rviews

    route-views>show bgp 91.202.196.140

    BGP routing table entry for 91.202.196.0/22, version 2291432774
    Paths: (24 available, best #24, table default)
    Not advertised to any peer
    Refresh Epoch 1
    3561 3910 3356 3216 49821
        206.24.210.80 from 206.24.210.80 (206.24.210.80)
        Origin IGP, localpref 100, valid, external
        path 7FE0DD4C6F48 RPKI State valid
        rx pathid: 0, tx pathid: 0
    Refresh Epoch 1
    57866 3356 3216 49821
    37.139.139.17 from 37.139.139.17 (37.139.139.17)

```

2. Создайте dummy0 интерфейс в Ubuntu. Добавьте несколько статических маршрутов. Проверьте таблицу маршрутизации.

    **Ответ**:

```shell
    sudo ip link add dummy0 type dummy
    sudo ip addr add 10.0.29.0/24 dev dummy0
    sudo ip link set dummy0 up
    ifconfig

    ...
    dummy0: flags=195<UP,BROADCAST,RUNNING,NOARP>  mtu 1500
        inet 10.0.29.0  netmask 255.255.255.0  broadcast 0.0.0.0
        inet6 fe80::d8a5:f7ff:fedc:403f  prefixlen 64  scopeid 0x20<link>
        ether da:a5:f7:dc:40:3f  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2  bytes 140 (140.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    ...


    sudo ip route add 3.3.3.0/24 via 10.0.2.1
    sudo ip route add 8.16.28.0/24 via 10.0.29.0
    ip route

    ...
    8.8.8.0/24 via 10.0.2.1 dev eth0 
    8.16.28.0/24 via 10.0.29.0 dev dummy0 
    10.0.29.0/24 dev dummy0 proto kernel scope link src 10.0.29.0
    ,,,

```

3. Проверьте открытые TCP порты в Ubuntu, какие протоколы и приложения используют эти порты? Приведите несколько примеров.

    **Ответ:**

     - 22 - TCP,

     - UDP - под SSH соединение, использует его sshd - is the OpenSSH server process 
     
     - 53 - TCP,UDP - под DNS, systemd-resolve 

     - 111 - TCP,UDP - под RPC - The rpcbind utility is a server that converts RPC program numbers into universal addresses

     - 9200 - ElasticSeach

```shell
    ss -tpan

    State     Recv-Q    Send-Q        Local Address:Port         Peer Address:Port     Process
    LISTEN    0         4096          127.0.0.53%lo:53                0.0.0.0:*         users:(("systemd-resolve",pid=570,fd=13))
    LISTEN    0         128                 0.0.0.0:22                0.0.0.0:*         users:(("sshd",pid=857,fd=3))
    LISTEN    0         4096                0.0.0.0:111               0.0.0.0:*         users:(("rpcbind",pid=569,fd=4),("systemd",pid=1,fd=35))
    ESTAB     0         0                 10.0.2.15:22               10.0.2.2:58010     users:(("sshd",pid=1148,fd=4),("sshd",pid=1111,fd=4))
    LISTEN    0         128                    [::]:22                   [::]:*         users:(("sshd",pid=857,fd=4))
    LISTEN    0         4096                   [::]:111                  [::]:*         users:(("rpcbind",pid=569,fd=6),("systemd",pid=1,fd=37))
    LISTEN    0         4096          [::ffff:127.0.0.1]:9200             *:*                                                                


```

4. Проверьте используемые UDP сокеты в Ubuntu, какие протоколы и приложения используют эти порты?

    **Ответ:**

```shell
    ss -upan

    State     Recv-Q    Send-Q         Local Address:Port         Peer Address:Port    Process
    UNCONN    0         0              127.0.0.53%lo:53                0.0.0.0:*        users:(("systemd-resolve",pid=570,fd=12))
    UNCONN    0         0             10.0.2.15%eth0:68                0.0.0.0:*        users:(("systemd-network",pid=402,fd=19))
    UNCONN    0         0                    0.0.0.0:111               0.0.0.0:*        users:(("rpcbind",pid=569,fd=5),("systemd",pid=1,fd=36))
    UNCONN    0         0                       [::]:111                  [::]:*        users:(("rpcbind",pid=569,fd=7),("systemd",pid=1,fd=38))

```

5. Используя diagrams.net, создайте L3 диаграмму вашей домашней сети или любой другой сети, с которой вы работали.

     **Ответ:** ![alt l2](https://github.com/asexsela/homework/blob/master/03-sysadmin-08-net/L3.png?raw=true)