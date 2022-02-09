# !/bin/bash



# -e option enables the interpretation of backslash escapes.

echo "CHARACTER SUBSTITUTION"

echo -e " Backslash : \\ "
echo -e " Alert : \a "
echo -e " Backspace : i\b "
echo -e " Suppress Newline : \c "
echo " This is another line POG "
echo -e " Form Feed : \f "
echo -e " Add Newline : \n "
echo -e " Carriage Return : \r "
echo -e " Horizontal Tab  : \t "
echo -e " Vertical Tab : \v "


echo "COMMAND SUBSTITUTION"
# The command substitution is performed when a command is given as −
# `command`


DATE=`date`
echo "Date is $DATE"

USERS=`who | wc -l`
echo "Logged in user are $USERS"

UP=`date ; uptime`
echo "Uptime is $UP"

echo -e "\n\n"
# ${var} : Substitute the value of var.
# ${var:=word} : If var is null or unset, var is set to the value of word.
# ${var:?message} If var is null or unset, message is printed to standard error. This checks that variables are set correctly.

echo ${var:-"Variable is not set"}
echo "1 - Value of var is ${var}"

echo ${var:="Variable is not set"}
echo "2 - Value of var is ${var}"

unset var
echo ${var:+"This is default value"}
echo "3 - Value of var is $var"

var="Prefix"
echo ${var:+"This is default value"}
echo "4 - Value of var is $var"

echo ${var:?"Print this message"}
echo "5 - Value of var is ${var}"

