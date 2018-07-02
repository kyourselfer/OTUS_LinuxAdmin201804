4) пробросить 80-й порт на inetRouter2:8080
---------------------
[iptables.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson14_firewall/2/iptables.conf)

DNAT:
Пробрасываем на внешний eth0:8080 и подменяем IP назначения с 192.168.2.111:8080 на 192.168.0.2:80

SNAT:
Заменяем IP источника с 192.168.2.111 на 192.168.254.1

![dnat_snat_8080](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson14_firewall/2/dnat_snat_8080.gif)
