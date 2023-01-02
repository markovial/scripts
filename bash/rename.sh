#!/bin/bash

#FOLDER="$HOME/Documents/personal/Profiles/"
for i in $( ls );
do

	# change extensions
	$i $i.sh;

	#remove extensions
#	mv $i ${i%.*};
done

