import itertools
from itertools import chain # iterate over multiple lists
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import zip_longest # Unequal lengths
from itertools import islice
from itertools import pairwise
from itertools import compress

a , b , c = ['x','y','z'] , [1,2,3] , [0,0,1]

print("Chain       : " , end=" ")
# chain is better than :  for _ in (a+b) , 
# a+b creates a new list which wastes memory on large datasets
for _ in chain(a,b):
    print(_ , end ="")
print()


print("Compress    : " , end=" ")
x = list(compress(a,c)); print(x) # show only elements in a , where elment in c = 1

print("Pairwise    : " , end=" ")
x = list(pairwise(a)); print(x)


print("islice      : " , end=" ")
x = list(islice(a,1,None)); print(x) #seq[start:stop:step]

print("Zip         : " , end=" ")
# useful when constructing dictionaries
for _ in zip(a,b):
    print(_ , end =" ")
print()


print("Product     : " , end=" ")
x = list(product(a,b));  print (x) # equivalent to nested for loops


print("Enum        : " , end=" ")
for i , item in enumerate(a,1): print(i,item,end=" ")
print()

print("Combination : " , end=" ")
x = list(combinations(a,2)); print(x) # combinations , length 2

print("Combination (r) : " , end=" ")
x = list(combinations_with_replacement(a,2)); print(x) # combinations , length 2

print("Permutation : " , end=" ")
x = list(permutations(a,2)); print(x) # permutations , length 2

print("Long zip    : " , end=" ")
a , b = ['x','y','z'] , [1]
for _ in zip_longest(a,b,fillvalue='!!!'): print(_,end="")

# iterator that counts
counter = itertools.count();
for _ in counter:
    if _ < 5 : continue; print(_ , end="")
    elif _ >= 5 : break;
