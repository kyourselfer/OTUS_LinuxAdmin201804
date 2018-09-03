- Поднять три виртуалки

- Объединить их разными vlan
![Схема сети](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/1/ospf_one_area.jpg)

### 1. Поднять OSPF между машинами на базе Quagga
##### вывод ip a
![ip](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/1/routerA1/routerA1_ip.gif)
##### конфиги /etc/quagga/*
[routerA1/ospfd.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/1/routerA1/ospfd.conf)

[routerA1/zebra.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/1/routerA1/zebra.conf)
##### вывод tracepath для каждого из трёх случаев
![path](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/1/routerA1/routerA1_path.gif)
##### вывод ip a
![ip](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/1/routerB1/routerB1_ip.gif)
##### конфиги /etc/quagga/*
[routerB1/ospfd.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/1/routerB1/ospfd.conf)

[routerB1/zebra.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/1/routerB1/zebra.conf)
##### вывод tracepath для каждого из трёх случаев
![path](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/1/routerB1/routerB1_path.gif)
##### вывод ip a
![ip](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/1/routerC1/routerC1_ip.gif)
##### конфиги /etc/quagga/*
[routerC1/ospfd.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/1/routerC1/ospfd.conf)

[routerC1/zebra.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/1/routerC1/zebra.conf)
##### вывод tracepath для каждого из трёх случаев
![path](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/1/routerC1/routerC1_path.gif)
