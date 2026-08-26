data={
    'eswar':{'status':True,'python':90,'mysql':95,'flask':98},
    'ram':{'status':False,'python':None,'mysql':None,'flask':None},
    'suresh':{'status':True,'python':70,'mysql':75,'flask':78},
    'jayanth':{'status':True,'python':80,'mysql':85,'flask':88},
    'kumar':{'status':False,'python':None,'mysql':None,'flask':None},
    'sai':{'status':True,'python':30,'mysql':35,'flask':38},
    'raghu':{'status':True,'python':60,'mysql':15,'flask':40}
}
name=input("Enter the name: ")
if name in data:
    if data[name]['status']:
        sum=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=sum/3
        print(f"hello {name}!!!")
        print(f"Your Average Score is: {avg}")
        if avg>=90:
            print("Outstanding")
        elif avg>=80:
            print("Excellent")
        elif avg>=70:
            print("Very Good")
        elif avg>=60:
            print("Good")
        elif avg>35:
            print("Average ,better luck next time")    
        else:
            print("Your Failed, you need to work hard")  
    else:
        print(f"hello {name}!!!")
        print("You are not eligible to see the result, because your are absent,please bring your parents")                  

else:
    print(f"Name {name} not found in the data")    