Настраиваем бэкап (Bacula)
------------
Настроить политику бэкапа каталога /etc с обоих клиентов
1) полный раз в день
2) инкремент каждые 10 минут
3) дифференциал каждые полчаса

запустить систему на 2 часа
для сдачи ДЗ приложить
list jobs
list files jobid=<idfullbackup>
и настроенный конфиг

* настроить доп опции - сжатия, шифрования, дедупликация</idfullbackup>

# troubleshooting
/etc/sysconfig/bacula-dir
`OPTS="-d 200"`

bacula-dir -tc /etc/bacula/bacula-dir.conf

