Num=int(input("Enter the Value of Num :"))
Temp=Num
DigitSum=0
Rem=0
while(Num!=0):
    Rem=Num%10
    DigitSum=DigitSum+Rem
    Num=Num//10
print(f"Summation is {DigitSum}")
