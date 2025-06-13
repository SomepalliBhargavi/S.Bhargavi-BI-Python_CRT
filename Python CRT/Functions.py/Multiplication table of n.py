'''write a python program to build a function which prints the multiplication 
table of n '''

def Multiplication_table(Num):
    for i in range(1,11):
        print(f"{Num}*{i}={i*Num}")  
Multiplication_table(4)


'''write a python program to build a function which prints the multiplication 
tables from 1 to n '''

def Multiplication_table(Num):
    for i in range(1,Num+1):
        for j in range(1,11):
            print(f"{i}x{j}={i*j}")
Multiplication_table(3)