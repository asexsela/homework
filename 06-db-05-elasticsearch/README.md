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

### Dockerfile
```Dockerfile
    FROM centos:7

    RUN curl -SL https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/opensearch-2.x.repo -o /etc/yum.repos.d/opensearch-2.x.repo

    RUN yum clean all

    RUN yum install -y opensearch vim openssl

    CMD ["/usr/sbin/init"]

```

### Dockerhub
https://hub.docker.com/r/asexsela/netology-opensearch