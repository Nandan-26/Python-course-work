# i=10
# while i>0:
#     print(i)
#     i-=1

# s="python programming"
# i=0
# while i<len(s):
#     print(i,'.',s[i])
#     i+=1

# s="python programming"
# i=len(s)-1
# while i>=0:
#     print(i,'.',s[i])
#     i-=1

# l=[1,2,3,4,5]
# i=0
# while i<len(l):
#     print(i,'.',l[i], ',',end=' ')
#     i+=1
    
# i=0
# while i<10:
#     print(i,end="") 
#     i+=1   

# n=8765
# s=0
# p=1
# while n>0:
#     print(n%10,end="")
#     p*=n%10
#     s+=n%10
#     n//=10
# print("\nSum of digits:", s)
# print("Product of digits:", p)

# n=5678
# res=0
# while n>0:
#     rem=n%10
#     if rem%2==0:
#         res=res+rem
#     n//=10
# print(res)

# l=[7,9,23,0,0,0,0,12,0,34,0,0,0,0,0,0]
# while 0 in l:
#     l.remove(0)
# print(l)    
        
l=[2,3,6,76,12,4,1,5,61,4,5,2,23]  
i=0
s=0
j=len(l)-1
while i<=j:
    if i==j:
        print(l[i])
    else:
        s=l[i]+l[j]
        print(s)
    i+=1
    j-=1
      