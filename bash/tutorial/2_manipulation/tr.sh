
# tr : the translate command changes one character to another
# remember this does not translate strings , it changes chars

# tr -d : delete strings or character blocks
# tr -s : compress multiple chracters into 1

echo "----------"
echo "tr"
echo "----------"
echo -n "tr \"e\" \"E\"  : "
echo "Hello" | tr "e" "E"
echo -n "tr -d \"e\"   : "
echo "Hello" | tr -d "e"
echo -n "tr -d [a-z] : "
echo "Hello" | tr -d [a-z]
echo -n "tr -s \" \"   : "
echo "He      llo" | tr -s " "
echo -n "tr -s \"l\"   : "
echo "Hello" | tr -s "l"
