# Домашнее задание к занятию "3.7. Компьютерные сети, лекция 2"

1. Проверьте список доступных сетевых интерфейсов на вашем компьютере. Какие команды есть для этого в Linux и в Windows?

    **Ответ**: 

        - Linux: ifconfig, ip, nmcli, netstat

        - Windows: Ipconfig, netsh

2. Какой протокол используется для распознавания соседа по сетевому интерфейсу? Какой пакет и команды есть в Linux для этого?

    **Ответ**: Протокол обнаружения соседей NDP(Neighbor Discovery Protocol)
        Пакет и команты: ip, ip neigh show;

3. Какая технология используется для разделения L2 коммутатора на несколько виртуальных сетей? Какой пакет и команды есть в Linux для этого? Приведите пример конфига.

    **Ответ**: 

        - VLAN

        - пакет vlan, ``sudo vconfig add enp0s3 9``, ``sudo ip addr add 10.0.0.9/24 dev enp0s3.9``, ``sudo ip link set up enp0s3.9``

        - Конфиг

```conf
    auto vlan1400
    iface vlan1400 inet static
            address 192.168.1.1
            netmask 255.255.255.0
            vlan_raw_device eth0
    auto eth0.1400iface
        eth0.1400 inet static
            address 192.168.1.1
            netmask 255.255.255.0
            vlan_raw_device eth0
```

4. Какие типы агрегации интерфейсов есть в Linux? Какие опции есть для балансировки нагрузки? Приведите пример конфига.

    **Ответ**: 

        - Статический, Динамический

        - L4, L7

``L4`` - конфиг
```conf
http {  
    upstream backend1 {    
        server 192.168.0.1;    
        server 192.168.0.2;    
        server 192.168.0.3;  
    }  

    server {    
        listen 80;    
        location / {      
            proxy_pass http://backend1;    
        }  
    }
}
# балансировка UDP - DNS 
stream {  
    upstream dns_backends {    
        server 8.8.8.8:53;    
        server 8.8.4.4:53;  
    }  
        
    server {   
        listen 53 udp;    
        proxy_pass dns_backends;    
        proxy_responses 1;  
    }
}

```
``L7`` - конфиг
```conf
http{	
	upstream allbackend {
		server 127.0.0.1:2222;
		server 127.0.0.1:3333;
		server 127.0.0.1:4444;
		server 127.0.0.1:5555;
	}

	upstream app1backend{
	    server 127.0.0.1:2222;
	    server 127.0.0.1:3333;
	}

	upstream app2backend{
	    server 127.0.0.1:4444;
	    server 127.0.0.1:5555;
  	}

	server{

		listen 80;
		
		location /{
			proxy_pass http://allbackend/;
		}

		location /app1{
			proxy_pass http://app1backend/;
		}

		location /app2{
		    proxy_pass http://app2backend/;
		}	

		location /admin{
			return 403;
		}
	}
}

```

5. Сколько IP адресов в сети с маской /29 ? Сколько /29 подсетей можно получить из сети с маской /24. Приведите несколько примеров /29 подсетей внутри сети 10.10.10.0/24.

    **Ответ**:

        - 8 адресов

        - 32

        - 10.10.10.0/29, 10.10.10.8/29, 10.10.10.16/29,

6. Задача: вас попросили организовать стык между 2-мя организациями. Диапазоны 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 уже заняты. Из какой подсети допустимо взять частные IP адреса? Маску выберите из расчета максимум 40-50 хостов внутри подсети.

    **Ответ**: 

        - 100.64.0.0 — 100.127.255.255 с маской 255.192.0.0 (/10)

        - Маску выберите из расчета максимум 40-50 хостов внутри подсети.

```bash
    ipcalc 100.64.0.0/10 -s 50

    Output:

    Needed size:  64 addresses.
    Used network: 100.64.0.0/26
    Unused:
    100.64.0.64/26
    100.64.0.128/25
    100.64.1.0/24
    100.64.2.0/23
    100.64.4.0/22
    100.64.8.0/21
    100.64.16.0/20
    100.64.32.0/19
    100.64.64.0/18
    100.64.128.0/17
    100.65.0.0/16
    100.66.0.0/15
    100.68.0.0/14
    100.72.0.0/13
    100.80.0.0/12
    100.96.0.0/11

    #оптимальным решением будут подсети /26 по 64 хоста.

```

7. Как проверить ARP таблицу в Linux, Windows? Как очистить ARP кеш полностью? Как из ARP таблицы удалить только один нужный IP?

    **Ответ**:

        - arp -a(windows), arp(linux)

        - netsh interface ip delete arpcache(windows), ip neigh flush all(linux)