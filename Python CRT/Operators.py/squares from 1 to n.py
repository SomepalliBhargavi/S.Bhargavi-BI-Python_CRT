#to print squares from 1 to n
Num=int(input("Enter the Value of Num :"))
print(f"squares from 1 to {Num} : ")
for i in range(1,Num+1):
    print(i*i)

#to print squares from n to 1
Num=int(input("Enter the Value of Num :"))
print(f"squares from {Num} to 1 : ")
for i in range(Num,0,-1):
    print(i*i)