'''Write a python program to read a string as input from the 
user and replace all vowels with '0' zero'''

Str=input("Enter the string :")
modified=""
for ch in Str:
    if ch in 'AEIOUaeiou':
        modified+='0'
    else:
        modified+=ch
print(modified)

