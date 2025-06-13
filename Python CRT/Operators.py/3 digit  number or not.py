Num=int(input("Enter the Integer Value:"))
#using if-else
if(Num>100 and Num<999):
    print(f"{Num} is a Three Digit Number")
else:
    print(f"{Num} is not a Three Digit Number")
#Ternary
Result="Three Digit Number" if(Num>=10 and Num<=99) else "not a Three Digit Number"
print(f"{Num} is {Result}")