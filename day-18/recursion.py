# note : 3 conditions for recursion
#         1.function calling itself
#         2.base condition with return to stop and retrive the function
#         3. modifing the parameters
        
#         def function(args):
#             if base condition:
#                 return
#             function(modified args)
#example: print 1 to 10 numbers
# def display(n):
#     if n==11:
#         return
#     print(n)
#     display(n+1)
    
# display(1)  

#display 10 to 1 numbers:
# def display(n):
#     if n==0:
#         return
#     print(n)
#     display(n-1)
    
# display(10)  


def display(string, i):
    if i == len(string):
        return
    print(string[i])
    display(string, i + 1)

display("codegnan", 0)