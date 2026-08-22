#str list tuple set dict range
'''s="python programming"
for i in s:
    print(i)'''
    
'''
l=[1,2,3,4,5]  
for num in l:
    print(num)  '''
    
'''prices=(9696,6985,56669,231)  
for x in prices:
    print(x)  '''
    
'''names= {'nandan','ram','vamshi','sai'}    
for name in names:
    print(name) '''
    
'''dict={'name':'nandan','age':22,'place':'hyderabad'}
for key in dict:
    print(key,dict[key]) '''  
    
# range function range(start,end+1,step)
'''for i in range(1,11):
    print(i) '''    
'''
for i in range(2,21,2): 
    print(i)       '''
    
'''for i in range(10,0,-1):
    print(i) '''
    
'''for i in range(5,101,5):
    print(i)'''
    
'''s="python programming  "
for i in range(len(s)):
    print(i,s[i])
    # when ever  we want index we have to use range function with len() function  ''' 
    
# we only use range function with for loop and we can use it with len() function to get index of the string, list, tuple.
#we cant use range function with set and dict because they are unordered data types.

# we use enumerate() function to get index of the set and dict,because enumerate returns data in the form of tuple and tuple is ordered data type.let's see the example of enumerate function with set and dict.

'''s={1,2,3,4,5}
for i in enumerate(s):   
    print(i[0],i[1]) ''' # i[0] is index and i[1] is value of the set.as output will be in the form of tuple because enumerate returns data in the form of tuple.
# the output for above code will be in the form of (index,value) because enumerate returns data in the form of tuple. and we can use index to access the value of the set.

'''for i in range(1,11):
    if i==5:
        break
    print(i)
# here break statement is used to exit the loop when i is equal to 5. so the output will be 1,2,3,4 and the loop will exit when i is equal to 5.
#so break statement is used to exit the loop when a certain condition is met.consider it as a jump statement which will jump out of the loop when a certain condition is met.    
'''
'''for i in range(1,11):
    if i==5:
        continue
    print(i)    
# here continue statement is used to skip the current iteration when i is equal to 5. so the output will be 1,2,3,4,6,7,8,9,10 and the loop will skip the iteration when i is equal to 5.
#so continue statement is used to skip the current iteration when a certain condition is met.consider it as a jump statement which will jump to the next iteration when a certain condition is met.    '''

'''l=[12,13,14,15,16,17,18,19,20]
n=26
for i in l:
    if i==n:
        print("found")
        break
else:
    print(n,"not found") 
# here else statement is executed when the loop is completed without any break statement. so the output will be 26 not found because the loop is completed without any break statement.  
     '''

#unlocking a mobile ,here you have 5 attempts to unlock the mobile, if you enter the wrong password 5 times then the mobile will show try again after 30 seconds. if you enter the correct password then the mobile will unlock and show welcome message. if wrong password is entered then the mobile will show wrong password message and ask to enter the password again. if you enter the wrong password 5 times then the mobile will show try again after 30 seconds message.
'''pin=1234
for i in range(5):
    user_pin=int(input("enter your pin:"))
    if user_pin==pin:
        print("welcome")
        break
    else:
        print("wrong pin try again")
else:
    print("try again after 30 seconds")        '''
    
#prime number or not
n=int(input("enter a number:"))
for i in range(2,n//2+1):
    if n%i==0:
        print(n,"is not a prime number")
        break
else:
    print(n,"is a prime number")