'''ATM Withdrawal Systen
Scenario:
You're simulating an ATM machine. A user Inputs the amount they want to 
withdraw, Task:
-Raise an error if the amount is more than the account balance
-Also handle non-Integer input gracefully'''

class InsufficientFundsError(Exception): pass
balance=10000
try:
    amount=int(input("Enter amount to withdraw :"))
    if amount<=0:
        raise ValueError("withdrawal amount must be greater than 0")
    if amount>balance:
        raise InsufficientFundsError("Insufficient balance for withdrawal")
    balance-=amount
    print(f"Wthdrawal successful! Remaining balance: {balance}")
except ValueError as ve:
    print("Invalid input:",ve)
except InsufficientFundsError as ie:
    print("Insufficient")