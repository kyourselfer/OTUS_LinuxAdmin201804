### Реализован knocking port.

* centralRouter может попасть на ssh inetrRouter через [knock скрипт](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/tree/master/lesson14_firewall/1/scripts)

Конфигурационный файл [iptables.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson14_firewall/1/iptables.conf)

Прописываем правила:
Создаем доп. цепочки
```
iptables -N TRAFFIC
iptables -N SSH1-INPUT
iptables -N SSH2-INPUT
```
Пропускаем весь вх.|исх. трафик с lo, eth0 на рутер
```
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -i eth0 -j ACCEPT
iptables -A INPUT -j TRAFFIC
iptables -A OUTPUT -o lo -j ACCEPT
iptables -A OUTPUT -o eth0 -j ACCEPT
```
Добавляем правила в цепочку SSH1-INPUT (все unicast адреса источника добавляется в список и дропается)
```
iptables -A SSH1-INPUT -m recent --set --name SSH1 --mask 255.255.255.255 --rsource -j DROP

```
Добавляем правила в цепочку SSH2-INPUT
Настраиваем список для добавления источника адресов SSH2 и формируем список по условию(mod. recent) --mask 255.255.255.255 --rsource с целью сброса без проверки соединение если unicast и он имеется в списке(mod. recent).
```
iptables -A SSH2-INPUT -m recent --set --name SSH2 --mask 255.255.255.255 --rsource -j DROP
```
Добавляем правила в цепочку TRAFFIC
```
iptables -A TRAFFIC -j ACCEPT
# Пропускаем любой тип icmp
iptables -A TRAFFIC -p icmp -m icmp --icmp-type any -j ACCEPT
# Используем модуль state, пропускаем только с определенным(conntrack) состоянием RELATED(новое или рожденное соединение от
уже установленного) и ESTABLISHED(установленное)
iptables -A TRAFFIC -m state --state RELATED,ESTABLISHED -j ACCEPT
# Проверяем на соблюдение всех условий, используем модуль state, tcp, recent пропускаем только с определенным(conntrack) состоянием NEW и destination port 22 tcp и если подключающийся IP имеется в списке SSH2(IP адрес источника явл. unicast), то пропускаем к 22 порту
iptables -A TRAFFIC -p tcp -m state --state NEW -m tcp --dport 22 -m recent --rcheck --seconds 30 --name SSH2 --mask 255.255.255.255 --rsource -j ACCEPT
# если ip source имеется в списке SSH2, но не соблел условие подключения в течение 30 сек., то он удаляется из списка SSH2
iptables -A TRAFFIC -p tcp -m state --state NEW -m tcp -m recent --remove --name SSH2 --mask 255.255.255.255 --rsource -j DROP
# Траффик с conntrack = NEW и с портом назначения 9991 сверяет с IP из листа SSH1 и джампится
в цепочку SSH2-INPUT
iptables -A TRAFFIC -m state --state NEW -m tcp -p tcp --dport 9991 -m recent --rcheck --name SSH1 -j SSH2-INPUT
# если ip source имеется в списке SSH1, но не соблел условие подключения в течение 30 сек., то он удаляется из списка SSH2 и дропается
iptables -A TRAFFIC -p tcp -m state --state NEW -m tcp -m recent --remove --name SSH1 --mask 255.255.255.255 --rsource -j DROP
# если --dport 7777 и ip source имеется в списке SSH0, то джампнуть в цепочку SSH1-INPUT
iptables -A TRAFFIC -p tcp -m state --state NEW -m tcp --dport 7777 -m recent --rcheck --name SSH0 --mask 255.255.255.255 --rsource -j SSH1-INPUT
# если ip source имеется в списке SSH0, но не соблел условие подключения в течение 30 сек., то он удаляется из списка SSH0 и дропается
iptables -A TRAFFIC -p tcp -m state --state NEW -m tcp -m recent --remove --name SSH0 --mask 255.255.255.255 --rsource -j DROP
# если --dport 8881, ip source имеется в списке SSH0, но не соблел условие подключения в течение 30 сек., то дропается
iptables -A TRAFFIC -p tcp -m state --state NEW -m tcp --dport 8881 -m recent --set --name SSH0 --mask 255.255.255.255 --rsource -j DROP
# Остальное в цепочке TRAFFIC джампим на действие DROP
iptables -A TRAFFIC -j DROP
```
Меняем политику дропаем все вх. в таблице filter в цепочке INPUT
```
iptables -t filter -P INPUT DROP
```
Маскарадинг на внешнем eth0 для 192.168.0.0/16
```
iptables -t nat -A POSTROUTING ! -d 192.168.0.0/16 -o eth0 -j MASQUERADE
```
