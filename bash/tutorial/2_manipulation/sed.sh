#!/bin/bash

echo "----------"
echo "sed"
echo "----------"

# find and replace a pattern
# https://www.grymoire.com/Unix/Sed.html#uh-10a

# sed by default only changes the first occurance of a pattern per line


echo day | sed s/day/night/
echo Sunday | sed 's/day/night/'

# sed 's/p1/p2/' file.txt   : subtitute the first occurances of p1 with p2
# sed 's/p1/p2/g' file.txt : subtitute all occurances of p1 with p2
# sed 's/p1/p2/I' file.txt : subtitute first occurance of p1 with p2


# sed -n
# sed -v
# sed -i
