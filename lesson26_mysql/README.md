#### Д.З.
Развернуть базу из дампа и настроить для нее реплику
В материалах приложены ссылки на вагрант для репликации
и дамп базы bet.dmp
базу развернуть на мастере
и настроить чтобы реплицировались таблицы
| bookmaker |
| competition |
| market |
| odds |
| outcome

* Настроить GTID репликацию

варианты которые принимаются к сдаче
- рабочий вагрантафайл
- скрины или логи SHOW TABLES
* конфиги
* пример в логе изменения строки и появления строки на реплике

#### Решение

Берем готовый Vagrantfile от автора chrisleekr по созданию [MySQLServer5.5 связки Master-Slave](https://github.com/chrisleekr/vagrant-mysql-master-slave-replication) и правим под соответствие ДЗ.

* master
./[bootsrap-master.sh](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson26_mysql/bootstrap-master.sh)

conf.d/[my_override.cnf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson26_mysql/config/master/my-master.cnf)
```
server-id              	= 1
log_bin            		= /var/log/mysql/mysql-bin.log
binlog_do_db			= bet
#replicate-wild-do-table         = bet.%
replicate-ignore-table          = bet.events_on_demand
replicate-ignore-table          = bet.v_same_event
datadir  				= /var/lib/mysql_vagrant
```
* slave
./[bootstrap-slave.sh](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson26_mysql/bootstrap-slave.sh)

conf.d/[my_override.cnf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson26_mysql/config/slave/my-slave.cnf)
```
server-id              	= 2
log_bin            		= /var/log/mysql/mysql-bin.log
binlog_do_db			= bet
#replicate-wild-do-table         = bet.%
replicate-ignore-table          = bet.events_on_demand
replicate-ignore-table          = bet.v_same_event
```

* Добавляем на Master стоки и изменяем, и наблюдаем реплику в binlog `mysql -e "USE bet; SHOW TABLES; SELECT * FROM bookmaker; INSERT INTO bookmaker VALUES(13,'StRiNg13'); UPDATE bookmaker SET bookmaker_name='StRiNg14' WHERE bookmaker_name='StRiNg13'; SELECT * FROM bookmaker;" && tail /var/log/mysql/mysql-bin.000002`
![replica_binlog](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson26_mysql/replica_binlog.gif)
