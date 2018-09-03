- Поднять три виртуалки

- Объединить их разными vlan
![Схема сети](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/3/ospf_one_area%20.jpg)

### Поднять OSPF между машинами на базе Quagga
## Сделать один из линков "дорогим", но что бы при этом роутинг был симметричным
Устанавливаем cost 1000 на routerA1(eth2.10) и на routerB1(eth2.10)
##### вывод `tracepath` и `vtysh -c 'show ip route 10.0.1.1/30'`

##### конфиги /etc/quagga/*
[routerA1/ospfd.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/3/configs/ospfd.conf)

[routerB1/ofpfd.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/2/configs/ospfd.conf)

