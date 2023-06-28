#!/bin/bash

# uncomment lines if you want to pass wallpaper and speed as args

#[ "$#" -lt "1" ] || [ "$#" -gt "2" ] && {  echo -e "ERROR : args number invalid \n $0 speed /path/name.gif" ; echo "try 0.010 as speed" ; exit 1 ; }
dir=/tmp/back4  
speed=$1
image_format=$2
name=$3

#speed=0.01
#name=~/Images/gif/watching_checkpoint_bw.gif
#image_format=--bg-scale

[[ "$name" == "" ]] && { name=$speed ; speed=${name##*-} ; }

hash=`md5sum $name | cut -f1 -d" "`

[[ ! -d $dir ]] && mkdir $dir 

[[ ! -d $dir/$hash ]] && { mkdir $dir/$hash ; echo "spliting .." ; convert -coalesce $name $dir/$hash/$hash.png ; echo ok ; }

while : ; do for i in ` ls $dir/$hash -v ` ; do feh $image_format $dir/$hash/$i ; sleep $speed ; done ; done 

