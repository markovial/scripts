
echo "----------"
echo "uniq"
echo "----------"

# uniq : remove all but one copy of SUCCESSIVE repeated lines
# to remove all duplicates , sort it , then pipe into uniq

# uniq -c : counts occurrance of each item , works best after sort
# uniq -d : shows only items in list that are repeated , i.e. count > 1
# uniq -u : shows only items in list that are not repeated , i.e. count = 1

# uniq -w : Limit comparison only to the first N characters
# uniq -s : Avoid comparing the first N characters
# uniq -i : Ignore variations in case between lines
# uniq -f : Avoid comparing the first N fields


