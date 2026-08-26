budget=int(input("Enter your budget: "))
if budget >10000:
    print("Cloud Hosting")
elif budget >5000:
    print("Bussiness Hosting")
elif budget >2000:
    print("Premium Hosting")
else:
    print("Single Hosting")