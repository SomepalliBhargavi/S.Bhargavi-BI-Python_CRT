# to know how the method is called 
N=int(input("Enter the value of n:"))
i=0
def NaturalNum(N,i):
    i=i+1
    if N==0:
        return
    NaturalNum(N-1,i)
    print(f" {i} Method Call")
NaturalNum(N,i)