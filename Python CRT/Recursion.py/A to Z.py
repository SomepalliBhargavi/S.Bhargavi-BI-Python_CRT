'''write a python program to print Alphabets from A to Z using recursions'''
def Alphabets(ch):
    if ch>=ord('A') and ch<=ord('Z'):
        print(chr(ch))
        return Alphabets(ch+1)
ch=65
Alphabets(ch)

print("----------------------")
#Z to A
def Alphabets(ch):
    if ch>=ord('A') and ch<=ord('Z'):
        print(chr(ch))
        return Alphabets(ch-1)
ch=90
Alphabets(ch)
   