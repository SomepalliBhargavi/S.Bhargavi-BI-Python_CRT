#to print cubes from 1 to n
Num=int(input("Enter the Value of Num :"))
print(f"cubes from 1 to {Num} : ")
for i in range(1,Num+1):
    print(i*i*i)

#to print cubes from n to 1
Num=int(input("Enter the Value of Num :"))
print(f"cubes from {Num} to 1 : ")
for i in range(Num,0,-1):
    print(i*i*i)