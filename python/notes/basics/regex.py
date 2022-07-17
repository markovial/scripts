import re

# r        : raw string , changes rules in backslash interpretation
#findall() : list , containing all matches
#search()  : bool , result of found
#split()   : list , string split at each match
#sub()     : string , replace match with a string
#re.sub(pattern, repl, string, count=0, flags=0)

sentence = "5 and 10 are the digits."
pattern  = "\d{1,}"
matches  = re.findall( rf"{pattern}", sentence);               #print (matches)
matches  = re.search ( rf"{pattern}", sentence);               #print (matches)
matches  = re.split  ( rf"{pattern}", sentence);               #print (matches)
matches  = re.sub    ( rf"{pattern}", "!!" ,sentence);         #print (matches)
matches  = re.sub    ( rf"{pattern}", "!!" ,sentence,count=1); #print (matches)

# num_matches = len(matches)

# iterator over matches
for item in re.finditer(rf"{pattern}", sentence):
    print(item)
    print(item.groups())

# sentence = "1 = value ,2 = value ,3 = value"
# pattern  = "(?P<key>^\d{1,})(?P<value>)"
# for item in re.finditer(rf"{pattern}", sentence):
    # print(item.groupdict())



s = 'I refer to https://google.com and I never refer http://www.baidu.com if I have to search anything'
# p = "(?<=https:\/\/)([A-Za-z0-9.]*)"
p = "(?<=[https]:\/\/)([A-Za-z0-9.]*)"
m = re.findall(rf"{p}",s)
print(m)
