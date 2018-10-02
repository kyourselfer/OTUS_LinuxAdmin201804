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

Подключимся для проверки к FreeIPA - WebUI

![check_of]()
