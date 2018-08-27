Цели занятия:
-------
Учимся администрировать PostgreSQL
Установка, настройка, создаем пользователей и роли
выдаем права, создаем базы,
мониторим, делаем бэкапы
### Д.З.:
PostgreSQL
1. Написать playbook установки postgres.
- в vars вынести версию, так что бы поддерживалась версия 9.6 и 10
- сконфигурировать pg_hba.conf (пересмотрите слайды)
- сконфигурировать postgresql.conf на работу с конкретной машиной (ansible_memtotal_mb вам в помощь)

2. Написать playbook разворачивания реплики с помощью pg_basebackup.

3*. Установить PostgresPro Standard, попробовать бекап и восстановление с помощью pg_probackup

### Выполнение:
[Playbook.yml](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson27_postgresql/Playbook.yml)
 Меняем версию пакета через переменную в Playbook.yml `postgresql_default_version: 10` 9.6 или 10 (возможно использовать 9.3 и выше, на дистрибутивах семейства Debian и RH, но необходима отладка)

Используем для выполнения задания две роли [PGServersMaster](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/tree/master/lesson27_postgresql/roles/PGServersMaster) и [PGServersSlave](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/tree/master/lesson27_postgresql/roles/PGServersSlave)

выносим основные переменные с просчетом относительно RAM(ansible_memtotal_mb) хоста [vars](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson27_postgresql/roles/PGServersMaster/vars/main.yml)/main.yml

template [pg_hba.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson27_postgresql/roles/PGServersMaster/templates/pg_hba.conf.redhat.j2)

[postgresql.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson27_postgresql/roles/PGServersMaster/templates/25ansible_postgresql.conf.j2)

В роли PGServersSlave используем task [pg_basebackup](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson27_postgresql/roles/PGServersSlave/tasks/pg_basebackup.yml)

Подменяем recovery.conf по template [recovery.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson27_postgresql/roles/PGServersSlave/templates/recovery.conf.j2)

### PrintScreens of avidence

