### Разворачиваем через Vagrant + Ansible

Настраиваем центральный сервер для сбора логов
--------
Настраиваем центральный сервер для сбора логов
в вагранте поднимаем 2 машины web и log
на web поднимаем nginx
на log настраиваем центральный лог сервер на любой системе на выбор
- journald
- rsyslog
- elk 

настраиваем аудит следящий за изменением конфигов нжинкса 

все критичные логи с web должны собираться и локально и удаленно
все логи с nginx должны уходить на удаленный сервер (локально только критичные)
логи аудита уходят ТОЛЬКО на удаленную систему

* развернуть еще машину elk
и таким образом настроить 2 центральных лог системы elk И какую либо еще
в elk должны уходить только логи нжинкса
во вторую систему все остальное

##### 1. [journald](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/tree/master/lesson21_Journald_ELK/1)
##### 2. [rsyslog](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/tree/master/lesson21_Journald_ELK/2)
##### 3. [elk](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/tree/master/lesson21_Journald_ELK/3_extra)
