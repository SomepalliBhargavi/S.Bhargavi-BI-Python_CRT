'''write a python program to print even numbers from 1 to n using list
comprehension'''
n=int(input("Enter the n value :"))
Even=[i for i in range(n) if i%2==0]
print(Even)