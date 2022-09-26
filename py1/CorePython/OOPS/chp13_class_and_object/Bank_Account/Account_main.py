import sys
import random


class Account:

    def __init__(self):
        pass

    def add_account(self):
        print("Enter the name of the Customer: ")
        self.name = input()
        print("Enter the initial balance amount of the Customer: ")
        self.balance = int(input())
        self.identity = random.randint(10 ** 10, 10 ** 12)
        print("Hello {} , you have been assigned {} as your identity number".format(self.name, self.identity))
        return self.identity

    def view(self, id_):
        nam = self.name
        print("Name : ", nam)
        print("id : ", id_)
        bal = self.balance
        print("Current Balance : ", bal)

    # transaction fxns :
    def deposit(self, id, amount):
        self.balance = self.balance + amount
        print("Successfully deposited ₹{}  in your account".format(amount))

    def withdraw(self, id_, amount):

        # print(id(self.balance) == id(temp_act.balance))

        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            print("Successfully withdrawn ₹{}  from your account".format(amount))
        else:
            print("Cannot withdrawn more than your balance account :")
            print("You can withdraw maximum of : ₹{}".format(self.balance))
            print("Please try again : ")

# def add_account(self):

# if we want to add account :
# if choice_account == "a" or choice_account == "A": then

# acc1 = Account()

# to transact with the account :

# while True:
#     choice = input("Input : d=Deposit , w=Withdraw , e=Exit , v=View Balance    ")
#
#     if choice == "e" or choice == "E":
#         sys.exit()
#
#     if choice == "d" or choice == "D":
#         pass
#
#     if choice == "w" or choice == "W":
#         pass
#
#     if choice == "v" or choice == "V":
#         pass
