# to print pattern D
# n = int(input("enter the size : "))
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print() 

# to print pattern B
# n = int(input("enter the size : "))
# m = n//2
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1 or i==m:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()        

# to print pattern E
# n = int(input("enter the size : "))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or i==m:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print() 

# To print the pattern " F "
# n = int(input("enter the size : "))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==m:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print() 

# pattern C
# n = int(input("enter the size : "))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print() 

# pattern G
# n = int(input("enter the size : "))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or (j==n-1 and i>=m) or (i==m and j>=m):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print() 

#pattern S
# n = int(input("enter the size : "))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if (i==0 and i<=m) or (j==0 and i<=m) or i==n-1 or (j==n-1 and i>=m) or i==m:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print() 

# pattern J
# n = int(input("enter the size : "))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i==0 or (i==n-1 and j<=m) or j==m:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print() 

# pattern Z
# n = int(input("enter the size : "))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or (i+j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print() 

# pattern X
# n = int(input("enter the size : "))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i==j  or (i+j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print() 

# pattern Y
# n = int(input("enter the size : "))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if (i==j and i<=m)  or (i+j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print() 

# pattern M
# n = int(input("enter the size : "))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if  j==0 or (i==j and i<=m)  or (i+j==n-1 and j>=m) or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print() 

# pattern W
# n = int(input("enter the size : "))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if  j==0 or (i==j and i>=m)  or (i+j==n-1 and j<=m) or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print() 

# pattern v
# n = int(input("enter the size : "))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if  (j==0 and i<=m) or (j==n-1 and i<=m) or (i-j==m and i>=m) or (i+j==n+m-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()

# pattern A
# n = int(input("enter the size : "))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if  (j==0 and i>=m) or (j==n-1 and i>=m) or (i+j==m and i<=m) or (j-i==m and j>=m) or i==m+1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()

n = int(input("enter the size : "))
m=n//2
for i in range(n):
    for j in range(n):
        if  (j==0 and i>=m) or (j==n-1 and i>=m) or (i+j==m and i<=m) or (j-i==m and j>=m) or i==m+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()
