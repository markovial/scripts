#!/bin/bash
# https://superuser.com/questions/611538/is-there-a-way-to-display-a-countdown-or-stopwatch-timer-in-a-terminal

# Countdown from seconds taken as commandline arg

# m flag is for minutes , s is for seconds , s is default case
FLAG="$1"
SECONDS="$2";
if [ $FLAG == "-m" ]
then
	SECONDS=$((SECONDS*60))
elif [ $FLAG == "-h" ]
then
	echo "-m is for mins , -s is for secs , -h is for help"
	echo "secs is default"
fi


DATE_VAR=$((`date +%s` + $SECONDS)); 
while [ "$DATE_VAR" -ge `date +%s` ]; do 
	echo -ne "$(date -u --date @$(($DATE_VAR - `date +%s` )) +%H:%M:%S)\r"; 
done

#countdown(){
    #date1=$((`date +%s` + $1));
    #while [ "$date1" -ge `date +%s` ]; do 
    ### Is this more than 24h away?
    #days=$(($(($(( $date1 - $(date +%s))) * 1 ))/86400))
    #echo -ne "$days day(s) and $(date -u --date @$(($date1 - `date +%s`)) +%H:%M:%S)\r"; 
    #sleep 0.1
    #done
#}

#stopwatch(){
    #date1=`date +%s`; 
    #while true; do 
    #days=$(( $(($(date +%s) - date1)) / 86400 ))
    #echo -ne "$days day(s) and $(date -u --date @$((`date +%s` - $date1)) +%H:%M:%S)\r";
    #sleep 0.1
    #done
#}
