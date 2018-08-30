Purpose of task:
-------
Строим файловое хранилище на основе Linux
## H.W.:
vagrant стенд  для NFS или.SAMBA
NFS или SAMBA на выбор
vagrant up должен поднимать 2 виртуалки: сервер и клиент
на сервер должна быть расшарена директория
на клиента она должна автоматически монтироваться при старте ( fstab или autofs)
в шаре должна быть папка upload с правами на запись
- требования дл NFS: NFSv3 по UDP, включенный firewall

* аутентификация через KERBEROS
##  Execution:
Ansible [Playbook.yml](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson28_nfs/Playbook.yml)

Две роли [nfssrv](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson28_nfs/roles/nfs_srv/tasks/main.yml) и [nfsclient](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson28_nfs/roles/nfs_client/tasks/main.yml)

### PrintScreens of avidence
![server_side](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson28_nfs/img/srv.gif)

![client_side](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson28_nfs/img/client.gif)

##### Configs
* server side

/etc/[nfs.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson28_nfs/configs/nfs.conf)

/etc/sysconfig/[nfs](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson28_nfs/configs/sysconfig_nfs)

/etc/[firewall.rules](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson28_nfs/configs/firewall.rules)

/etc/[exports](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson28_nfs/configs/exports)

* client side

/etc/[fstab](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson28_nfs/configs/client_fstab)
