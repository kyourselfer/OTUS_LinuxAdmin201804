##### Драйвер tun(L2-L3) используем при обьединении сетей с разной адресацией в одну (OpenVPN сервер может кидать маршруты для клиентов)

![openvpn_server](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/1/ovpn_server.gif)

![openvpn_client](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/1/ovpn_client.gif)


##### Драйвер tap(L2) используем при подключании клиента в режиме моста (пропускает broadcast) при адресации используем не пересекающиеся адреса из одной подсети

[server_tap.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/1/server_tap.conf)

[bridge_up.sh](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/1/bridge_up.sh)

До обьядинения интерфейсов в bridge

![server_ip_before_BridgeUp](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/1/tap_ip_a.gif)

запускаем `bash bridge_up.sh`

![server_ip_after_BridgeUp](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/1/tap_ip_a_bridgeUp.gif)

клиент получает ip из стоки `server-bridge 192.168.111.0 255.255.255.0 192.168.111.10 192.168.111.20` в `server.conf` ![client](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/1/tap_ip_a_client.gif)

проверяем 

![check](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/1/tap_ip_a_check.gif)
