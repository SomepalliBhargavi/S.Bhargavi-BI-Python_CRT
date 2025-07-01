'''write a python program to calculate sum of first N natural 
numbers using recursion'''

#sum of first N natural numbers
n1=int(input("Enter a number: "))
def sum(n1):
    if n1==0:
        return 0 
    else:
        return n1+sum(n1-1) 
      
print(sum(n1))