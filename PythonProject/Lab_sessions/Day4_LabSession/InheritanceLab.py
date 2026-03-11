#Ques:- cerate a python program with class name savingsaccount and functions deposit in parent class  
# and  addinterest in the child class

class SavingsAcc:
    def __init__(self, acc_num, deposit_amt):
        self.acc_num = acc_num
        self.deposit_amt = deposit_amt
    def deposits(self, amount):
        self.deposit_amt += amount
        print(f"Deposited {amount}. New balance: {self.deposit_amt}")
class SavingsAccWithInterest(SavingsAcc):
    def add_interest(self, interest_rate):
        interest = self.deposit_amt * (interest_rate / 100)
        self.deposit_amt += interest
        print(f"Added interest: {interest}. New balance: {self.deposit_amt}")
# Create an instance of SavingsAccWithInterest
savings_account = SavingsAccWithInterest(acc_num="123456789", deposit_amt=500)
savings_account.deposits(500)  # Deposit money  
savings_account.add_interest(9)  # Add interest at 5% rate

    
    