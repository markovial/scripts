#!/bin/bash

echo "----------"
echo "grep"
echo "----------"

# find a pattern

# grep "word" file.txt             : search for strings and sub-strings of "word"
# grep 'phase' 'filename'          : find and return all occurances of the phrase (or regex) in the given file
# grep 'phrase' *                  : return all lines that match the given phrase from all files in cur directory
# grep -i 'phrase'                 : return all lines (case insensitive) that match the given phrase in the given files
# grep -w "word" file.txt          : search only for full strings , no substrings
# grep -v 'phrase' 'filename'      : Do an inverse match , i.e., return all lines that do not contain the given phrase
# grep -l 'phrase' *               : return all filenames that contain the given phrase
# grep -c 'phrase' *               : return count of the number of lines (not times) the phrase occurs in the specified files
# grep -r 'phrase' *               : search for phrase recursively in all subdirectories
# grep -e "pattern1" -e "pattern2" : search one file for multiple patterns
# grep "phrase with space" *       : use double quotes to search for phrases that contain spaces
# grep -A 3 -i "example" demo_text : show 3 lines AFTER match
# grep -B 3 -i "example" demo_text : show 3 lines BEFORE match
# grep -C 3 -i "example" demo_text : show 3 lines BEFORE and AFTER (CONTEXT) match

# GREP + REGEX

# grep -E 'regex_pattern' file.txt

#^ matches the empty string at the beginning of a line
#$ (dollar) symbol matches the empty string at the end of a line
#. (period) symbol is a meta-character that matches any single character
#[[:alnum:]]	Alphanumeric characters.
#[[:alpha:]]	Alphabetic characters.
#[[:blank:]]	Space and tab.
#[[:digit:]]	Digits.
#[[:lower:]]	Lowercase letters.
#[[:upper:]]
#*	Match the preceding item zero or more times.
#?	Match the preceding item zero or one time.
#+	Match the preceding item one or more times.
#{n}	Match the preceding item exactly n times.
#{n,}	Match the preceding item at least n times.
#{,m}	Match the preceding item at most m times.
#{n,m}	Match the preceding item from n to m times.



