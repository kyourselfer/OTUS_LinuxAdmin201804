#!/bin/sh
# Перечисляем все не ществующие цели ботов
req1="libraries/import.core.php|mail.php|jcache.php|templates/jblank/start.php|/libraries/e5nbwvcxef.php|/libraries/joomla/client/file.php|/libraries/kunena/activity/utf.php|upgysncy.php|pdjsizui.php | awk -F"/" '{ print $6 }'"
#
cd /home/kisl/RUN/
# Запишем найденые ip
find /usr/local/www/apache24/ -type f -name 'access.log' | xargs egrep -i "$req1" > find_access2_email.tmp
numIp=`cat find_access2_email.tmp | wc -l`
# Выведем найденые ip
echo "Found ip: $numIp"
for i in `seq 1 \$numIp`
do
    site1=`cat find_access2_email.tmp | awk NR=="$i" | awk -F"/" '{ print $6 }'`
    ip1=`cat find_access2_email.tmp | awk NR=="$i" | awk -F":" '{ print $2 }' | cut -f 1 -d  - -s`
    url1=`cat find_access2_email.tmp | awk NR=="$i" | awk -F" " '{ print $7 }'`
    code1=`cat find_access2_email.tmp | awk NR=="$i" | awk -F" " '{ print $9 }'`
    echo -e "$site1 \t $ip1 \t $url1 \t $code1"
done
# Добавляем ip в базу PacketFilter_BSD
cat /home/kisl/RUN/find_access2_email.tmp | awk -F ":" '{print $2}' | cut -f 1 -d - -s | sort | uniq >> /etc/pfBotsDB
cat /etc/pfBotsDB | sort | uniq > /etc/pfBotsDB.uniq
cat /etc/pfBotsDB.uniq >> /etc/pfBotsDB
pfctl -vf /etc/pf.conf
pfctl -T show -t badhosts | wc -l
exit 0


