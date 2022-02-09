#!/bin/bash

echo "----------"
echo "paste"
echo "----------"

# can be really useful in transforming files from one type tsv to another csv

# paste       : uses tab by default , joins lines in file
# paste -s    : joins all lines in file
# paste -d,   : joins all lines based on given delimiter , which is ',' here
# paste -     : will read and join every 1 line
# paste - -   : will read and join every 2 lines
# paste - - - : will read and join every 3 lines , and so on
# paste -d, file1 file2 ; joins two files sidy by side
