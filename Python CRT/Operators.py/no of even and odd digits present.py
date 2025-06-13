Num=int(input("Enter an integer :"))
even=0
odd=0
while Num!=0:
    rem=Num%10
    if(rem%2==0):
        even+=1
    else:
        odd+=1
print(f"No of even digits : {even}")
print(f"No of odd digits:{odd}")