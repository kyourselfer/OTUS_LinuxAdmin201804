Настроить все без выключения selinux ddns тоже должен работать без выключения selinux
---------------------
Для настройки SELinux используем пакет policycoreutils-python

Просмотрим настройки политик на доступ к файлам и каталогам для расположения конфигов и файлов зон
`semanage fcontext -l | grep '/etc/named'` 

Cоздадим сопоставляющий эквивалент для /etc/named как для /var/named, т.е. путь /var/named = /etc/named
`semanage fcontext -a -e /var/named /etc/named`

Рекурсивно применим новое правило контекста
`restorecon -R -v /etc/named`

После этого сможем обновить зону без ошибок

![SE Результат](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson13_dns/1/se.gif)

* change_ddnsclient_zone.sh

`#!/bin/bash
/usr/bin/nsupdate -k /etc/named/Kkislovodsk01.ddns.lab.+157+12223.private -v $1`

* changes.txt
```
server ns1.dns.lab
zone ddns.lab
update add kislovodsk01.ddns.lab 3600 IN A 192.168.50.112
send
```

Обновляем зону ddns.lab

`bash change_ddnsclient_zone.sh changes`
