'''write a program that
checks if the string has only valid bases(A,T,G,C)
then count how many of each base there are.'''

s=input("Enter the sample base sequence: ")
A,T,G,C=0,0,0,0
for i in s:
    if i in 'A':
        A+=1
    elif i in 'G':
        G+=1
    elif i in 'T':
        T+=1
    elif i in 'C':
        C+=1
base={'A':A,'C':C,'G':G,'T':T}
print(base)

#another method
sequence=input("Enter the sequence: ")
base_count={'A':sequence.count('A'),'T':sequence.count('T'),'G':sequence.count('G'),'C':sequence.count('C')}
print(base_count)