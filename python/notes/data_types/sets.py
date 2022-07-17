# A set is an unordered collection of elements without duplicate entries. 

def input():
    input_string = "This is a string."
    input_list = [1,22,33,444]
#    input_int = set(map(int, input().split())
#    input_string = set(input().split())

    print(set(input_string))
    print(set(input_string.split(" ")))
    print(set(input_list))

    # add() : adds an elements if it does not already exist in the set
    my_set = {"a","b","c"}
    my_set.add("a")
    my_set.add("d")
    print("add() : " , my_set)


def access():
    my_set = {"a", "b", "c"}
    for x in my_set:
      print(x)

def check():

    my_set = {"a", "b", "c"}
    print("b" in my_set)

    my_set = {0, 1, 0}
    print("any() : " , any(my_set))




def operations():

    a = {2, 4, 5, 9}
    b = {2, 4, 11, 12}

    # union()             : Values which exist in a or b
    print("union()        : " , a.union(b))
    # intersection()      : Values which exist in a and b
    print("intersection() : " , a.intersection(b))
    # difference()        : Values which exist in a but not in b
    print("difference()   : " , a.difference(b))

    # symmetric_difference() : values that exist in a and b , but not in both
    # ^ operator can be used for symmetric difference
    print("symmetric_difference()   : " , a.symmetric_difference(b))
    print("^   : " , a^b)


def add():
    a = set("abc")
    b = set("def")

    print(a)
    print(b)
    # .update() or |= : add elements from another set
    #                 : updates happens in place
    a.update(b)
    print("update() : " , a)

    # .intersection_update() or &= : add elements found only in both sets
    a = set("abc")
    b = set("ab")
    a.intersection_update(b)
    print("intersection_update() : " , a)

    # .difference_update() or -= : remove elements found in another set
    a = set("abc")
    b = set("ab")
    a.difference_update(b)
    print("difference_update() : " , a)

    # .symmetric_difference_update() or ^= : add elements found in either set
    # but not both

    a = set("abc")
    b = set("ab")
    a.symmetric_difference_update(b)
    print("symmetric_difference_update() : " , a)

def delete():

    my_set = {"a","b","c"}

if __name__ == '__main__':
#    input()
#    access()
    add()
#    delete()
#    check()
#    operations()
