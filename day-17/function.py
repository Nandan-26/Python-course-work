# def functionname(args):
#     #logic or statements
#     return # optional

# functionname(parameters)


# def gst(price):
#     print("Original Price : ", price)
#     print("Final Price : ", price + (price * 0.18))

# gst(1000)
# gst(2000)
# gst(700)
# gst(5000)
# gst(1)   


# # tables
# def table(n):
#     print(f"{n}-Table".center(15)) 
#     print("-"*15)
#     for i in range(1,11):
#         print(f"{n} * {i} = {n*i}".center(14))
# for i in range(1,21) :
#     table(i)    

# def isleap(year):
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         return "Leap year"
#     else:
#         return "Not a leap year"
# print(isleap(2026))
# print(isleap(2016))
# print(isleap(2006))
# print(isleap(20116))


# def isprime(n):
# 	for i in range(2, int(n ** 0.5) + 1):
# 		if n % i == 0:
# 			return "Not a Prime Number"
# 	return "Prime Number"


# print(isprime(7))
# print(isprime(10))

# # positional,keyword,default,variablelength

# positional 
# def display(name,email,pwd):
#     print("name :",name,)
#     print("email :",email)
#     print("pwd :",pwd)
#     print()

# display("nandan","nandan123@gmail.com","Nandan@65")
# display("nandan123@gmail.com","nandan","Nandan@65")
# display("Nandan@65","nandan","nandan123@gmail.com")


# keyword arguments
# def display(name,email,pwd):
#     print("name :",name,)
#     print("email :",email)
#     print("pwd :",pwd)
#     print()

# display(name="nandan",email="nandan123@gmail.com",pwd="Nandan@65")
# display(email="nandan123@gmail.com",name="nandan",pwd="Nandan@65")
# display(pwd="Nandan@65",name="nandan",email="nandan123@gmail.com")

def display(name,email,pwd=None):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)
    
display("Nandan","email")
display("Nandan","email","pwd@123")    