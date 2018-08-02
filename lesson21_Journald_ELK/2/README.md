### Настраиваем центральный сервер для сбора логов rsyslog
--------
##### rsyslog
![rsyslogd](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/img/rsyslogd.gif)
Роль [rsyslogSrv](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/rsyslogSrv/tasks/main.yml)
добавляем /etc/rsyslog.d/nginx_logs.conf (принимаем сообщения по шаблону и складываем в директорию ), roles/rsyslogSrv/files/server_rsyslog.conf
```

```

```
Опции для rsyslogd /etc/sysconfig/rsyslog
В системе запускаются два демона протоколирования - rsyslogd и klogd
```


##### auditd
#Изменим конфиг демона auditd
auditd.conf

#Cлежение за конфигами
rules.d\[audit.rules]()
rules.d\[pam.rules]()
rules.d\[sshd.rules]()

#Слежение за конфигами nginx
rules.d\[nginx.rules]()
```
/etc/audit/auditd.conf - настройки поведения auditd;
/etc/audit/rules.d/audit.rules - правила аудита
autrace - аудит событий, порождаемых указанным процессом (like a strace);
ausearch - поиск событий в журнальных файлах;
aureport - генерирует суммарные отчеты о работе системы аудита;
```
