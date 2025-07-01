#checks with every adjacent elemnt
Arr=[25,20,15,10,5]
print(f"Original Array :{Arr}")
count=0
for i in range(len(Arr)):
    Flag=False
    for j in range(len(Arr)-1):
        if(Arr[j]>Arr[j+1]):
            Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
            print(Arr)
            Flag=True
    if Flag==False:
        break
print(Arr)