import sys


class Bank:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Successfully deposited ₹{}  in your account".format(amount))

    def withdraw(self, amount):

        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            print("Successfully withdrawn ₹{}  from your account".format(amount))
        else:
            print("Cannot withdrawn more than your balance account :")
            print("You can withdraw maximum of : ₹{}".format(self.balance))
            print("Please try again : ")

    def view(self):
        print(self.balance)


print("Enter the name of the Customer : ")
name1 = input()

print("Enter the balance amount of the account : ")
balance1 = int(input())

b1 = Bank(name1, balance1)

while True:
    choice = input("Input : d=Deposit , w=Withdraw , e=Exit , v=View Balance    ")

    if choice == "e" or choice == "E":
        print("The final balance amount in the account of {} is : {} ".format(b1.name, b1.balance))
        sys.exit()
        # exit is a helper for the interactive shell - sys.exit is intended for use in programs.

    if choice == "d" or choice == "D":
        print("Enter the amount to be deposited : ")
        amt_dep = int(input())
        b1.deposit(amt_dep)

    if choice == "w" or choice == "W":
        print("Enter the amount to be withdrawn :")
        amt_with = int(input())
        b1.withdraw(amt_with)

    if choice == "v" or choice == "V":
        b1.view()
