Настраиваем центральный сервер для сбора логов в вагранте поднимаем 2 машины web и log на web поднимаем nginx на log настраиваем центральный лог сервер на любой системе на выбор.
Настраиваем аудит следящий за изменением конфигов нжинкса.
Все критичные логи с web должны собираться и локально и удаленно все логи с nginx должны уходить на удаленный сервер (локально только критичные) логи аудита уходят ТОЛЬКО на удаленную систему.
### Настраиваем центральный сервер для сбора логов rsyslog
--------
##### rsyslog
Роль [rsyslogSrv](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/rsyslogSrv/tasks/main.yml)

Заменяем конфиг /etc/[rsyslog.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/rsyslogSrv/files/server_rsyslog.conf)

Добавляем /etc/rsyslog.d/[nginx_logs.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/rsyslogSrv/files/server_rsyslog_nginx.conf) (принимаем сообщения по шаблону и складываем в директорию /var/log/remote/$ip)

Добавляем audit_logs.conf в /etc/rsyslog.d/[audit_logs.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/rsyslogSrv/files/server_rsyslog_audit.conf)
Роль [rsyslogClient](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/rsyslogClient/tasks/main.yml)

Добавляем конфиг для отправки критических событий на сервер и локально
/etc/rsyslog.d/[crit.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/rsyslogClient/files/crit.conf)

Заменяем конфиг для клиента /etc/[rsyslog.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/rsyslogClient/files/client_rsyslog.conf)

Роль [nginx](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/nginx/tasks/main.yml)

#Следим за файлами логов nginx и отправляем от оборудывания(Facility) используя local6 и template `$template simple, "<174> %msg%", \n local6.* @@192.168.168.111;simple`, а точнее `PRI = (facility * 2^3) + severity` (на стороне клиента) и важности(Facility) на сервер логов logsrv

#Также следим за audit.log и кидаем по local4 используя шаблон и формулу PRI `$template simple2, "<166> %msg%"` и template `local4.* @@192.168.168.111;simple2` PRI=`20(local4) * 8(2^3) + 6(Info)`

[facility,serivity](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/2/table.txt)

Добавляем конфиг для отправки событий
/etc/rsyslog.d/[nginx.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/nginx/files/nginx_syslog.conf)

Также Nginx c версии 1.7.1 умеет отправлять в syslog
```
$ModLoad imfile

# error log
$InputFileName /var/log/nginx/error.log
$InputFileTag nginx:
$InputFileStateFile stat-nginx-error
$InputFileSeverity error
$InputFileFacility local6
$InputFilePollInterval 1
$InputRunFileMonitor

# access log
$InputFileName /var/log/nginx/access.log
$InputFileTag nginx:
$InputFileStateFile stat-nginx-access
$InputFileSeverity notice
$InputFileFacility local6
$InputFilePollInterval 1
$InputRunFileMonitor

$template simple, "<174> %msg%"

local6.* @@192.168.168.111;simple
```
Проверим отправку событий по local4.info или PRI=166
![audit_syslog](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/img/audit_syslog.gif)

##### auditd
#Изменим конфиг демона auditd
[auditd.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/CentOS_Srv/files/auditd.conf)

#Cлежение за конфигами

rules.d\[audit.rules](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/CentOS_Srv/files/audit.rules)

rules.d\[pam.rules](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/CentOS_Srv/files/pam.rules)

rules.d\[sshd.rules](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/CentOS_Srv/files/sshd.rules)

#Слежение за конфигами nginx
rules.d\[nginx.rules](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/nginx/files/nginx.rules)

```
[root@web01 vagrant]# auditctl -l
-w /etc/audit/auditd.conf -p wa -k auditd
-w /etc/audit/audit.rules -p wa -k auditd
-w /etc/libaudit.conf -p wa -k auditd
-w /etc/audit/rules.d -p wxa -k auditd
-w /etc/nginx/nginx.conf -p wa -k nginx
-w /etc/nginx/conf.d/default.conf -p wa -k nginx
-w /etc/pam.d -p rwxa -k pam
-w /etc/ssh/sshd_config -p wa -k sshd
```
logsrv:

![rsyslogd_srv](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/img/rsyslog_srv.gif)

web01:

![rsyslogd_client](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/img/rsyslog_client.gif)
```

# Comments
Опции для rsyslogd /etc/sysconfig/rsyslog
В системе запускаются два демона протоколирования - rsyslogd и klogd (для событий ядра)

/etc/audit/auditd.conf - настройки поведения auditd;
/etc/audit/rules.d/audit.rules - правила аудита
autrace - аудит событий, порождаемых указанным процессом (like a strace);
ausearch - поиск событий в журнальных файлах;
aureport - генерирует суммарные отчеты о работе системы аудита;
```
