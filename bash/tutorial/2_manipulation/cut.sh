#!/bin/bash

STRING="word 1 , word 2 , word 3."
TAB_STRING="	word 1,	word 2,	word 3."

# most of the text manipulation commands expect files as input , so instead we
# echo our input string , and use that as an input

# IFS

# cut -b : cuts string by bytes

echo "----------"
echo "cut"
echo "----------"
echo
echo -n "cut -b 3   : "
echo "$STRING" | cut -b 3
echo -n "cut -b 1,3 : "
echo "$STRING" | cut -b 1,3
echo -n "cut -b 1-3 : "
echo "$STRING" | cut -b 1-3
echo -n "cut -b -3  : "
echo "$STRING" | cut -b -3
echo -n "cut -b 3-  : "
echo "$STRING" | cut -b 3-


# cut -c : cuts string by characters

echo
echo -n "cut -c 3   : "
echo "$STRING" | cut -c 3
echo -n "cut -c 1,3 : "
echo "$STRING" | cut -c 1,3
echo -n "cut -c 1-3 : "
echo "$STRING" | cut -c 1-3
echo -n "cut -c -3  : "
echo "$STRING" | cut -c -3
echo -n "cut -c 3-  : "
echo "$STRING" | cut -c 3-

# cut -f : cuts string by 'fields' , which are elements seperated by some
#          delimiter , the default delimiter is tab , to specify some other
#          delimiter use -d flag

# cut -d ',' -f 1-3 filename.txt : will cut first 3 fields seperated by ,
echo
echo -n "cut -f 3        : "
echo "$TAB_STRING" | cut -f 3
echo -n "cut -d ' ' -f 2 : "
echo "$TAB_STRING" | cut -d ' ' -f 2
echo -n "cut -d ',' -f 2 : "
echo "$TAB_STRING" | cut -d ',' -f 2
