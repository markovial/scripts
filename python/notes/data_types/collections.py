
# https://www.youtube.com/watch?v=UdcPhnNjSEw

# collections are special continer data types
# counter : stores elements as dictionary keys , counts as dictionary values
# namedtuple : 

from collections import Counter

string = "aaabbbbcccd"
counter = Counter(string)


# counter        : key value pairs , value = count of key
# items()        : prints only the stored count values
# elements()     : returns iterator over elements , i.e., actual original list
# keys()         : returns iterable over keys
# values()       : returns iterable over values
# most_common(n) : returns the 'n' most common types


print("counter             : " , counter)
print("counter(value)      : " , counter['a'])
# better because none is returned instead of throwing an exception
print("counter(value)      : " , counter.get('a'))
print("counter(value)      : " , counter.get('f' , "Error Message"))
print(".items()            : " , counter.items())
print(".elements()         : " , list(counter.elements()))
print(".keys()             : " , counter.keys())
print(".values()           : " , counter.values())
print(".most_common()      : " , counter.most_common(2))

print(".most_common(key)   : " , counter.most_common(2)[0][0])
print(".most_common(value) : " , counter.most_common(2)[0][1])
print(".most_common(key)   : " , counter.most_common(2)[1][0])
print(".most_common(value) : " , counter.most_common(2)[1][1])

