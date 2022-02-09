#!/bin/bash

# dont do things like the following , use arrays

NAME01="Zara"
NAME02="Qadir"
NAME03="Mahnaz"
NAME04="Ayan"
NAME05="Daisy"

# initialization 
# bash shell : array_name=(value1 ... valuen)
# ksh shell : set -A array_name value1 value2 ... valuen

NAME[0]="Zara"
NAME[1]="Qadir"
NAME[2]="Mahnaz"
NAME[3]="Ayan"
NAME[4]="Daisy"


# Accessing values : ${array_name[index]}

echo "First Index: ${NAME[0]}"
echo "Second Index: ${NAME[1]}"

# access all items for loops and such with : ${array_name[*]}
#                                            ${array_name[@]}

# initialize array of 100 elements
declare -a MY_ARRAY=( $(for i in {1..100}; do echo 0; done) )

# read input as array from stdin , seperated by newline
#readarray MY_ARRAY
#LENGTH=${#MY_ARRAY[@]}

#initialize array
#for (( i=0; i<$LENGTH; i++ ))
#do
#    echo -n "${MY_ARRAY[i]}"
#done

# read array inputted seperated by specified delimiter
#readarray -d "," myarr


# length of nth element in array
Unix[0]='Debian'
Unix[1]='Red hat'
Unix[2]='Ubuntu'
Unix[3]='Suse'

echo ${#Unix[3]} # length of the element located at index 3 i.e Suse


# extract 2 elements starting from position 3
Unix=('Debian' 'Red hat' 'Ubuntu' 'Suse' 'Fedora' 'UTS' 'OpenLinux');
echo ${Unix[@]:3:2}

# Extract the first 4 elements of the 1st element in an array
Unix=('Debian' 'Red hat' 'Ubuntu' 'Suse' 'Fedora' 'UTS' 'OpenLinux');
echo ${Unix[2]:0:4}

# Search and replace in an array
Unix=('Debian' 'Red hat' 'Ubuntu' 'Suse' 'Fedora' 'UTS' 'OpenLinux');

echo ${Unix[@]/Ubuntu/SCO Unix}

# add element to existing array
Unix=('Debian' 'Red hat' 'Ubuntu' 'Suse' 'Fedora' 'UTS' 'OpenLinux');
Unix=("${Unix[@]}" "AIX" "HP-UX")
echo ${Unix[7]}

# remove elements from existing array
Unix=('Debian' 'Red hat' 'Ubuntu' 'Suse' 'Fedora' 'UTS' 'OpenLinux');

unset Unix[3]

# remove an element based on pattern match
declare -a Unix=('Debian' 'Red hat' 'Ubuntu' 'Suse' 'Fedora');
declare -a patter=( ${Unix[@]/Red*/} )
echo ${patter[@]}

# copy an array into another array
Unix=('Debian' 'Red hat' 'Ubuntu' 'Suse' 'Fedora' 'UTS' 'OpenLinux');
Linux=("${Unix[@]}")
echo ${Linux[@]}

# concatenate two arrays
Unix=('Debian' 'Red hat' 'Ubuntu' 'Suse' 'Fedora' 'UTS' 'OpenLinux');
Shell=('bash' 'csh' 'jsh' 'rsh' 'ksh' 'rc' 'tcsh');

UnixShell=("${Unix[@]}" "${Shell[@]}")
echo ${UnixShell[@]}
echo ${#UnixShell[@]}

# delete an entire array
Unix=('Debian' 'Red hat' 'Ubuntu' 'Suse' 'Fedora' 'UTS' 'OpenLinux');
Shell=('bash' 'csh' 'jsh' 'rsh' 'ksh' 'rc' 'tcsh');

UnixShell=("${Unix[@]}" "${Shell[@]}")
unset UnixShell
echo ${#UnixShell[@]}

# read file content into array
filecontent=( `cat "logfile" `)

for t in "${filecontent[@]}"
do
echo $t
done
echo "Read file content!"
