'''write a python program to print natural numbers from 1 to n'''
N=int(input("Enter the value of n:"))
def NaturalNum(N):
    if N==0:
        return
    NaturalNum(N-1)
    print(N)
NaturalNum(N)
#n to 1
print("Natural Numbers from N to 1")
def NaturalNum(N):
    if N!=0:
      print(N)
      return NaturalNum(N-1)
NaturalNum(N)
