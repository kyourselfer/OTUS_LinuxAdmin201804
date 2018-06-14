ДЗ. 1. Написать сервис, который будет раз в 30 секунд мониторить лог на предмет наличия ключевого слова. Файл и слово должны задаваться в /etc/sysconfig
-------------------------------
##### Сервис SYSV формата `mon_keyword_serviceSysV`:
* [mon_keyword_proc.sh](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson6_SystemD/SCRIPTS/serviceSYSV/mon_keyword_proc.sh) # Процесс принимает 3 аргумента `ключевую фразу`, `файл лога для поиска`, `интервал проверки`. Набюдает за изменением числа строк в файле лога. В случае сработки условия пишет в `/var/log/mon_keyword_serviceSysV/security.log` и `/var/log/messeges`;
* mon_keyword_serviceSysV # Файл сервиса SYSV передающий три агрумента в `/etc/sysconfig/mon_keyword_serviceSysV.conf` пишет файл лога запуска и остановки `/var/log/mon_keyword_serviceSysV/daemon.log`;
* mon_keyword_serviceSysV.conf # Конфигурационный файл.
