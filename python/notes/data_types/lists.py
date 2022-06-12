import sys

def static_list():
    my_list = [11, 19, 21, 29, 46]
    print(my_list)
    print(len(my_list))

def dynamic_list():

    # Declaration Methods
    data1 = list();
    data2 = [];
    print(data1 == data2)

    # Dynamically sized list
    #print ("Dynamic list size ? : " , end="")
    #n = int(input());
    n=5
    data3 = ['x'] * n
    data4 = [0] * n

    print(data3)
    print(data4)

    # LIST COMPREHENSIONS

    # initializing using for loops
    ListOfNumbers = [ x for x in range(10) ]
    print(ListOfNumbers)

def nested_list():

    print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])
    ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0]
    print(ListOfThreeMultiples)


def list_operations():

    data1 = list();

    # insert(position,x)
    data1.insert(0,1)
    data1.insert(0,3)
    data1.insert(0,5)
    print(rf"insert : {data1} ")

    data1.sort(key=None, reverse=False)

    print(rf"sort   : {data1} ")

    data1.reverse()

    print(rf"reverse: {data1} ")

    # remove(x) : remove first occurance of x
    data1.remove(3)
    print(rf"remove : {data1} ")

    # append(x) : insert x at end of list
    data1.append(3)
    print(rf"append : {data1} ")

    # pop(): remove last element from list
    data1.pop()
    print(rf"pop    : {data1} ")

    print(rf"1 element    : {data1[0]} ")
    print(rf"1 element    : {data1[(0+1)]} ")

    # del keyword removes the specified index

    # delete the entire list

def casting():
    string_list = ["12","9","5","11"]
    # this is why we would want to do this
    # because sort is wierd on string lists of ints

    print("sorted string : " , sorted(string_list))
    int_list = list(map(int, string_list))
    print("sorted int : " , sorted(int_list))


if __name__ == '__main__':
    static_list()
    dynamic_list()
    nested_list()
    list_operations()
    casting()

    mylist = [False, True, False]
    x = any(mylist)
    print(x)

# check if all of these are in here
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list

