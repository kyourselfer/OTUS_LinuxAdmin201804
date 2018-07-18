Домашнее задание
---------------------
### Первые шаги с Ansible.
Переделать разворачивание файрвалла (ДЗ 14) через ansible

[hosts]() с параметрами
```
[ForefrontRouters]
ipr01 ansible_ssh_host=127.0.0.1 ansible_port=2222
ipr02 ansible_ssh_host=127.0.0.1 ansible_port=2200
[rootRouters]
centralRouter ansible_ssh_host=127.0.0.1 ansible_port=2201
[WebServers]
centralServer ansible_ssh_host=127.0.0.1 ansible_port=2204
```
Vagrantfile с provisioning на Ansible [playbook]()

Проверим выход в ИНет `ansible all -i hosts -m shell -a 'ping -c1 -s1 ya.ru`
![ping]()

Постучимся на 
* в рамках ДЗ создать свою роль
