# Домашнее задание к занятию "5.1. Введение в виртуализацию. Типы и функции гипервизоров. Обзор рынка вендоров и областей применения."


## 1. Опишите кратко, как вы поняли: в чем основное отличие полной (аппаратной) виртуализации, паравиртуализации и виртуализации на основе ОС.

### Ответ:

> 1. Полная(аппаратная) виртуализация испольщует ресурсы сервера и ей не нужна операционная система для управления виртуальной машиной.
> 2. Паравиртуализацияиспользует операционную систему для разделения ресурсов с виртуальной машиной
> 3. Виртуализация на основе ОС запускает небольшие копии самой ОС в контейнерах

## 2. Выберите один из вариантов использования организации физических серверов, в зависимости от условий использования.

**Организация серверов:**

 - физические сервера,
 - паравиртуализация,
 - виртуализация уровня ОС.

**Условия использования:**

 - Высоконагруженная база данных, чувствительная к отказу.
 - Различные web-приложения.
 - Windows системы для использования бухгалтерским отделом.
 - Системы, выполняющие высокопроизводительные расчеты на GPU.

***Опишите, почему вы выбрали к каждому целевому использованию такую организацию.***

### Ответ:

> 1. Для базы данных я бы выбрал аппаратную виртуализацию можно выделить максимум ресурсов пресурсов для виртуальной машины и обеспечить отказоустойчивость
> 2. Для различных веб приложений я бы выбрал виртуализацию уровня ОС(например в Docker) потому что их легче масштабировать при нагрузке на сервер
> 3.Windows системы для использования бухгалтерским отделом я бы на Hyper-V(паравиртуализация) потому что это продукт Microsoft и ее будет легче обслуживать и настраивать
> 4. Системы, выполняющие высокопроизводительные расчеты на GPU я бы разверунл на апаппаратной виртуализации потому что на ней можно задействовать масимум ресурсов

## 3. Выберите подходящую систему управления виртуализацией для предложенного сценария. Детально опишите ваш выбор.


**Сценарии:**

 - 100 виртуальных машин на базе Linux и Windows, общие задачи, нет особых требований. Преимущественно Windows based инфраструктура, требуется реализация программных балансировщиков нагрузки, репликации данных и автоматизированного механизма создания резервных копий.

 - Требуется наиболее производительное бесплатное open source решение для виртуализации небольшой (20-30 серверов) инфраструктуры на базе Linux и Windows виртуальных машин.

 - Необходимо бесплатное, максимально совместимое и производительное решение для виртуализации Windows инфраструктуры.

 - Необходимо рабочее окружение для тестирования программного продукта на нескольких дистрибутивах Linux.

 ### Ответ:

 > 1. Я бы наверное выбрал продукты vmware vSphere или ESXi потому что управлять таким количеством серверов будет удобнее и и нет ограничений к гостевым ОС
 > 2. Склоняюсь к KVM с Proxmox они производительные и бесплатные
 > 3. Скорее всего я бы выбрал Hyper-V бесплатную версию потому что это продукт microsoft и он современный
 > 4. Я бы выбрал Docker он позволяет быстро поднимать контейнеры для тестирования с использрованием автоматизации

## 4. Опишите возможные проблемы и недостатки гетерогенной среды виртуализации (использования нескольких систем управления виртуализацией одновременно) и что необходимо сделать для минимизации этих рисков и проблем. Если бы у вас был выбор, то создавали бы вы гетерогенную среду или нет? Мотивируйте ваш ответ примерами.

### Ответ:

> Я думаю ими сложно управлять, физические ресурсы будут разделены и потребуют различных методов организации серверов, различные навыки в обслуживании различных систем виртуализации и подхода к аппаратным требованиям
Я бы не стал создавать такую среду в силу своего опыта, а выбрал бы однородную среду которую легче масштабировать и упровлять ей.