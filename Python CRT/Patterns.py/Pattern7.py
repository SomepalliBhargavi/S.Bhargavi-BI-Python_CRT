'''
P 
P Y 
P Y T 
P Y T H 
P Y T H O 
P Y T H O N
'''
Str="PYTHON"
Length=len(Str)
for i in range(Length):
    for j in range(i+1):
        print(f"{Str[j]} ",end="")
    print()