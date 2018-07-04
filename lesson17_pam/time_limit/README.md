### Запретить всем пользователям, кроме группы admin логин в выходные и праздничные дни


В стеке /etc/pam.d/sshd делаем изменения (меняем список пользователей которым разрешен доступ при помощи скрипта /usr/local/sbin/[loginANDsshdUsers](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson17_pam/time_limit/loginANDsshdUsers))
```
auth       requisite     pam_listfile.so onerr=fail item=user sense=allow file=/etc/loginANDsshdUsers
```
Запускаем скрипт по крону (в дальнейшем преобразуем в systemd unit) в субботу с аргументов запрета логин для всех пользователей исключая группу "admin", и в понидельник без аргументов для отключения запрета на вход



#### Tips
##### Для лимитирования доступа по времени и дням нидели

/etc/pam.d/login|sshd

`account    requisite    pam_time.so`

/etc/security/time.conf
```
# сервису login или sshd через все терминалы для всех пользователей исключая admin001
# разрешить доступ исключая SaterdaySunday с 00:00-24:00 (admin001 разрешено логиниться в любое время)
login|sshd;*;!admin001;!SaSu0000-2400
```
##### Для проверки по условию

/etc/pam.d/login|sshd
```
auth       required     pam_succeed_if.so debug user ingroup admin
```

