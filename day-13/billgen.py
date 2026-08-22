data={
    'sugar': 10,
    'salt': 5, 
    'rice': 20,
    'wheat': 15,
    'cooking oil': 50,
    'milk': 30,
    'eggs': 70,
    'bread': 20,
    
}
prods=input("Enter the products you want to buy : ").split(",")
total=0
print("YOUR BILL".center(50,"-"))
print("Product".ljust(25), "Price")
for i in prods:
    print(i.ljust(25), data[i])
    total+=data[i]
print("Total amount to be paid :".ljust(25), total)
print("\n" + "Thank you for shopping with us".center(50,"*"))
    
   