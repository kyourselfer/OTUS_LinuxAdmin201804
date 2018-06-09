### 2. Поднять RAS на базе OpenVPN с клиентскими сертификатами, подключиться с локальной машины на виртуалку

![Scheme](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/2/schem.jpeg)
                                                           
OpenVPN Server

![OpenVPN Server](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/2/ovpn_server.gif)

OpenVPN Client

![OpenVPN Client](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/2/ovpn_client.gif)

Buh1

![buh1](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/2/buh1.gif)

Buh2

![buh2](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/2/buh2.gif)

Local machine

![local_machine](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/2/local_machine.gif)

# server.conf
...
`server 10.0.0.0 255.255.255.0 # subnet of tunnel`
`route 192.168.112.0 255.255.255.248`
`route 192.168.2.0 255.255.255.0`
`push "route 192.168.111.0 255.255.255.248" # sent to clients`

`ifconfig-pool-persist name-ip_clients.list`
`client-to-client # clients connect between each other`
`client-config-dir /etc/openvpn/ccd`
...
# Клиент inetRouterB отвечает за сети на его стороне
`iroute 192.168.112.0 255.255.255.248`
`iroute 192.168.2.0 255.255.255.0`
# Листинг файл name-ip_clients.list
`inetRouterB 192.168.200.10`
