'''
N O H T Y P 
N O H T Y P 
N O H T Y P 
N O H T Y P 
N O H T Y P 
N O H T Y P 
'''
Str="PYTHON"
Length=len(Str)
for i in range(Length):
    for j in range(Length):
        print(f"{Str[Length-j-1]} ",end="")
    print()