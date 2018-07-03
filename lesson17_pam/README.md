Домашнее задание
---------------------
### PAM
1. [Запретить всем пользователям, кроме группы admin логин в выходные и праздничные дни]()
/etc/security/time.conf
login|sshd;*;!admin001|!root;!SaSu0000-2400
/etc/pam.d/login
account    requisite    pam_time.so
2. [Дать конкретному пользователю права рута]()
