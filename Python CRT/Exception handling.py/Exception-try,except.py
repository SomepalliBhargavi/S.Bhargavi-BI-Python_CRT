''' try:
        statements
    except ExceptionName:
        statements'''

Num=100
print("Program Execution Begins")
print(Num)
try:
    print(Num/0)
except ZeroDivisionError:
    print("Dividing with Zero Gives an Infinite values")
print("program Execution  Ends")