l=eval(input("Is Link Active.: "))
if l:
    a=eval(input("Is Access Permission is granted.: "))
    if a:
        print("You can access the link")
    else:
        print("You can't access the link, because you don't have permission to access the link")
else:
    print("Link is not active, please check the link")            