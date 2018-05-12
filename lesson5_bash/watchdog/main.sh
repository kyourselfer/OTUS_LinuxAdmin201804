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
		#
		# catching Psignals
		trap 'rm -f $cPID; echo "$cPID has removed"' EXIT
		trap ' echo "$0 is closing ..." ; exit 3 ' 15
		#
		# find pidfile
		if [ -e $cPID ]
		then
			    echo "script can not start untill $cPID is existed, it has just deleted and everething is OK"
			        exit 2
			fi
			#
			# create pidfile
			echo $$ > $cPID
			echo "$cPID has created"
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
								    echo "script can not start untill $cPID is existed, it has just deleted and everething is OK"
								        exit 2
								fi
								#
								# create pidfile
								echo $$ > $cPID
								echo "$cPID has created"
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
													        `systemctl start $proc`
														    fi
													    done

