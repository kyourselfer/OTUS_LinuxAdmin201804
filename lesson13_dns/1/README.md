Домашнее задание
---------------------
### настраиваем split-dns

взять стенд https://github.com/erlong15/vagrant-bind

добавить еще один сервер client2

завести в зоне dns.lab 

имена

web1 - смотрит на клиент1

web2 смотрит на клиент2

`ls /etc/named`
![ls](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson13_dns/1/ls_zones.gif)

Зона dns.lab.

![dns.lab](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson13_dns/1/dns.lab.gif)

Зона dns.lab.rev.

![dns.lab.rev](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson13_dns/1/dns.lab.rev.gif)

завести еще одну зону newdns.lab

завести в ней запись

www - смотрит на обоих клиентов

Зона newdns.lab.

![newdns.lab](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson13_dns/1/newdns.lab.gif)

настроить split-dns

клиент1 - видит обе зоны, но в зоне dns.lab только web1

![dns.lab_client1](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson13_dns/1/dns.lab_client1.gif)

Обратная 

![dns.lab.rev_client1](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson13_dns/1/dns.lab_client1.rev.gif)

клиент2 видит только dns.lab
