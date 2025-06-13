'''write a program to read password as input from the user 
and check whether it is a valid password or invalid password '''

import string
password=input("Enter your password :")
upper=lower=digit=special=0
for ch in password:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
    elif ch.isdigit():
        digit+=1
    elif ch in string.punctuation:
        special+=1
    else:
        special+=1
    if(len(password)>=10 and upper>=3 and lower>=3 and special>=3
       and digit>=1):
        print("Valid password")
    else:
        print("Invalid password")