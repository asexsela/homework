# Домашнее задание к занятию "6.4. PostgreSQL"

## Задача 1
В этом задании вы потренируетесь в:

 - установке elasticsearch
 - первоначальном конфигурировании elastcisearch
 - запуске elasticsearch в docker

Используя докер образ centos:7 как базовый и документацию по установке и запуску Elastcisearch:

 - составьте Dockerfile-манифест для elasticsearch
 - соберите docker-образ и сделайте push в ваш docker.io репозиторий
 - запустите контейнер из получившегося образа и выполните запрос пути / c хост-машины

Требования к elasticsearch.yml:

 - данные path должны сохраняться в /var/lib
 - имя ноды должно быть netology_test

В ответе приведите:

 - текст Dockerfile манифеста
 - ссылку на образ в репозитории dockerhub
 - ответ elasticsearch на запрос пути / в json виде

Подсказки:

 - возможно вам понадобится установка пакета perl-Digest-SHA для корректной работы пакета shasum
 - при сетевых проблемах внимательно изучите кластерные и сетевые настройки в elasticsearch.yml
 - при некоторых проблемах вам поможет docker директива ulimit
 - elasticsearch в логах обычно описывает проблему и пути ее решения
 
Далее мы будем работать с данным экземпляром elasticsearch.

## Ответ

```bash
    # Собираем докер образ
    docker build --rm -t asexsela/netology-opensearch:latest .
    # Запускаем образ
    docker run --rm -itd -p 127.0.0.1:9300:9200 --network host --privileged  asexsela/netology-opensearch
    # Подключаемся к контейнеру
    docker exec -it {image_id} bash
    # Запускаем opensearch
    systemctl start opensearch.service
    # Проверяем работу сервиса
    curl -XGET https://localhost:9200 -u 'admin:admin' --insecure

```

#### Dockerfile

```Dockerfile
    FROM centos:7

    RUN curl -SL https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/opensearch-2.x.repo -o /etc/yum.repos.d/opensearch-2.x.repo

    RUN yum clean all

    RUN yum install -y opensearch vim openssl

    CMD ["/usr/sbin/init"]

```

#### Dockerhub

https://hub.docker.com/r/asexsela/netology-opensearch

#### Opensearch output localhost:9200

```json
{
    "name" : "netology_test",
    "cluster_name" : "opensearch",
    "cluster_uuid" : "UbDfRU-USPyzdFCTgWjg0w",
    "version" : {
        "distribution" : "opensearch",
        "number" : "2.2.0",
        "build_type" : "rpm",
        "build_hash" : "b1017fa3b9a1c781d4f34ecee411e0cdf930a515",
        "build_date" : "2022-08-09T02:27:29.062212502Z",
        "build_snapshot" : false,
        "lucene_version" : "9.3.0",
        "minimum_wire_compatibility_version" : "7.10.0",
        "minimum_index_compatibility_version" : "7.0.0"
    },
    "tagline" : "The OpenSearch Project: https://opensearch.org/"
}
```

## Задача 2

В этом задании вы научитесь:

 - создавать и удалять индексы
 - изучать состояние кластера
 - обосновывать причину деградации доступности данных
 
Ознакомтесь с документацией и добавьте в elasticsearch 3 индекса, в соответствии со таблицей:

| Имя | Количество реплик | Количество шард
| --- | --- | ---
| ind-1 | 0 | 1
| ind-2 | 1 | 2
| ind-3 | 2 | 4

Получите список индексов и их статусов, используя API и приведите в ответе на задание.

Получите состояние кластера elasticsearch, используя API.

Как вы думаете, почему часть индексов и кластер находится в состоянии yellow?

Удалите все индексы.


#### Создаем индексы

```shell
    # Создаем первый индекс
    curl -X PUT "localhost:9200/ind-1?pretty" -u 'admin:admin' --insecure -H 'Content-Type: application/json' -d'
    {
    "settings": {
        "index": {
            "number_of_shards": 1,  
            "number_of_replicas": 0 
            }
        }
    }
    '
    # Ответ
    {
        "acknowledged" : true,
        "shards_acknowledged" : true,
        "index" : "ind-1"
    }

    # Создаем второй индекс
    curl -X PUT "localhost:9200/ind-2?pretty" -u 'admin:admin' --insecure -H 'Content-Type: application/json' -d'
    {
    "settings": {
        "index": {
            "number_of_shards": 2,  
            "number_of_replicas": 1 
            }
        }
    }
    '
    # Ответ
    {
        "acknowledged" : true,
        "shards_acknowledged" : true,
        "index" : "ind-2"
    }

     # Создаем третий индекс
    curl -X PUT "localhost:9200/ind-3?pretty" -u 'admin:admin' --insecure -H 'Content-Type: application/json' -d'
    {
    "settings": {
        "index": {
            "number_of_shards": 4,  
            "number_of_replicas": 2 
            }
        }
    }
    '
    # Ответ
    {
        "acknowledged" : true,
        "shards_acknowledged" : true,
        "index" : "ind-3"
    }

```

#### Получаем список всех индексов

```shell
    curl -X GET "localhost:9200/_cat/indices?pretty" -u 'admin:admin' --insecure

    # Ответ
    green  open ind-1                        TLDKAAs1TZaBSK7xJN-jzw 1 0  0 0   208b   208b
    green  open .opendistro_security         b0nzzvjXQt2KGJ8OnlkeBQ 1 0 10 0 69.2kb 69.2kb
    yellow open ind-3                        Eku5P6gPTVex3h4SbaQgDw 4 2  0 0   832b   832b
    yellow open security-auditlog-2022.08.24 oKgSpZpyTkWkJKJW_UpP8Q 1 1  5 0 80.3kb 80.3kb
    yellow open ind-2                        dmt5peTuRHSxkHoRZX7jUg 2 1  0 0   416b   416b

```


#### Получаем состояние кластера

```shell
    curl -X GET "localhost:9200/_cluster/health?pretty" -u 'admin:admin' --insecure

    # Ответ
    {
        "cluster_name" : "opensearch",
        "status" : "yellow",
        "timed_out" : false,
        "number_of_nodes" : 1,
        "number_of_data_nodes" : 1,
        "discovered_master" : true,
        "discovered_cluster_manager" : true,
        "active_primary_shards" : 9,
        "active_shards" : 9,
        "relocating_shards" : 0,
        "initializing_shards" : 0,
        "unassigned_shards" : 11,
        "delayed_unassigned_shards" : 0,
        "number_of_pending_tasks" : 0,
        "number_of_in_flight_fetch" : 0,
        "task_max_waiting_in_queue_millis" : 0,
        "active_shards_percent_as_number" : 45.0
    }

```

#### Как вы думаете, почему часть индексов и кластер находится в состоянии yellow?

Потому что у них указано число реплик, а по факту нет других серверов, соответсвено реплицировать некуда.

#### Удаляем индексы

```shell 
    curl -X DELETE "localhost:9200/ind-1?pretty" -u 'admin:admin' --insecure
    curl -X DELETE "localhost:9200/ind-2?pretty" -u 'admin:admin' --insecure
    curl -X DELETE "localhost:9200/ind-3?pretty" -u 'admin:admin' --insecure

    # Ответ

    {
        "acknowledged" : true
    }
```


## Задача 3

В данном задании вы научитесь:

 - создавать бэкапы данных
 - восстанавливать индексы из бэкапов

Создайте директорию {путь до корневой директории с elasticsearch в образе}/snapshots.

Используя API зарегистрируйте данную директорию как snapshot repository c именем netology_backup.

Приведите в ответе запрос API и результат вызова API для создания репозитория.

Создайте индекс test с 0 реплик и 1 шардом и приведите в ответе список индексов.

Создайте snapshot состояния кластера elasticsearch.

Приведите в ответе список файлов в директории со snapshotами.

Удалите индекс test и создайте индекс test-2. Приведите в ответе список индексов.

Восстановите состояние кластера elasticsearch из snapshot, созданного ранее.

Приведите в ответе запрос к API восстановления и итоговый список индексов.

#### Регистрируем репозиторий

```shell
    curl -X PUT "localhost:9200/_snapshot/netology_backup?pretty" -u 'admin:admin' --insecure -H 'Content-Type: application/json' -d'
    {
        "type": "fs",
        "settings": {
            "location": "/etc/opensearch/snapshots/netology_backup"
        }
    }
    '
    # Ответ
    {
        "acknowledged" : true
    }

```

#### Создаем индекс

```shell
    curl -X PUT "localhost:9200/test?pretty" -u 'admin:admin' --insecure -H 'Content-Type: application/json' -d'
    {
    "settings": {
        "index": {
            "number_of_shards": 1,  
            "number_of_replicas": 0 
            }
        }
    }
    '

    # Ответ
    {
        "acknowledged" : true,
        "shards_acknowledged" : true,
        "index" : "test"
    }

    # Список индексов
    curl -X GET "localhost:9200/_cat/indices?pretty" -u 'admin:admin' --insecure

    green  open test                         VAWVB2z7SPOPu101yAkLlA 1 0  0 0    208b    208b
    green  open .opendistro_security         b0nzzvjXQt2KGJ8OnlkeBQ 1 0 10 0  69.2kb  69.2kb
    yellow open security-auditlog-2022.08.24 oKgSpZpyTkWkJKJW_UpP8Q 1 1  9 0 141.6kb 141.6kb

```


#### Создаем снимок

```shell

    curl -X PUT "localhost:9200/_snapshot/netology_backup/%3Cnetology_snapshot_%7Bnow%2Fd%7D%3E?pretty" -u 'admin:admin' --insecure

    # Ответ
    {
        "accepted" : true
    }
    
    # Список файлов в директории со снимками
    [root@alex-MS-7B89 opensearch]# ls -la snapshots/
    total 16
    drwxr-sr-x 3 opensearch opensearch 4096 Aug 24 23:11 .
    drwxr-sr-x 1 opensearch opensearch 4096 Aug 24 22:56 ..
    drwxr-sr-x 3 opensearch opensearch 4096 Aug 24 23:18 netology_backup
    [root@alex-MS-7B89 opensearch]# ls -la snapshots/netology_backup/
    total 28
    drwxr-sr-x 3 opensearch opensearch 4096 Aug 24 23:18 .
    drwxr-sr-x 3 opensearch opensearch 4096 Aug 24 23:11 ..
    -rw-r--r-- 1 opensearch opensearch  983 Aug 24 23:18 index-0
    -rw-r--r-- 1 opensearch opensearch    8 Aug 24 23:18 index.latest
    drwxr-sr-x 5 opensearch opensearch 4096 Aug 24 23:18 indices
    -rw-r--r-- 1 opensearch opensearch  372 Aug 24 23:18 meta-mlG_9EFJScmebyKoqcmr3g.dat
    -rw-r--r-- 1 opensearch opensearch  335 Aug 24 23:18 snap-mlG_9EFJScmebyKoqcmr3g.dat
    

```

#### Удаляем индекс

```shell
    curl -X DELETE "localhost:9200/test?pretty" -u 'admin:admin' --insecure

    # Ответ
    {
        "acknowledged" : true
    }

    # Список индексов
    curl -X GET "localhost:9200/_cat/indices?pretty" -u 'admin:admin' --insecure

    green  open .opendistro_security         b0nzzvjXQt2KGJ8OnlkeBQ 1 0 10 0  69.2kb  69.2kb
    yellow open security-auditlog-2022.08.24 oKgSpZpyTkWkJKJW_UpP8Q 1 1 11 0 189.9kb 189.9kb

```

#### Создаем индекс

```shell
    curl -X PUT "localhost:9200/test-2?pretty" -u 'admin:admin' --insecure -H 'Content-Type: application/json' -d'
    {
    "settings": {
        "index": {
            "number_of_shards": 1,  
            "number_of_replicas": 0 
            }
        }
    }
    '

    # Список индексов
    curl -X GET "localhost:9200/_cat/indices?pretty" -u 'admin:admin' --insecure
    green  open test-2                       uwwP6FQXT56A194aGR0OnA 1 0  0 0   208b   208b
    green  open .opendistro_security         b0nzzvjXQt2KGJ8OnlkeBQ 1 0 10 0 69.2kb 69.2kb
    yellow open security-auditlog-2022.08.24 oKgSpZpyTkWkJKJW_UpP8Q 1 1 12 0 64.9kb 64.9kb

```



#### Восстанавливаем снимок

```shell
    # Получаем список снимков
    curl -X GET "localhost:9200/_cat/snapshots/netology_backup?pretty" -u 'admin:admin' --insecure 
    # Ответ
    netology_snapshot_2022.08.24 SUCCESS 1661383133 23:18:53 1661383133 23:18:53 200ms 3 3 0 3

    # Восстанваливаем
    curl -X POST "localhost:9200/_snapshot/netology_backup/netology_snapshot_2022.08.24/_restore?pretty" -u 'admin:admin' --insecure -H 'Content-Type: application/json'

    # Список индексов
    curl -X GET "localhost:9200/_cat/indices?pretty" -u 'admin:admin' --insecure
    
    green  open test                         VAWVB2z7SPOPu101yAkLlA 1 0  0 0   208b   208b
    green  open test-2                       uwwP6FQXT56A194aGR0OnA 1 0  0 0   208b   208b
    green  open .opendistro_security         b0nzzvjXQt2KGJ8OnlkeBQ 1 0 10 0 69.2kb 69.2kb
    yellow open security-auditlog-2022.08.24 oKgSpZpyTkWkJKJW_UpP8Q 1 1 12 0 64.9kb 64.9kb


```