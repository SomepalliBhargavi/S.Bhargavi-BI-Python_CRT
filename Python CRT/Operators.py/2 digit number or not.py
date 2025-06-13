Num=int(input("Enter the Integer Value:"))
#using if-else
if(Num>10 and Num<99):
    print(f"{Num} is a Two Digit Number")
else:
    print(f"{Num} is not a Two Digit Number")
#Ternary
Result="Two Digit Number" if(Num>=10 and Num<=99) else "not a Two Digit Number"
print(f"{Num} is {Result}")