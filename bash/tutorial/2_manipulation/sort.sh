#!/bin/bash

# commands

STRING="word 1 , word 2 , word 3."
TAB_STRING="	word 1,	word 2,	word 3."

echo "----------"
echo "sort"
echo "----------"

Sort Options

# sort : sort input lexicographically
# sort -n : sort numerically , if first word / column is a number
# sort -r : sort either reverse lexicographical , or reverse numerical
# (descending)

# sort -k : sort based on specific column in table of data (tsv,csv etc.) 
# sort -t : sort while specifing a particular delimiter , . | ; : which is used
# to seprate the values you want sorted


sort -t$'\t' -nr -k2 file_name.txt
sort -t'|' -nr -k2 file_name.txt


