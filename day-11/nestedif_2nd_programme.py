reg=eval(input("Are you registered: "))
if reg:
    fee=eval(input("Have you paid the fee: "))
    if fee:
        print("You can attend the event")
    else:
        print("You can't attend the event, because you have not paid the fee")
else:
    print("You can't attend the event, because you are not registered")            