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

* настроить доп опции - сжатия, шифрования, дедупликация

Bacula поставляется (CentOS|Fedora) по умолчанию с настройкой на postgresql elf-файлом(библиотекой) для коннекта с `Catalog` нам необходимо изменить если хотим использовать `mysql`

Вырезка из /etc/bacula/[bacula-dir.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson23_bacula/bacula/bacula-dir.conf)
``
Catalog {
        Name = bacula
        dbname = "bacula"; dbuser = "rootadmin"; dbpassword = "pass"
}
``

```
[root@bacula]# su -c 'alternatives --config libbaccats.so'

There are 3 programs which provide 'libbaccats.so'.

  Selection    Command
-----------------------------------------------
 + 1           /usr/lib64/libbaccats-mysql.so
   2           /usr/lib64/libbaccats-sqlite3.so
*  3           /usr/lib64/libbaccats-postgresql.so

Enter to keep the current selection[+], or type selection number: 1
```
##### Configs
```
/etc/bacula/
├── bacula-dir.conf
├── bacula-fd.conf
├── bacula-sd.conf
├── bconsole.conf
├── clients
│   ├── web01-fd.conf
│   └── web02-fd.conf
└── query.sql
```
[bacula-dir.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson23_bacula/bacula/bacula-dir.conf)

[bacula-fd.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson23_bacula/bacula/bacula-fd.conf)

[bacula-sd.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson23_bacula/bacula/bacula-sd.conf)

[bconsole.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson23_bacula/bacula/bconsole.conf)

clients/[web01-fd.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson23_bacula/bacula/clients/web01-fd.conf)

clients/[web02-fd.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson23_bacula/bacula/clients/web02-fd.conf)

`list jobs`

![jobs list](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson23_bacula/list_jobs.gif)

[list files jobid=84](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson23_bacula/jobid84.out) (Full)

[list files jobid=85](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson23_bacula/jobid84.out) (Full)


##### troubleshooting
#options of daemon /etc/sysconfig/bacula-dir
`OPTS="-d 200"`

bacula-dir -tc /etc/bacula/bacula-dir.conf

#default settings in /usr/libexec/bacula/bacula_config
#scripts of DB /usr/libexec/bacula
