# Домашнее задание к занятию "6.3. MySQL"

## Задача 1

Используя docker поднимите инстанс MySQL (версию 8). Данные БД сохраните в volume.

Изучите бэкап БД и восстановитесь из него.

Перейдите в управляющую консоль mysql внутри контейнера.

Используя команду \h получите список управляющих команд.

Найдите команду для выдачи статуса БД и приведите в ответе из ее вывода версию сервера БД.

Подключитесь к восстановленной БД и получите список таблиц из этой БД.

Приведите в ответе количество записей с price > 300.

В следующих заданиях мы будем продолжать работу с данным контейнером.


## Ответ: 


 - Запуск контейнера

```shell
    // Качаем образ
    docker pull mysql:8.0

    // Создаем volume
    docker volume create volume_mysql

    // Запускаем контейнер
    docker run --rm -d --name mysql-docker -e MYSQL_ROOT_PASSWORD=mysql -ti -p 3306:3306 -v volume_mysql:/etc/mysql mysql:8.0

    // Подключаемся к контейнеру
    docker exec -it mysql-docker /bin/bash


```

 - Выводод команды \h

![](https://github.com/asexsela/homework/blob/master/06-db-03-mysql/images/mysql_help.png?raw=true)

 - Команда вывода состояния ДБ \s и ее вывод

 ![](https://github.com/asexsela/homework/blob/master/06-db-03-mysql/images/mysql_status.png?raw=true)

  - Список таблиц ДБ

   ![](https://github.com/asexsela/homework/blob/master/06-db-03-mysql/images/mysql_tables.png?raw=true)


 - Приведите в ответе количество записей с price > 300.

![](https://github.com/asexsela/homework/blob/master/06-db-03-mysql/images/mysql_orders_result.png?raw=true)

## Задача 2

Создайте пользователя test в БД c паролем test-pass, используя:

 - плагин авторизации mysql_native_password
 - срок истечения пароля - 180 дней
 - количество попыток авторизации - 3
 - максимальное количество запросов в час - 100
 - аттрибуты пользователя:
   - Фамилия "Pretty"
   - Имя "James"

Предоставьте привелегии пользователю test на операции SELECT базы test_db.

Используя таблицу INFORMATION_SCHEMA.USER_ATTRIBUTES получите данные по пользователю test и приведите в ответе к задаче.

## Ответ: 

```mysql
    CREATE USER 'test'@'localhost' IDENTIFIED BY 'test-pass'
        WITH
        MAX_QUERIES_PER_HOUR 100
        PASSWORD EXPIRE INTERVAL 180 DAY
        FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2
        ATTRIBUTE '{"fname":"James", "lname":"Pretty"}';

    GRANT Select ON test_db.orders TO 'test'@'localhost';

```

 - Используя таблицу INFORMATION_SCHEMA.USER_ATTRIBUTES получите данные по пользователю test и приведите в ответе к задаче


![](https://github.com/asexsela/homework/blob/master/06-db-03-mysql/images/mysql_user.png?raw=true)


## Задача 3

Установите профилирование SET profiling = 1. Изучите вывод профилирования команд SHOW PROFILES;.

Исследуйте, какой engine используется в таблице БД test_db и приведите в ответе.

Измените engine и приведите время выполнения и запрос на изменения из профайлера в ответе:

 - на MyISAM
 - на InnoDB

## Ответ: 


![](https://github.com/asexsela/homework/blob/master/06-db-03-mysql/images/mysql_profiling.png?raw=true)

переключениe на MyISAM: 0.01279000
переключениe на InnoDB: 0.04942325

## Задача 4

Изучите файл my.cnf в директории /etc/mysql.

Измените его согласно ТЗ (движок InnoDB):

 - Скорость IO важнее сохранности данных
 - Нужна компрессия таблиц для экономии места на диске
 - Размер буффера с незакомиченными транзакциями 1 Мб
 - Буффер кеширования 30% от ОЗУ
 - Размер файла логов операций 100 Мб

Приведите в ответе измененный файл my.cnf.

## Ответ: 

```conf
    [mysqld]

    skip-host-cache
    skip-name-resolve
    datadir=/var/lib/mysql
    socket=/var/run/mysqld/mysqld.sock
    secure-file-priv=/var/lib/mysql-files
    user=mysql

    pid-file=/var/run/mysqld/mysqld.pid

    // Changed
    innodb_flush_log_at_trx_commit = 0 
    innodb_file_format=Barracuda
    innodb_log_buffer_size	= 1M
    key_buffer_size = 2GB
    max_binlog_size	= 100M
    
    [client]
    socket=/var/run/mysqld/mysqld.sock


    !includedir /etc/mysql/conf.d/
```