### Домашнее задание
Настраиваем центральный сервер для сбора логов rsyslog
--------

### Разворачиваем три сервера при помощи Vagrant+Ansible:
##### rsyslogd

![rsyslogd](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/img/rsyslogd.gif)

#Options for rsyslogd /etc/sysconfig/rsyslog

#В системе запускаются два демона протоколирования - syslogd и klogd

##### auditd
```
/etc/audit/auditd.conf - настройки поведения auditd;
/etc/audit/rules.d/audit.rules - правила аудита
autrace - аудит событий, порождаемых указанным процессом (like a strace);
ausearch - поиск событий в журнальных файлах;
aureport - генерирует суммарные отчеты о работе системы аудита;
```
