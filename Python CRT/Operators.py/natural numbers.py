# to print the natural numbers from 1 to n
Num=int(input("Enter the Value of Num :"))
print(f"Natural Number from 1 to {Num} : ")
for i in range(1,Num+1):
    print(i,end=" ")

# to print the natural numbers from n to 1
Num=int(input("Enter the Value of Num :"))
print(f"Natural Number from {Num} to 1 : ")
for i in range(Num,0,-1):
    print(i)


