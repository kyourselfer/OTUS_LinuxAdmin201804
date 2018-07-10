##### Драйвер tun(L2-L3) используем при обьединении сетей с разной адресацией в одну (OpenVPN сервер может кидать маршруты для клиентов)

![openvpn_server](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/1/ovpn_server.gif)

![openvpn_client](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/1/ovpn_client.gif)


##### Драйвер tap(L2) используем при подключании клиента в режиме моста (пропускает broadcast) при адресации используем не пересекающиеся адреса из одной подсети

[server_tap.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/1/server_tap.conf)

[bridge_up.sh](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson11_vpn/1/bridge_up.sh)
