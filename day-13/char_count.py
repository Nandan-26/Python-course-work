s='python programming'
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1   # default it will initialize the value of the key with 1 if it is not present in the dictionary.
print(d)