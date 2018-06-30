### Реализован knocking port.

* centralRouter может попасть на ssh inetrRouter через [knock скрипт](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/tree/master/lesson14_firewall/1/scripts)

Прописываем правила:
```
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -i eth0 -j ACCEPT

```

Конфигурационный файл [iptables.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson14_firewall/1/iptables.conf)
