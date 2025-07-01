'''
P Y T H O N 
P         N 
P         N 
P         N 
P         N 
P Y T H O N
'''
Str="PYTHON"
Length=len(Str)
for i in range(Length):
    for j in range(Length):
        if i==0 or i==Length-1 or j==0 or j==Length-1:
            print(f"{Str[j]}",end=" ")
        else:
            print(" ",end=" ")
    print()