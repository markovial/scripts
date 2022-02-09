#!/bin/bash
# http://linuxcommand.org/lc3_writing_shell_scripts.php
# My first script

# The first line of the script is important. This is a special clue, called a
# shebang # = hash and ! = bang, given to the shell indicating what program is
# used to interpret the script. In this case, it is /bin/bash. Other scripting
# languages such as Perl, awk, tcl, Tk, and python also use this mechanism.


# the -n flag suppresses the newline

echo -n "What is your name?"
read PERSON
echo "Hello, $PERSON"

# when a shell show either % or $ it is waiting for some input
# there are two types of shells :
# Bourne - $ prompt
# C Shell - % prompt

#The Bourne Shell has the following subcategories −

#    Bourne shell (sh)
#    Korn shell (ksh)
#    Bourne Again shell (bash)
#    POSIX shell (sh)

#The different C-type shells follow −

#    C shell (csh)
#    TENEX/TOPS C shell (tcsh)

