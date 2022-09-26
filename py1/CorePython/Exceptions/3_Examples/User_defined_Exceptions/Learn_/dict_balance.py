class BalanceException(Exception):
    pass


Accounts = {}


def checkbalance():
    for name, balance in Accounts.items():
        if balance <= 2000:
            raise BalanceException('Insufficient Balance in the account of ' + name)
        print("Name: {}  Balance: {} ".format(name, balance))


def inputAccounts():
    # print("For creating new accounts with given balance")
    # counter = 0
    # global Accounts
    # while True:
    #     print("Press Y to create new account of N to exit creation of accounts")
    #     choice = input()
    #
    #     if choice == "y" or choice == "Y":
    #         print("Enter the Full name of the account holder")
    #         name = input()
    #         print("Enter the balance in the account")
    #         bal = int(input())
    #         Accounts[name] = bal
    #
    #     else:
    #         break
    #
    #     counter += 1
    global Accounts
    Accounts = {"Name1": 10000, "Name2": 2500, "Name3": 1000, "Name4": 5000, "Name5": 500, "Name6": 7000}


inputAccounts()

try:
    checkbalance()

except BalanceException as be:
    print(be)

# how to print the remaining names after the execution has occurred
