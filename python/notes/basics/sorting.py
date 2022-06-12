from operator import itemgetter
# sort()   : sorts lists , sorts the list in place
# sorted() : sorts any iterable obj. , returns a new list object

x = [5, 2, 3, 1, 4].sort();                             # print(x)  # List : in place
x = sorted([5, 2, 3, 1, 4]);                            # print(x)  # List : return obj

x = [['A', 4], ['B', 2], ['C', 1], ['D', 3]];           # LIST
x.sort(key = lambda x: x[0]);                           # print(x)  # List : specified field , in place
x.sort(key = lambda x: x[1]);                           # print(x)  # List : specified field , in place

x = {1: 'D', 2: 'B', 3: 'E', 4: 'C', 5: 'A'}            # DICTIONARY
y = sorted(x);                                          # print(y)  #
y = sorted(x.items(),key=lambda x:x[0]);                # print(y)  #
y = sorted(x.items(),key=lambda x:x[1]);                # print(y)  #

y = [ ('a', 'A', 15), ('b', 'B', 12), ('c', 'B', 10), ] # TUPLE
x = sorted(y, key=lambda y: y[0]);                      # print (x) #  Sort Tuple : specified field
x = sorted(y, key=lambda y: y[1]);                      # print (x) #  Sort Tuple : specified field
x = sorted(y, key=lambda y: y[2]);                      # print (x) #  Sort Tuple : specified field

