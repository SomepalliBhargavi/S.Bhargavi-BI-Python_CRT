'''write a program to take name as input from the user including 
prefix(Mr,Mrs) print the gender classification of the name on bases of
prefix 
'''
Str=input("Enter the Name with prefix (MS/Mr) : ")
if Str.startswith('Mr.'):
    print("Male")
elif(Str.startswith('Ms.')):
    print("Female")
else:
    print("In-valid name")