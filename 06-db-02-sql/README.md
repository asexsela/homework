# Домашнее задание к занятию "6.2. SQL"

## Задача 1

Используя docker поднимите инстанс PostgreSQL (версию 12) c 2 volume, в который будут складываться данные БД и бэкапы.

Приведите получившуюся команду или docker-compose манифест.


## Ответ: 

```yaml
   version: "3.7"

   services:
      postgres:
         image: postgres:12
         environment:
            POSTGRES_DB: "test_db"
            POSTGRES_USER: "admin"
            POSTGRES_PASSWORD: "password"
         ports:
            - "5432:5432"
         volumes:
            - ./postgres/vol1:/var/lib/postgresql/data
            - ./postgres/vol2:/var/lib/postgresql
```


## Задача 2


В БД из задачи 1:

 - создайте пользователя test-admin-user и БД test_db
 - в БД test_db создайте таблицу orders и clients (спeцификация таблиц ниже)
 - предоставьте привилегии на все операции пользователю test-admin-user на таблицы БД test_db
 - создайте пользователя test-simple-user
 - предоставьте пользователю test-simple-user права на SELECT/INSERT/UPDATE/DELETE данных таблиц БД test_db


Таблица orders:

 - id (serial primary key)
 - наименование (string)
 - цена (integer)

Таблица clients:

 - id (serial primary key)
 - фамилия (string)
 - страна проживания (string, index)
 - заказ (foreign key orders)

Приведите:

 - итоговый список БД после выполнения пунктов выше,
 - описание таблиц (describe)
 - SQL-запрос для выдачи списка пользователей с правами над таблицами test_db
 - список пользователей с правами над таблицами test_db


## Ответ: 

```sql

   create database test_db;
   create role "test-admin-user" superuser nocreatedb nocreaterole noinherit login;

   create table orders (
      id integer primary key,
      name text,
      price integer,
   );
   create table clients (
      id integer primary key,
      surname text,
      country text,
      order_id integer,
      foreign key (order_id) references orders (id)
   );

   create role "test-simple-user" nosuperuser nocreatedb nocreaterole noinherit login;

   grant select on table public.clients to "test-simple-user";
   grant insert on table public.clients to "test-simple-user";
   grant update on table public.clients to "test-simple-user";
   grant delete on table public.clients to "test-simple-user";
   grant select on table public.orders to "test-simple-user";
   grant insert on table public.orders to "test-simple-user";
   grant update on table public.orders to "test-simple-user";
   grant delete on table public.orders to "test-simple-user";

```
 - итоговый список БД после выполнения пунктов выше
   ![](https://github.com/asexsela/homework/blob/master/06-db-02-sql/images/db_list.png?raw=true)

 - описание таблиц (describe)
   ![](https://github.com/asexsela/homework/blob/master/06-db-02-sql/images/tables.png?raw=true)

 - SQL-запрос для выдачи списка пользователей с правами над таблицами test_db
   ![](https://github.com/asexsela/homework/blob/master/06-db-02-sql/images/grants.png?raw=true)

 - список пользователей с правами над таблицами test_db
   ![](https://github.com/asexsela/homework/blob/master/06-db-02-sql/images/users.png?raw=true)


## Задача 3

Используя SQL синтаксис - наполните таблицы следующими тестовыми данными:

Таблица orders

| Наименование | цена |
|---|---|
| Шоколад  | 10 |
| Принтер  | 3000 |
| Книга  | 500 |
| Монитор  | 7000 |
| Гитара  | 4000 |


Таблица clients

| ФИО | Страна проживания |
|---|---|
| Иванов Иван Иванович  | USA |
| Петров Петр Петрович  | Canada |
| Иоганн Себастьян Бах  | Japan |
| Ронни Джеймс Дио  | Russia |
| Ritchie Blackmore  | Russia |

Используя SQL синтаксис:

 - вычислите количество записей для каждой таблицы
 - приведите в ответе:
   - запросы
   - результаты их выполнения.

## Ответ: 

```sql
   insert into orders values (1, 'Шоколад', 10), (2, 'Принтер', 3000), (3, 'Книга', 500), (4, 'Монитор', 7000), (5, 'Гитара', 4000);
   insert into clients values (1, 'Иванов Иван Иванович', 'USA'), (2, 'Петров Петр Петрович', 'Canada'), (3, 'Иоганн Себастьян Бах', 'Japan'), (4, 'Ронни Джеймс Дио', 'Russia'), (5, 'Ritchie Blackmore', 'Russia');

   select count (*) from orders;
   select count (*) from clients;


```

![](https://github.com/asexsela/homework/blob/master/06-db-02-sql/images/insert.png?raw=true)


## Задача 4

Часть пользователей из таблицы clients решили оформить заказы из таблицы orders.

Используя foreign keys свяжите записи из таблиц, согласно таблице:

| ФИО | Заказ |
|---|---|
| Иванов Иван Иванович  | Книга |
| Петров Петр Петрович  | Монитор |
| Иоганн Себастьян Бах  | Гитара |

## Ответ: 

```sql
   update clients set order_id = 3 where id = 1;
   update clients set order_id = 4 where id = 2;
   update clients set order_id = 5 where id = 3;

   select * from clients where order_id is not null;
```

![](https://github.com/asexsela/homework/blob/master/06-db-02-sql/images/orders.png?raw=true)

## Задача 5

Получите полную информацию по выполнению запроса выдачи всех пользователей из задачи 4 (используя директиву EXPLAIN).

Приведите получившийся результат и объясните что значат полученные значения.

## Ответ: 

Показывает нагрузку на исполнение запроса, и фильтрацию по полю order_id для выборки

![](https://github.com/asexsela/homework/blob/master/06-db-02-sql/images/explain.png?raw=true)

## Задача 6

Создайте бэкап БД test_db и поместите его в volume, предназначенный для бэкапов (см. Задачу 1).

Остановите контейнер с PostgreSQL (но не удаляйте volumes).

Поднимите новый пустой контейнер с PostgreSQL.

Восстановите БД test_db в новом контейнере.

Приведите список операций, который вы применяли для бэкапа данных и восстановления.

## Ответ: 

```sql
   docker exec -t 06-db-02-sql_postgres_1 pg_dump -U admin test_db -f /var/lib/postgresql/data/dump_test.sql

   docker exec -i 06-db-02-sql_postgres_2 psql -U admin -d test_db -f /var/lib/postgresql/data/dump_test.sql
```