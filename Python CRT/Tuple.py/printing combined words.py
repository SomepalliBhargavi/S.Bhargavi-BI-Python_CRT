n=int(input("Enter the no.of words that you would like to find : "))
List=['Marker','Water','Wrist','Bread','Class','home','jim','black','crack']
Tuple=('Pen','Bottle','Watch','Jam','Room','Theatre','jam','board','jack')
i=1
while(i<=n):
    word=input("Enter the word :")
    index=List.index(word)
    print(f"{word}-{Tuple[index]}")
    i+=1