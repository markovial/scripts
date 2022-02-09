# !/bin/bash
# https://www.tutorialspoint.com/unix/unix-shell-loops.htm


# Types of avaialable loops :
# - for , while , until


echo "WHILE :"

a=0

while [ $a -lt 10 ]
do
   echo $a
   a=`expr $a + 1`
done

echo "FOR :"

# for over specific elements

for i in 1 2 3 4 5
do
   echo "Welcome $i times"
done

# Over larger ranges

for i in {1..5}
do
   echo "Welcome $i times"
done

# over ranges , with increment specifications

# Bash v4.0+ has inbuilt support for setting up a step value using
# {START..END..INCREMENT} 

echo "Bash version ${BASH_VERSION}..."
for i in {0..10..2}
  do 
     echo "Welcome $i times"
 done

for FILE in $HOME/.bash*
do
   echo $FILE
done

echo "UNTIL "

a=10

# following is infinite loop


#until [ $a -lt 10 ]
#do
#   echo $a
#   a=`expr $a + 1`
#done


# breaking

a=0

while [ $a -lt 10 ]
do
   echo $a
   if [ $a -eq 5 ]
   then
      break
   fi
   a=`expr $a + 1`
done


# breaking from nested loops : break n
# Here n specifies the nth enclosing loop to the exit from.

for var1 in 1 2 3
do
   for var2 in 0 5
   do
      if [ $var1 -eq 2 -a $var2 -eq 0 ]
      then
         break 2
      else
         echo "$var1 $var2"
      fi
   done
done

# loop over array
readarray MY_ARRAY
LENGTH=${#MY_ARRAY[@]}

#initialize array
for (( i=0; i<$LENGTH; i++ ))
do
    echo -n "${MY_ARRAY[i]}"
done
