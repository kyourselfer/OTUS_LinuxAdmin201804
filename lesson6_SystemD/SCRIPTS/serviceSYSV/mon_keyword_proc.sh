#!/bin/bash
# This script is following for Logfile and looking for Keyword every 30 seconds.
#
## Function searching Keyword in Logfile 
function fcheck {
    local r=`grep "$1" $2`
    return $?
}
## Return quantity of found rows
function count_check {
    local c=`grep "$1" "$2" | wc -l`
    echo "$c"
}

### It checks number of arguments
if [ $# -ne 3 ]
then
    echo -e "$0: Give me three arguments 1st is Keyword, 2nd is Logfile, 3rd is Interval between checks,\n\n\tExample: $0 \$arg1 \$arg2 \$arg3\n"
    exit 1
fi

# Values
# Arguments
Keyword=$1
Logfile=$2
INTERVALOFCHECK=$3

while true
do
    # find Keyword in Logfile
    fcheck "$Keyword" "$Logfile"
    if [ $? = 0 ]
    then
#        echo "ssh session has detected in $Logfile" #
	# counts rows of event
	# gets 1st number
	count1=`count_check "$Keyword" "$Logfile"`
	sleep $INTERVALOFCHECK
	# gets 2nd number
	count2=`count_check "$Keyword" "$Logfile"`
	# find changes between count1 and count2
	if [[ "$count1" -lt "$count2" ]]
        then
            echo "Somebody has just logged in (ssh session)"
	    echo "Logged at (time is approximately): `date`" >> /var/log/mon_keyword_serviceSysV/security.log
	    continue
	elif [[ "$count1" -gt "$count2" ]]
	then
	    echo "Somewthing is wrong! Count of ssh sessions has become less then before. Check your security logs!"
	    continue
	else
#            echo "Count of ssh sessions is same. Nothing wrong." #
            continue
	fi
    else
	sleep $INTERVALOFCHECK
	continue
    fi
done


