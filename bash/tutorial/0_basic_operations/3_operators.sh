# !/bin/bash.sh
# https://www.tutorialspoint.com/unix/unix-basic-operators.htm
# types of available operators :

# Arithmetic , Relational , Boolean , String , File Test
echo "" 
echo "-------------------------------------------"
echo "ARITHMETIC" 
echo "-------------------------------------------"
echo "" 

# keep in mind :

# there must be spaces between operators and expressions
# the expression to be evaluated should be between backticks : ``

a=10
b=20

echo " a=$a , b=$b "

echo " Addition       : +  : $a + $b = `expr $a + $b` "
echo " Subtraction    : -  : $a - $b = `expr $a - $b` "
echo " Multiplication : *  : $a * $b = `expr $a \* $b` "
echo " Division       : /  : $b / $a = `expr $b / $a` "
echo " Modulus        : %  : $b % $a = `expr $b % $a` "
echo " Assignment     : =  : $a = $b"
echo " Equality       : == : $a == $b"
echo " Not Equality   : != : $a != $b"
# all the conditional expressions should be inside square braces with spaces
# around them, for example [ $a == $b ] is correct whereas, [$a==$b] is
# incorrect.

# when using with variables instead of using backticks like above , we can also
# use $(())

echo
echo " using \$(()) "
echo
echo " Addition       : +  : $a + $b = $(($a + $b)) "
echo " Subtraction    : -  : $a - $b = $(($a - $b)) "



echo "" 
echo "-------------------------------------------"
echo "RELATIONAL" 
echo "-------------------------------------------"
echo "" 

RESULT=""

if [ $a -eq $b ] ; then RESULT="true" ; else RESULT="false" ; fi
echo " Equality              : -eq : $a -eq $b : $RESULT"

if [ $a -ne $b ] ; then RESULT="true" ; else RESULT="false" ; fi
echo " Not Equality          : -ne : $a -ne $b : $RESULT"

if [ $a -gt $b ] ; then RESULT="true" ; else RESULT="false" ; fi
echo " Greater Than          : -gt : $a -gt $b : $RESULT"

if [ $a -lt $b ] ; then RESULT="true" ; else RESULT="false" ; fi
echo " Less Than             : -lt : $a -lt $b : $RESULT"

if [ $a -ge $b ] ; then RESULT="true" ; else RESULT="false" ; fi
echo " Greater Than or Equal : -ge : $a -ge $b : $RESULT"

if [ $a -le $b ] ; then RESULT="true" ; else RESULT="false" ; fi
echo " Less Than or Equal    : -le : $a -le $b : $RESULT"


echo ""
echo "-------------------------------------------"
echo "BOOLEAN"
echo "-------------------------------------------"
echo ""


echo "Logical Negation : ! "
echo "Logical OR       : -o "
echo "Logical AND      : -a "

if [ $a != $b ]
then
   echo "$a != $b : a is not equal to b"
else
   echo "$a != $b: a is equal to b"
fi

if [ $a -lt 100 -a $b -gt 15 ]
then
   echo "$a -lt 100 -a $b -gt 15 : returns true"
else
   echo "$a -lt 100 -a $b -gt 15 : returns false"
fi

if [ $a -lt 100 -o $b -gt 100 ]
then
   echo "$a -lt 100 -o $b -gt 100 : returns true"
else
   echo "$a -lt 100 -o $b -gt 100 : returns false"
fi

if [ $a -lt 5 -o $b -gt 100 ]
then
   echo "$a -lt 100 -o $b -gt 100 : returns true"
else
   echo "$a -lt 100 -o $b -gt 100 : returns false"
fi

echo ""
echo "-------------------------------------------"
echo "STRING"
echo "-------------------------------------------"
echo ""


a=foo
b=bar

echo " a = $a , b = $b "

if [ $a = $b ] ; then RESULT="true" ; else RESULT="false" ; fi
echo " Equality           : =   : $a = $b : $RESULT"

if [ $a != $b ] ; then RESULT="true" ; else RESULT="false" ; fi
echo " Non Equality       : !=  : $a != $b : $RESULT"

if [ -z $a ] ; then RESULT="a is len 0" ; else RESULT="a is non 0 len" ; fi
echo " Zero Length        : -z  : -z $a : $RESULT"

if [ -n $a ] ; then RESULT="a is non len 0" ; else RESULT="a is 0 len" ; fi
echo " Non Zero Length    : -n  : -n $a : $RESULT"

if [ $a ] ; then RESULT="true" ; else RESULT="false" ; fi
echo " Empty String Check : str : $a : $RESULT"

echo ""
echo "-------------------------------------------"
echo "FILE TEST"
echo "-------------------------------------------"
echo ""

echo "Check if file is Block Special               : -b  "
echo "Check if file is Character Special           : -c  "
echo "Check if file is directory                   : -d  "
echo "Check if file is ordinary                    : -f  "
echo "Check if file has set group ID               : -g  "
echo "Check if file has set sticky bit             : -k  "
echo "Check if file is a named pipe                : -p  "
echo "Check if file descriptor is open in terminal : -t  "
echo "Check if file has set user ID (UID)          : -u  "
echo "Check if file is readable                    : -r  "
echo "Check if file is writable                    : -w  "
echo "Check if file is executable                  : -x  "
echo "Check if file has size > 0                   : -s  "
echo "Check if file exists                         : -e  "




