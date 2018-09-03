- Поднять три виртуалки

- Объединить их разными vlan
![Схема сети](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/1/ospf_one_area.jpg)

### Поднять OSPF между машинами на базе Quagga
## Изобразить ассиметричный роутинг
Устанавливаем cost 1000 на routerB1(eth2.10)
##### вывод `tracepath` и `vtysh -c 'show ip route 10.0.1.1/30'`
![simetric](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/2/asimetric.png)
##### конфиги /etc/quagga/*
[routerB1/ofpfd.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson12_ospf/2/configs/ospfd.conf)
