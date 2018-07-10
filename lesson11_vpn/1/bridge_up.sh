#!/bin/bash

openvpn --mktun --dev tap0

systemctl stop openvpn@server.service

brctl addbr br0
for i in eth2 tap0
do
    brctl addif br0 $i
    ifconfig $i 0.0.0.0 promisc up
done

ifconfig br0 192.168.111.11/24

systemctl start openvpn@server.service
