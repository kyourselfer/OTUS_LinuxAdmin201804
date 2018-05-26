#!/bin/bash
#
# This script is following for Logfile and looking for Keyword every 30 seconds.
#
## Function searching Keyword in Logfile 
function fcheck {
    r=`grep "$1" $2`
    return $?
}

### It checks quantity of arguments | Проверка на кол-во аргументов
if [ $# -ne 2 ]
then
    echo -e "$0: Give me two arguments 1st is Keyword and 2nd is Logfile,\n\n\tExample: $0 \$arg1 \$arg2\n"
    exit 1
fi

# Values
Keyword=$1
Logfile=$2
#
while true
do
    sleep 3
    fcheck "$Keyword" "$Logfile"
    if [ $? = 0 ]
    then
        echo "Event has come!"
        exit 0
    else
        echo "Event hasn\'t come yet!"
	continue
    fi
done

