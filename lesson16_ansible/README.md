Домашнее задание
---------------------
### Первые шаги с Ansible.
Переделать разворачивание файрвалла (ДЗ 14) через ansible

[hosts](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson16_ansible/hosts) с параметрами
```
[ForefrontRouters]
ipr01 ansible_ssh_host=127.0.0.1 ansible_port=2222
ipr02 ansible_ssh_host=127.0.0.1 ansible_port=2200
[rootRouters]
centralRouter ansible_ssh_host=127.0.0.1 ansible_port=2201
[WebServers]
centralServer ansible_ssh_host=127.0.0.1 ansible_port=2204
```
[Vagrantfile](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson16_ansible/Vagrantfile) с provisioning на Ansible [playbook](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson16_ansible/Start.yml)

Проверим выход в ИНет `ansible all -i hosts -m shell -a 'ping -c1 -s1 ya.ru`

![ping](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson16_ansible/PrnScr/ping.gif)

Проверим открытость 22/tcp `ansible centralRouter -i hosts -m shell -a 'nc -z -w 1 -v 192.168.255.1 22'` и
постучимся через centralRouter на 192.168.255.1:22 (ipr01) `ansible centralRouter -i hosts -m shell -a 'bash /vagrant/provisioning/ssh_port_knocking.sh'`, сново проверим открытость 22/tcp

![knocking_to](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson16_ansible/PrnScr/knocking_port.gif)

* в рамках ДЗ создать свою роль

[roles/nginx](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/tree/master/lesson16_ansible/roles)
```
- hosts: centralServer
  become: yes
  tasks:
  
  ...
  
  # install nginx
  roles:
    - { role: nginx }
```
