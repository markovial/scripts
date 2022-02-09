# !/bin/bash
# https://www.tutorialspoint.com/unix/unix-decision-making.htm

# Number Comparison
a=10
b=20
c=30
if [ $a == $b ]
then
   echo "a is equal to b"
elif [ $a -gt $b ]
then
   echo "a is greater than b"
elif [ $a -lt $b ]
then
   echo "a is less than b"
else
   echo "None of the condition met"
fi

# Switch Case Comparison

FRUIT="kiwi"

case "$FRUIT" in
   "apple") echo "Apple pie is quite tasty."
   ;;
   "banana") echo "I like banana nut bread."
   ;;
   "kiwi") echo "New Zealand is famous for kiwi."
   ;;
esac


# Logicial conditionals in addition to if statements
if [ $a == $b ] && [ $b == $c ]
then
    echo "EQUILATERAL"
elif [ $a == $b ] || [ $b == $c ] || [ $a == $c ]
then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi




# evaluation of command line args example use case
option="${1}"
case ${option} in
   -f) FILE="${2}"
      echo "File name is $FILE"
      ;;
   -d) DIR="${2}"
      echo "Dir name is $DIR"
      ;;
   *)
      echo "`basename ${0}`:usage: [-f file] | [-d directory]"
      exit 1 # Command to come out of the program with status 1
      ;;
esac


