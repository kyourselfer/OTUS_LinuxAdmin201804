### Настраиваем центральный сервер для сбора логов rsyslog
--------
##### rsyslog
![rsyslogd](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/img/rsyslogd.gif)

Роль [rsyslogSrv](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/rsyslogSrv/tasks/main.yml)

Заменяем конфиг /etc/[rsyslog.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/rsyslogSrv/files/server_rsyslog.conf)

Добавляем /etc/rsyslog.d/[nginx_logs.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/rsyslogSrv/files/server_rsyslog_nginx.conf) (принимаем сообщения по шаблону и складываем в директорию /var/log/remote/$ip)

Роль [rsyslogClient](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/rsyslogClient/tasks/main.yml)

Добавляем конфиг для отправки критических событий на сервер и локально
/etc/rsyslog.d/[crit.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/rsyslogClient/files/crit.conf)

Заменяем конфиг для клиента /etc/[rsyslog.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/rsyslogClient/files/client_rsyslog.conf)

Роль [nginx](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/nginx/tasks/main.yml)

#Следим за файлами логов nginx и отправляем от оборудывания(Facility) используя local6(на стороне клиента) и важности(Facility) на сервер логов logsrv

Добавляем конфиг для отправки событий
/etc/rsyslog.d/[nginx.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/nginx/files/nginx_syslog.conf)
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
```
Опции для rsyslogd /etc/sysconfig/rsyslog
В системе запускаются два демона протоколирования - rsyslogd и klogd (для событий ядра)
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
