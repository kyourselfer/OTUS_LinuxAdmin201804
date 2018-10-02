LDAP
------------
1. Установить FreeIPA
2. Написать playbook для конфигурации клиента
3. Всю "сетевую лабораторию" перевести на аутентификацию через LDAP

4*. Настроить авторизацию по ssh-ключам

В git - результирующий playbook

Решение:
------
Используется Vagrantfile: в котором provider = VirtualBox и provision = Ansible

```
# Развернем три хоста для проверки inetrouter->centralrouter->ipaserver
for i in "inetrouter centralrouter ipaserver"; do vagrant up $i; done
# Включаем клиента centralrouter в домен otus.local
ansible-playbook -i hosts -vvv -l ipaclients Playbook.yml
```

Подключимся для проверки к FreeIPA - WebUI, создадим пользователя и запросим его group и user ID:

![check_of](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson18_ldap_freeipa/ldap_auth.gif)

Для подключения  `sudo ssh -N -L 443:127.0.0.1:443 vagrant@127.0.0.1 -p 2203` (в hosts `127.0.0.1	localhost ipaserver.otus.local`)
