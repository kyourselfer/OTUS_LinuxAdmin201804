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
	# check quantity of arguments
	if [ $# -ne 1 ]
	then
		    echo -e "$0: Enter name of the process which you would like to follow!\n\n\tExample: $0 \$arg1\n"
		        exit 1
		fi
		#
		# VALUES
		cPID=/tmp/$(basename $0).pid
		lPID=/tmp/$(basename $0).lock
		email='kyourselfer@ya.ru'
		#
		# catching Psignals
		trap 'rm -f $cPID; echo "$cPID has removed"' EXIT
		trap 'echo "$0 is closing ..."; exit 3' 15
		trap -- 1 3 17 18
		#
		# find pidfile
		if [ -e $cPID ]
		then
			    echo -e "Process can not start. It's existed already."
			        exit 2
			fi
			#
			# create pidfile and lockfile
			echo $$ > $cPID
			flock -w $lPID ...........................sh
			echo "$cPID has created and blocked"
			#
			proc=$1
			#
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

