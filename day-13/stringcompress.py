s="aaaaaaabbbbbbcccccdddddtttttgggggg"
c=1
res=''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        res+=s[i]+str(c)
        c=1
print(res+s[i]+str(c))
print(i)