'''write a program toread a string as input from the user and print:
1.count of uppercase letters
2.count of lowercase letters
3.print the count of numeric values
4.print the count of special characters
'''
Str=input("Enter the string : ")
Uppercase_Alpha=0
Lowercase_Alpha=0
Numeric=0
Special_char=0
for ch in Str:
    if ch.isupper():
        Uppercase_Alpha=+1
    elif ch.islower():
        Lowercase_Alpha=+1
    elif ch.isdigit():
        Numeric+=1
    else:
        Special_char+=1
print(f"Count of the Uppercase letters :{Uppercase_Alpha}")
print(f"Count of the lowercase letters :{Lowercase_Alpha}")
print(f"Count of Numeric values :{Numeric}")
print(f"count of the special characters :{Special_char}")
