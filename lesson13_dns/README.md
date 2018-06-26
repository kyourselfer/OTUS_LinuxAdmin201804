Домашнее задание
---------------------
[настраиваем split-dns](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/tree/master/lesson13_dns/1)

взять стенд https://github.com/erlong15/vagrant-bind [Vagrantfile_vm](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson13_dns/Vagrantfile)

Конфиги:
* [server_master](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson13_dns/1/named_master.conf)
* [server_slave](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson13_dns/1/named_slave.conf)
* [client_ddns](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson13_dns/1/clientddns/)


добавить еще один сервер client2

завести в зоне dns.lab 

имена

web1 - смотрит на клиент1

web2 смотрит на клиент2

завести еще одну зону newdns.lab

завести в ней запись

www - смотрит на обоих клиентов

настроить split-dns

клиент1 - видит обе зоны, но в зоне dns.lab только web1

клиент2 видит только dns.lab

*) [настроить все без выключения selinux
ddns тоже должен работать без выключения selinux](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/tree/master/lesson13_dns/extra)
