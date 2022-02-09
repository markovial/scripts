# !bin/bash

# shell script variables are all by convention in uppercase
# they can contain a-z A-Z 0-9 and _

# variables are defined as follows :

NAME="John Smith"
NUMBER=100

# to access a variable prefix the name with $

echo $NAME

# you can mark variables as readonly by :

echo "-------------------------------------------"

readonly NAME
NAME="Jane Smith"



# the above operation should prompt an error during run time

# to remove a variable from a list of tracked variables use unset command
echo "-------------------------------------------"

unset NAME
echo $NAME

# The following are special variables made aviable by the shell :

echo "-------------------------------------------"

echo "Filename                              : $0 "
echo "First Argument Passed                 : $1 "
echo "Second Argument Passed                : $2 "

echo "All Arguments passed                  : $n "
echo "All Arguments passed                  : $@ "
echo "All Arguments passed                  : $* "

# for most intents and purposes #@ = $* and will have same result

echo "Num Arguments passed                  : $# "
echo "Exit status of last command           : $? "

# exit status 0 = success , 1 = failure (generally speaking)

echo "Process ID                            : $$ "
echo "Process ID of last background command : $! "

# to process command line arguments individually do something like :

echo "-------------------------------------------"

for TOKEN in $*
do
	echo $TOKEN
done

# to read from stdin use the read command , -r is not mandatory but is
# recommended since : -r do not allow backslashes to escape any characters

echo -n "Enter some text : "
IFS= read -r var_name
echo "You entered : $var_name"


