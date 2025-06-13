'''Write a python program to read mail ID as input from the user and 
print username and organization name based on mail id (name@orgname.com)
'''
Mail_ID=input("Enter the mail ID :")
List=Mail_ID.split('@')
print(f"User Name : {List[0]}")
Org=List[1]
List=Org.split('.')
print(f"Org Name :{List[0]}")

#by removeprefix
Mail_ID=input("Enter the mail ID :")
#name@org.com
n=Mail_ID.removeprefix('.com')
print(n)