#OOP_Programming_Challenge

'''#Create a bank account that has 2 attributes:
# 1. Owner
# 2. Balance

#Also 2 Deposit Methods:
# 1. Deposit
# 2. Withdraw
# Withdrawels may not exceed availible balance

class Acount:
    pass

#Instantiate the class 
#acct1 = Account('Jose',100)

#2. Print the obhject 'str'
#print(acct1)

show account owner Attribute
account1.owner
#"Jose"

#4. Show account balance 
acct1.balance

5. Make a series of Deposits and withdrawls
acc1. deposit(50)

Deposit Accepted

acct1.withdraw(75)
Withdrawel Accepted

#6.MAke a withdrawel that exceeds the availible balance
'''
#Calling methods that affect attributes

class Simple():

    def __init__(self,value):
        self.value = value

    def add_to_value(self,amount):
        self.value = self.value + amount

myobj = Simple(300)
print(myobj.value)

myobj.add_to_value(500)

print(myobj.value)

class Account():
    
    ''''This is information of the Account Owner and
        the Balance they have in their account'''

    def __init__(self, owner,balance=0):
        
        self.owner =    owner
        self.balance =  balance

    def deposit(self,dep_amt):

        self.balance = self.balance + dep_amt

        print(f"the amount in this account is {self.balance}")

    def withdrawal(self,wd_amt):
            
            if self.balance >= wd_amt:
                self.balance = self.balance - wd_amt
                print("Withdrawel Accepted")

            else:
                
                print("Sorry not Enough Funds!")
    def __str__(self):

            return f"Owner: {self.owner} \nBalance: {self.balance}"


acct1 = Account("Jose",200)

print(acct1.balance)
print(acct1.owner)
print(acct1.balance)

a = Account("Sam",500)

print(a.owner)
print(a.balance)
a.deposit(100)

print(a)
a.withdrawal(600)
print(a)
a.withdrawal(40)
print(a)