Д.З. - Строим бонды и вланы
----------------------
в Office1 в тестовой подсети появляется сервера с доп интерфесами и адресами
во internal сети testLAN
- testClient1 - 10.10.10.254
- testClient2 - 10.10.10.254
- testServer1- 10.10.10.1 
- testServer2- 10.10.10.1

равести вланами
testClient1 <-> testServer1
testClient2 <-> testServer2

между centralRouter и inetRouter
"пробросить" 2 линка (2 internal сети) и объединить их в бонд актив-актив
проверить работу если выборать интерфейсы в бонде по очереди

для сдачи - вагрант файл с требуемой конфигурацией
идеально если с клиента можно попасть ssh на сервер без пароля

Решение
------------------------
* Соединили testClient1, testClient2, testServer1, testServer2 в свитч testLAN с тегированными интерфейсами eth1.1 и eth1.2
на testServer можно попасть через ssh на testClient по связке ключей.

##### [Vagrantfile](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson10_vlanANDbonding/Vagrantfile)

* Создан сетевой интерфейс bond0 в режиме бондинга mode=1 (active-backup):
если активный  eth1, то выключаем для проверки
`ifdown eth1`
перезапускаем bond0 чтобы вошел в ожидание slave интерфейса
`ifdown bond0 && ifup bond0`
подключаем не упавший интерфейс
`ifdown eth2 && ifup eth2`
и линк сново возобновлен.

для получения мониторинга:

`while true; do ifconfig |grep -i -E '(slave|master)' && echo -e "\n" && sleep 1; done`

![ifconfig](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson10_vlanANDbonding/ifconfig.gif)

`while true; do cat /proc/net/bonding/bond0 && sleep 1; done`

![procfs](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson10_vlanANDbonding/procfs.gif)
