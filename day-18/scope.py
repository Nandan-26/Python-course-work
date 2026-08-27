#local variable scope- just inside the function.
# def display():
#     n=10
#     print("inside function : ",n)
    
# display()
# print("outside the function : ",n)    
#
# OUTPUT:
#NameError: name 'n' is not defined
# GLOBAL VARIABLE SCOPE-throught the file both the inside and the outside.
# def display():
#     print("inside the function : ",n)
# n=10
# display()
# print("inside the function : ",n) 

#note : keyword to convert local variable to global variable is "global"  

# def display():
#     global n
#     n=10
#     print("inside the function : ",n)
# display()
# print("inside the function : ",n) 

# output:
#     (base) PS C:\Users\eswar\OneDrive\Desktop\Python-course-work\day-18> py scope.py
#         inside the function :  10
#         inside the function :  10
# note : global variable cannot be taken as parameter and whatever the task done inside to global variable will be applied throughout the code ,let see example
# def display():
#     global n
#     n+=10
#     print("inside the function : ",n)
# n=10   
# display()
# print("inside the function : ",n) 

# note : nonlocal will make a variable avaialable through out the fuction it can be inner fuction , outter functio or nested functiob
# def display():
#     course = "PFS"
#     def update():
#         nonlocal course
#         course="jfs"
#         print("inside the function : ",course)
#     update()
#     print("inside the function : ",n)       
# n=10   
# display()
# print("inside the function : ",

#note : int float complex str list tuple set dict bool
#note : list dict set  can be updated   
      
# def display(n):
#     n[5]=6
#     print("Inside the function :",n)
# n={1:2,3:4}
# display(n)
# print("outside the function :",n)    

# 
# def display(n):
#     n.add(65)
#     print("Inside the function :",n)
# n={1,2,3,4,5}
# display(n)
# print("outside the function :",n)  

def display(n):
    n.add(65)
    print("Inside the function :",n)
n={1,2,3,4,5}
display(n)
print("outside the function :",n) 




