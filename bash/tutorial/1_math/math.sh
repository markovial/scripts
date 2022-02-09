#!/bin/bash

# do math on integers
# bc -l, {- -mathlib } : Define the standard math library
NUM1=1
NUM1=$(echo $NUM1 + 1 | bc -l)
echo $NUM1


NUM2=3
NUM3=$((NUM1 + NUM2))
echo $NUM3


# print sig figs for ints
printf "%.3f" $(echo $NUM3 | bc -l)
echo

# do math on floats
# scale specifies sig figs
NUM1=$(echo "scale=2; $NUM3/$NUM2" | bc)
echo $NUM1






