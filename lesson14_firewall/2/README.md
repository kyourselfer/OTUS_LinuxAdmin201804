Домашнее задание
---------------------
2) добавить inetRouter2, который виден(маршрутизируется) с хоста

3) запустить nginx на centralServer

4) пробросить 80-й порт на inetRouter2:8080

5) дефолт в инет оставить через inetRouter

DNAT:
Пробрасываем на вн. eth0:8080 и подменяем IP назначения с 192.168.2.111:8080 на 192.168.0.2:80

SNAT:
Заменяем IP источника с 192.168.2.111 на 192.168.254.1

![dnat_snat_8080](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson14_firewall/2/dnat_snat_8080.gif)
