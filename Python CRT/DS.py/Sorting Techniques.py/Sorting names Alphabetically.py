lst=[]
num=int(input("Enter the number of names to be in the list: "))
for i in range(num):
    temp=input("Enter the name:")
    lst.append(temp)
print(lst)
for i in range(num):
    for j in range(num-1):
        if(lst[j]>lst[j+1]):
            t=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=t
print(lst)
