# optional number of arguments
# *args    : tuple of args
# **kwargs : dict of args
def sayhello(*names):
    for name in names:
        print(f"Hello, {name}")

def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
myFun(first ='Geeks', mid ='for', last='Geeks')



# unorganized arguments
# basically specify in func call
def person(name,age):
    print(name)
    print(age-1)
#person(age=25,name="Bob")

# default argument value
# overriden if passed as arg
def person(name,age=18):
    print(name)
    print(age-1)
#person("Bob",25)

# specify types of args
# -> return type
def my_func(l: list, index: int) -> int:
    return l[index]
#print(type(my_func(['a','b'],1)))

