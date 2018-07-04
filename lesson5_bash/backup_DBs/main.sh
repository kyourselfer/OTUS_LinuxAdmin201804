#
# Checked on FreeBSD
#
#!/bin/bash
DATA=`date +%Y.%m.%d--%H`
#
TAR=/usr/bin/tar
PIGZ=/usr/local/bin/pigz
#
LABELARH=mysql
DIRECTORIES="ram1/mysqlFull"
#
msqld=/usr/local/bin/mysqldump
msql=/usr/local/bin/mysql
#
# Время старта 
sttime=`date +%H:%M:%S`
#
# Общая блокировка на запись
$msql -u root -p`cat ~/.pwd` <<EOF
FLUSH TABLES WITH READ LOCK;
SET GLOBAL read_only = ON;
exit
EOF
# Дампим
myp=`cat ~/.pwd`
cd /
for VAL in `$msql -u root -p$myp -B -e 'show databases;' | grep -v 'Database\|information_schema\|performance_schema\|phpmyadmin\|plugin'`
do
    echo $VAL
    $msqld -u root -p$myp -f $VAL > $DIRECTORIES/$VAL.sql
done
# Разблокировка баз
$msql -u root -p`cat ~/.pwd` <<EOF
SET GLOBAL read_only = OFF;
UNLOCK TABLES;
exit
EOF
# Сжатие многопоточное
$TAR -cf - $DIRECTORIES | $PIGZ -9 -p 10 > /usr/home/kisl/REZERV/send/$LABELARH-$DATA.tar.gz
#
# Время окончания сжатия 
curtime=`date +%H:%M:%S`
#
echo `$0 $sttime $curtime`
#
# Отправляем в облако через webdav клиент
/usr/local/bin/cadaver -t <<EOF
open https://5i5i.ru/owncloud/remote.php/webdav
cd mysqlWebServer
put /usr/home/kisl/REZERV/send/$LABELARH-$DATA.tar.gz
quit
EOF
# Чистим за собой
rm /usr/home/kisl/REZERV/send/$LABELARH-$DATA.tar.gz
rm $DIRECTORIES/*.sql


