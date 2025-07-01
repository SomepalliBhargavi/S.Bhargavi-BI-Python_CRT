'''write a python program to calculate Factorial of N using recursion'''

#factorial
n=int(input("enter a number: "))
def factorial(n):
    if n==0:
        return 1
    else :
        return n*factorial(n-1)
print(factorial(n))