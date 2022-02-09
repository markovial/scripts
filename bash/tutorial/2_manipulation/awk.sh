
echo "----------"
echo "awk"
echo "----------"

# awk manipulates text data and generates formatted reports


# awk '/p1/ {Actions} /p2/ {Actions}' file

# {Actions} are bash statments to be run on the matched pattern p1


# BEGIN { Actions} # actions executed before starting to read lines from INPUT
# {ACTION} # Action for everyline in a file
# END { Actions }


# awk '{print;}' file.txt

# Awk Example 3. Print only specific field.

#Awk has number of built in variables. For each record i.e line, it splits the record delimited by whitespace character by default and stores it in the $n variables. If the line has 4 words, it will be stored in $1, $2, $3 and $4. $0 represents whole line. NF is a built in variable which represents total number of fields in a record.

#if(conditional-expression1)
#{
#	action1;
#	action1.1;
#}
#else if(conditional-expression2)
#	action2;
#else if(conditional-expression3)
#	action3;
#	.
#	.
#else
#	action n;

