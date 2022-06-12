
# loop over a list
for _ in ["a","b","c"] : print(_,end="")

# range( start , stop , increment )
# range (x,y)      : including x , not including y , default step 1
# range (x,y,step) : including x , not including y
for _ in range(6)        : print(_,end="")
for _ in range(2, 6)     : print(_,end="")
for _ in range(2, 30, 3) : print(_,end="")

for _ in range(6)        : break;           # print(_)
else                     : print("else br") # stopped by break => not execute

for _ in range(6)        : continue;        # print(_)
else                     : print("else ct") # stopped naturally => execute

i = 1
while i < 6:
    #print(i)
    if i == 5: continue
    if i == 3: break
    i += 1

