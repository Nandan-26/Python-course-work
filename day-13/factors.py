n=int(input("Enter the input : "))
res=[i for i in range(1, n+1) if n % i == 0] 
print(f'Factors of {n} are : {res}')



