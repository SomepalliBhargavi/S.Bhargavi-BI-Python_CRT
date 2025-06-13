Num=int(input("Enter an integer :"))
Num_str=str(Num)
Zero_count=0
for digit in Num_str:
    if digit=='0':
        Zero_count+=1
print(f"No.of Zero's present in {Num} are {Zero_count}")