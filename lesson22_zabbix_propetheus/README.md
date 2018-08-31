Цели занятия:
-------
Изучаем Zabbix. Знакомимся с Prometheus
### Д.З.:
Настройка мониторинга
Настроить дашборд с 4-мя графиками
1) память
2) процессор
3) диск
4) сеть

настроить на одной из систем
- zabbix (использовать screen (комплексный экран))
- prometheus - grafana

* использование систем примеры которых не рассматривались на занятии
- список возможных систем был приведен в презентации

в качестве результата прислать скриншот экрана - дашборд должен содержать в названии имя приславшего
### Execution:
`/usr/local/bin/prometheus --config.file=/etc/prometheus/prometheus.yml --storage.tsdb.path=/var/lib/prometheus --log.level=debug`

### PrintScreens of avidence:
Grafana

![Grafana](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson22_zabbix_propetheus/grafana.gif)