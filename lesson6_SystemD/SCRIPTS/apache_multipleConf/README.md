3. Дополнить юнит-файл apache httpd возможностьб запустить несколько инстансов сервера с разными конфигами
---------------------------------------
#####
Создадим unit для запуска по шаблону используя подстановку %i и %I [Specifiers](https://www.freedesktop.org/software/systemd/man/systemd.unit.html#Specifiers) /etc/systemd/system/[httpd@.service]()

Создаем конфиг на каждый экземпляр(instance)
/etc/httpd/conf/[httpd_site1.conf]()

Добавим в конфиг доп для одновременной работу
PidFile /var/run/httpd/httpd_site1.pid
