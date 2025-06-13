Num=int(input("Enter the Value of Num :"))
for i in range(1,Num+1):
    print(f"Multiplication table of {i}:")
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
