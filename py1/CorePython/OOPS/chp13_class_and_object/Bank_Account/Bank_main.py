import sys
from Account_main import Account
from pprint import pprint as pp


class Bank:
    account_dictionary = {}

    def start1(self):
        while True:
            pp("Enter "
               "a to Add/Create account "
               "l to list existing accounts "
               "t to transact with existing accounts "
               "e to exit handling of accounts")

            self.choice_account = input()

            if self.choice_account == "a" or self.choice_account == "A":
                acc1 = Account()
                ident = acc1.add_account()
                Bank.account_dictionary.update({ident: acc1})
                # cls.account_dictionary.update({ident: acc1})

            if self.choice_account == "l" or self.choice_account == "L":
                for key, value in Bank.account_dictionary.items():
                    # val
                    bal = value.balance
                    nam = value.name
                    print("id: {}   Name: {}   Balance: {}".format(key, nam, bal))

            if self.choice_account == "t" or self.choice_account == "T":

                while True:

                    print("Enter y to continue and n to exit transactions with existing accounts  ")
                    ch = input()

                    if ch == "n" or ch == "N":
                        break

                    print("Enter the id of the account you want to transact with: ")
                    ident_trans = int(input())

                    acc2 = Bank.account_dictionary[ident_trans]

                    pp("Enter w to withdraw from account "
                       "d for depositing in account "
                       "v for viewing the account"
                       "e for exiting transactions with existing accounts ")
                    choice = input()

                    if choice == "w" or choice == "W":
                        print("Enter the amount you want to withdraw :")
                        amt1 = int(input())
                        acc2.withdraw(ident_trans, amt1)

                    if choice == "d" or choice == "D":
                        print("Enter the amount you want to deposit :")
                        amt2 = int(input())
                        acc2.deposit(ident_trans, amt2)

                    if choice == "v" or choice == "V":
                        acc2.view(ident_trans)

                    if choice == "e" or choice == "E":
                        break

            if self.choice_account == "e" or self.choice_account == "E":
                sys.exit()

    def search_account_by_name(self):
        pass

    def transfer_between_two_accounts(self):
        pass


HDFC = Bank()
print("To handle accounts : press a")
res = input()

if res == "a" or res == "A":
    HDFC.start1()
