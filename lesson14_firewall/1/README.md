### Реализован knocking port.

* centralRouter может попасть на ssh inetrRouter через [knock скрипт](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/tree/master/lesson14_firewall/1/scripts)

Прописываем правила:
Пропускаем весь вх.|исх. трафик с lo, eth0 на рутер
```
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -i eth0 -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
iptables -A OUTPUT -o eth0 -j ACCEPT
```
Создаем доп. цепочки
```
iptables -N TRAFFIC
iptables -N SSH1-INPUT
iptables -N SSH2-INPUT
```
Добавляем правила в цепочку SSH1-INPUT
```
iptables -A SSH1-INPUT -m recent --set --name SSH1 --mask 255.255.255.255 --rsource -j DROP

```
Добавляем правила в цепочку SSH2-INPUT
```
# Назначаем переменную имени SSH2 и формируем список по условию --mask 255.255.255.255 --rsource
iptables -A SSH2-INPUT -m recent --set --name SSH2 --mask 255.255.255.255 --rsource -j DROP
```
Добавляем правила в цепочку TRAFFIC
```
# Пропускаем любой тип icmp
iptables -A TRAFFIC -p icmp -m icmp --icmp-type any -j ACCEPT
# Используем модуль state, пропускаем только с определенным(conntrack) состоянием RELATED(новое или рожденное соединение от уже установленного) и ESTABLISHED(установленное)
iptables -A TRAFFIC -m state --state RELATED,ESTABLISHED -j ACCEPT
# Используем модуль state, tcp, recent пропускаем только с определенным(conntrack) состоянием NEW и открывает 22 tcp в течение 30 сек. если подключающийся IP имеется в списке SSH2 
iptables -A TRAFFIC -p tcp -m state --state NEW -m tcp --dport 22 -m recent --rcheck --seconds 30 --name SSH2 --mask 255.255.255.255 --rsource -j ACCEPT
```

Конфигурационный файл [iptables.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson14_firewall/1/iptables.conf)
