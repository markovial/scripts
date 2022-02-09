
# head : shows first 10 characters of file

# head [filename]
# head -n 11 [filename]  -> First 11 lines
# head -c 20 [filename]  -> First 20 characters

echo "----------"
echo "head"
echo "----------"
echo
echo -n "head      : "
echo "$STRING" | head
echo -n "head -n 5 : "
echo "$STRING" | head -n 5
echo -n "head -c 7 : "
echo "$STRING" | head -c 7

# tail : shows last 10 characters of file
echo
echo "----------"
echo "tail"
echo "----------"
echo

echo -n "tail      : "
echo "$STRING" | tail
echo -n "tail -n 5 : "
echo "$STRING" | tail -n 5
echo -n "tail -c 7 : "
echo "$STRING" | tail -c 7
