'''
Write a python program to read a string as a input from the user and print the count of
a) upper case vowels
b) lower case vowels
c) upper case consonants
d) lower case consonants
 '''

Str=input("Enter the String :")
U_Vowels,L_Vowels,U_Consonants,L_Consonants=0,0,0,0
for ch in Str:
    if(ch.isalpha() and ch.isupper()):
        if ch in 'AEIOU':
            U_Vowels+=1
        else:
            U_Consonants+=1
    if(ch.isalpha() and ch.islower()):
        if ch in 'aeiou':
            L_Vowels+=1
        else:
            L_Consonants+=1
print(f"Lower Case  Vowels Count :{L_Vowels}")
print(f"Upper Case  Vowels Count :{U_Vowels}")
print(f"Lower Case  Consonants Count :{L_Consonants}")
print(f"Upper Case  Consonants Count :{U_Consonants}")

#with using loops

Str=input("Enter the String :")
U_Vowels,L_Vowels,U_Consonants,L_Consonants=0,0,0,0
for ch in Str:
    if(ch>='A' and ch<='Z'):
        if ch in 'AEIOU':
            U_Vowels+=1
        else:
            U_Consonants+=1
    if(ch>='a' and ch<='z'):
        if ch in 'aeiou':
            L_Vowels+=1
        else:
            L_Consonants+=1
print(f"Lower Case  Vowels Count :{L_Vowels}")
print(f"Upper Case  Vowels Count :{U_Vowels}")
print(f"Lower Case  Consonants Count :{L_Consonants}")
print(f"Upper Case  Consonants Count :{U_Consonants}")