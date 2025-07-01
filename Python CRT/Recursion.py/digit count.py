'''write a python program to calculate Sum of Digits of the given number
using recursion'''

n=int(input("enter the number: "))
b=int(input("enter the power number: "))
def Power(n, b):  
    if b == 0:
        return 1
    else:
        return n * Power(n, b - 1) 
print(Power(n,b))