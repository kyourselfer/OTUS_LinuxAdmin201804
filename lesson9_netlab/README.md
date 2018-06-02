#  Home work:
Vagrantfile с начальным  построением сети
inetRouter
centralRouter
centralServer

тестировалось на virtualbox

# Планируемая архитектура
построить следующую архитектуру

Сеть office1
- 192.168.2.0/26      - dev
- 192.168.2.64/26    - test servers
- 192.168.2.128/26  - managers
- 192.168.2.192/26  - office hardware

Сеть office2
- 192.168.1.0/25      - dev
- 192.168.1.128/26  - test servers
- 192.168.1.192/26  - office hardware

Сеть central
- 192.168.0.0/28    - directors
- 192.168.0.32/28  - office hardware
- 192.168.0.64/26  - wifi

```
Office1 ---\
      -----> Central --IRouter --> internet
Office2----/
```
Итого должны получится следующие сервера
- inetRouter
- centralRouter
- office1Router
- office2Router
- centralServer
- office1Server
- office2Server

# Теоретическая часть
- Найти свободные подсети
- Посчитать сколько узлов в каждой подсети, включая свободные
- Указать broadcast адрес для каждой подсети
- проверить нет ли ошибок при разбиении

# Практическая часть
- Соединить офисы в сеть согласно схеме и настроить роутинг
- Все сервера и роутеры должны ходить в инет черз inetRouter
- Все сервера должны видеть друг друга
- у всех новых серверов отключить дефолт на нат (eth0), который вагрант поднимает для связи
- при нехватке сетевых интервейсов добавить по несколько адресов на интерфейс

The solution
--------------------------------------
inetRouter

![inetRouter](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson9_netlab/img/inetRouter.gif)

centralRouter

![centralRouter](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson9_netlab/img/centralRouter.gif)

office1Router

![office1Router](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson9_netlab/img/office1Router.gif)

office2Router

![office2Router](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson9_netlab/img/office2Router.gif)

centralServer

![centralServer](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson9_netlab/img/centralServer.gif)

office1Server

![office1Server](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson9_netlab/img/office1Server.gif)

office2Server

![office1Server](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson9_netlab/img/office2Server.gif)



https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson9_netlab/subneting.txt
