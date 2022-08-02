# Домашнее задание к занятию "5.5. Оркестрация кластером Docker контейнеров на примере Docker Swarm"

## Задача 1

Дайте письменые ответы на следующие вопросы:

- В чём отличие режимов работы сервисов в Docker Swarm кластере: replication и global?
- Какой алгоритм выбора лидера используется в Docker Swarm кластере?
- Что такое Overlay Network?

## Ответ: 

 1. В чём отличие режимов работы сервисов в Docker Swarm кластере: replication и global?

    - **replication** - Вы можете указать количество выполненных задач. Например, вы решаете развернуть три копии экземпляров HTTP, каждый из которых предоставляет один и тот же контент.
    - **global** - Запустите одну и ту же задачу на каждом узле. Нет необходимости указывать количество заданий заранее. Каждый раз, когда узел добавляется в рой, координатор создает задачу, а планировщик назначает задачу новому узлу.

 2. Алгоритм поддержания распределенного консенсуса — **Raft**.

 3. **Оверлейная сеть** — это виртуальная или логическая сеть, созданная поверх существующей физической сети.

## Задача 2

Создать ваш первый Docker Swarm кластер в Яндекс.Облаке

Для получения зачета, вам необходимо предоставить скриншот из терминала (консоли), с выводом команды:


```
docker node ls
```

## Ответ: 

![](https://github.com/asexsela/homework/blob/master/05-virt-05-docker-swarm/images/nodes.png?raw=true)


## Задача 3

Создать ваш первый, готовый к боевой эксплуатации кластер мониторинга, состоящий из стека микросервисов.

Для получения зачета, вам необходимо предоставить скриншот из терминала (консоли), с выводом команды:


```
docker service ls
```

## Ответ: 

![](https://github.com/asexsela/homework/blob/master/05-virt-05-docker-swarm/images/services.png?raw=true)