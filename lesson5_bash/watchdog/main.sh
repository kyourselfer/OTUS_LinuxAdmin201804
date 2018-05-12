#!/bin/bash
#
### watchdog to nginx ###
#
#
function fcheck {
	    r=`ps -eo pid,comm|grep $proc`
	        return $?
	}
	#
	#
	# VALUES
	cPID=/tmp/$(basename $0).pid
	#
	# VALUES
	trap 'rm -f $cPID; ' EXIT
	trap ' echo "$0 is closing ..." ; exit 3 ' 15
	#
	# find pidfile
	if [ -e $cPID ]
	then
		    echo "script can not start untill $CPID is existed"
		        exit 2
		fi
		#
		# create pidfile
		echo $$ > $cPID
		echo "$cPID has created"
		#
		proc=nginx
		result1=`ps -eo pid,comm|grep $proc`
		#
		printf(fcheck)
		p1=$?
		echo "p1 = $p1"
		echo "p1 = $p1"
		while [ $p1 = 0 ]
		do
			    echo "while p1 = $p1"
			        echo "NGINX is here!"
				    sleep 5
				        
				        if [ 1 = 0 ]
						    then
							            break
								            exit 1
									        fi
									done

