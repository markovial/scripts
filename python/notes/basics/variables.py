import random

# random number
print(random.randrange(1, 10))

# Check type of variable
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x), type(y) , type(z))

# Casting one type to another
c = complex(x)   # convert int to complex
x = 1            # int
y = 2.8          # float
z = 1j           # complex
a = float(x)     # convert from int to float
b = int(y)       # convert from float to int
x = int(1)       # x will be 1
y = int(2.8)     # y will be 2
z = int("3")     # z will be 3
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1")    # x will be 's1'
y = str(2)       # y will be '2'
z = str(3.0)     # z will be '3.0'
