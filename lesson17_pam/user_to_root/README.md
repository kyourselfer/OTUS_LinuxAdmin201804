### Дать конкретному пользователю права рута 

В директории создаем файл /etc/sudoers.d/admin001
```
admin001 ALL=(ALL) NOPASSWD: ALL
```
После этого логин `su -l admin001` в пользователя admin001 и повышения права `sudo -s` пароль не запрашивает.

![rights_of_root](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson17_pam/user_to_root/rights_of_root.gif)
