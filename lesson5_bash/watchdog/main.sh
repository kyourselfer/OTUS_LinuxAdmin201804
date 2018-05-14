#!/bin/bash
#
### watchdog ###
#
# Function searching over list of processes | Поиск $arg1 среди процессов
function fcheck {
    r=`ps -eo pid,comm|grep $proc`
    return $?
}
#
#
##### It checks quantity of arguments | Проверка на кол-во аргументов
if [ $# -ne 2 ]
then
    echo -e "$0: Enter name of the process as ARG1 and your email as ARG2,\nwhich you would like to follow!\n\n\tExample: $0 \$arg1 \$arg2\n"
    exit 1
fi
#
# Values | Значения
cPID=/tmp/$(basename $0).pid
email=$2
proc=$1
#
##### Check pidfile | Проверка на существования pidfile
if [ -e $cPID ]
then
    echo "Process can not start. It's run already."
    exit 0
else
    echo $$ > $cPID
    echo "$cPID has created"
fi
#
# It catches PSignals | Ловим сигналы завершения процесса
trap 'rm -f $cPID; echo "$cPID has removed"' EXIT
trap 'echo "$0 is closing ..."; exit 3' 15
trap -- 1 3 17 18
#
##### It follows to $arg1 if stop then mailing to $arg2 | Следим за процессом $arg1 если исчезает отправляем оповещение на почту $arg2 и запускаем
fcheck
while [ $? = 0 ]
do
    sleep 5
    fcheck
    if [ $? = 1 ]
    then
        clogs=`journalctl -n 5 -u $proc`
        cinfo=`uptime | awk -Fe: '{print "avg:" $2}'; date; echo $clogs`
        `echo $cinfo | mail -s "$proc was restarted" $email`
	`systemctl start $proc`
    fi
done


