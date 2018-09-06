2. Из epel установить spawn-fcgi и переписать init-скрипт на unit-файл. Имя сервиса должно так же называться.
---------------------------------------
#####
Правим фаил окружения юнита

/etc/sysconfig/[spawn-fcgi](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson6_SystemD/SCRIPTS/spawn-fcgi/sysconfig_spawn)
```
SOCKET=/var/tmp/php-fcgi.sock
OPTIONS="-u apache -g apache -s /var/tmp/php-fcgi.sock -S -M 0600 -C 6 -P /var/tmp/spawn-fcgi.pid -- /usr/bin/php-cgi"
```

Правим сам юнит c типом "форкирования"

/etc/systemd/system/[spawn-fcgi.service](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson6_SystemD/SCRIPTS/spawn-fcgi/spawn-fcgi.service)
```
[Unit]
Description=Spawns FastCGI processes
After=network.target remote-fs.target nss-lookup.target httpd.service
Requires=httpd.service
Documentation=man:spawn-fcgi(1)

[Service]
Type=forking
PIDFile=/var/tmp/spawn-fcgi.pid
#WorkingDirectory=/var/run/

User=root
Group=apache

EnvironmentFile=/etc/sysconfig/spawn-fcgi
ExecStart=/bin/spawn-fcgi $OPTIONS
ExecStop=/bin/kill -TERM ${MAINPID}
TimeoutStopSec=3s
#ExecReload=/bin/kill -HUP ${MAINPID}
KillMode=control-group
RestartSec=1s

[Install]
WantedBy=multi-user.target
```
Проверяем

![spawn-fcgi](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson6_SystemD/SCRIPTS/spawn-fcgi/spawn-fcgi.gif)
