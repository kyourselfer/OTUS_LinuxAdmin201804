Цели занятия:
-------
Строим файловое хранилище на основе Linux
### Д.З.:
vagrant стенд  для NFS или.SAMBA
NFS или SAMBA на выбор
vagrant up должен поднимать 2 виртуалки: сервер и клиент
на сервер должна быть расшарена директория
на клиента она должна автоматически монтироваться при старте ( fstab или autofs)
в шаре должна быть папка upload с правами на запись
- требования дл NFS: NFSv3 по UDP, включенный firewall

* аутентификация через KERBEROS
### Выполнение:

### PrintScreens of avidence

##### configs
* server side
/etc/[nfs.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson28_nfs/configs/nfs.conf)

/etc/sysconfig/[nfs](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson28_nfs/configs/sysconfig_nfs)

/etc/[firewall.rules](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson28_nfs/configs/firewall.rules)

/etc/[exports](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson28_nfs/configs/exports)

* client side
/etc/[fstab](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson28_nfs/configs/client_fstab)
