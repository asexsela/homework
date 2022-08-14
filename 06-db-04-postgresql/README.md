# Домашнее задание к занятию "6.4. PostgreSQL"

## Задача 1

Используя docker поднимите инстанс PostgreSQL (версию 13). Данные БД сохраните в volume.
Подключитесь к БД PostgreSQL используя psql.
Воспользуйтесь командой \? для вывода подсказки по имеющимся в psql управляющим командам.
Найдите и приведите управляющие команды для:

 - вывода списка БД
 - подключения к БД
 - вывода списка таблиц
 - вывода описания содержимого таблиц
 - выхода из psql

## Ответ

 - Инстанс и volume

   ![](https://github.com/asexsela/homework/blob/master/06-db-04-postgresql/images/up.png?raw=true)

 - вывода списка БД
 - подключения к БД
 - вывода списка таблиц

   ![](https://github.com/asexsela/homework/blob/master/06-db-04-postgresql/images/connect.png?raw=true)

 - вывода описания содержимого таблиц
 - выхода из psql

  ![](https://github.com/asexsela/homework/blob/master/06-db-04-postgresql/images/table_info.png?raw=true)


## Задача 2

Используя psql создайте БД test_database.

Изучите бэкап БД.
Восстановите бэкап БД в test_database.
Перейдите в управляющую консоль psql внутри контейнера.
Подключитесь к восстановленной БД и проведите операцию ANALYZE для сбора статистики по таблице.
Используя таблицу pg_stats, найдите столбец таблицы orders с наибольшим средним значением размера элементов в байтах.
Приведите в ответе команду, которую вы использовали для вычисления и полученный результат.

## Ответ

 - Создание базы
 
    ![](https://github.com/asexsela/homework/blob/master/06-db-04-postgresql/images/db_create.png?raw=true)

 - Восстановление бекапа
 
    ![](https://github.com/asexsela/homework/blob/master/06-db-04-postgresql/images/db_backup.png?raw=true)

 - Перейдите в управляющую консоль psql внутри контейнера.
 - Подключитесь к восстановленной БД и проведите операцию ANALYZE для сбора статистики по таблице.
 - Используя таблицу pg_stats, найдите столбец таблицы orders с наибольшим средним значением размера элементов в байтах.

   ![](https://github.com/asexsela/homework/blob/master/06-db-04-postgresql/images/db_analyze.png?raw=true)



## Задача 3

Архитектор и администратор БД выяснили, что ваша таблица orders разрослась до невиданных размеров и поиск по ней занимает долгое время. Вам, как успешному выпускнику курсов DevOps в нетологии предложили провести разбиение таблицы на 2 (шардировать на orders_1 - price>499 и orders_2 - price<=499).

Предложите SQL-транзакцию для проведения данной операции.

Можно ли было изначально исключить "ручное" разбиение при проектировании таблицы orders?

## Ответ

```sql
    -- Переименовываем таблицу, что бы создать новую
    alter table orders rename to orders_old;
    -- Создаем таблицу orders с разделами по цене
    create table orders (id integer, title varchar(80), price integer) partition by range(price);
    -- Создаем таблицу для раздела с ценой меньше 499
    create table orders_1 partition of orders for values from (0) to (499);
    -- Создаем таблицу для раздела с ценой больше 499
    create table orders_2 partition of orders for values from (499) to (999999999);
    -- Вставляем данные из старой таблицы
    insert into orders (id, title, price) select * from orders_old;
    -- Удаляем старую таблицу
    drop table orders_old;
```

Если бы мы сразу создали таблицу с разделами, то не пришлось бы выполнять данные со старой таблицей


## Задача 4

Используя утилиту pg_dump создайте бекап БД test_database.

Как бы вы доработали бэкап-файл, чтобы добавить уникальность значения столбца title для таблиц test_database?


## Ответ

 - Backup
    ![](https://github.com/asexsela/homework/blob/master/06-db-04-postgresql/images/db_new_backup.png?raw=true)

 - Unique title

```sql
    alter table only test_database add unique (title);

    alter table test_database add unique (title);
    alter index title
        attach partition title;

```