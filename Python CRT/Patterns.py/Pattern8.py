'''
P 
Y Y 
T T T 
H H H H 
O O O O O 
N N N N N N
'''
Str="PYTHON"
Length=len(Str)
for i in range(Length):
    for j in range(i+1):
        print(f"{Str[i]} ",end="")
    print()