class Account:
    def __init__(self, name, number, type_acc, balance):
        self.account_name = name
        self.account_number = number
        self.account_type = type_acc
        self.account_balance = balance

    def display_all_info(self):
        print("Account Name: ", self.account_name)
        print("Account Number: ", self.account_number)
        print("Account Type: ", self.account_type)
        print("Account Balance: ", self.account_balance)

    def check_balance(self):
        if self.account_balance <= 500:
            self.account_balance = self.account_balance - 0.02 * self.account_balance


class CurrentAccount(Account):
    def __init__(self, name, number, type_acc, balance):
        Account.__init__(self, name, number, type_acc, balance)

    def accepting_deposit(self):
        print("Enter the amount to be deposited in account")
        amount = float(input())
        self.account_balance = self.account_balance + amount
        self.check_balance()

    def withdrawing(self):
        print("Enter amount to be withdrawn")
        withdraw = float(input())
        if self.account_balance - withdraw >= 0:
            self.account_balance = self.account_balance - withdraw
        else:
            print("insufficient balance , try again later")

        self.check_balance()

    # provides cheque book facility but no interest


class SavingAccount(Account):
    def __init__(self, name, number, type_acc, balance, time):
        self.rate_of_interest = 5
        self.time = time  # time in years
        Account.__init__(self, name, number, type_acc, balance)

    # provides simple interest and withdrawal facilities but no cheque book facility
    def interest_calculation_and_displaying(self):
        self.check_balance()
        interest = (self.account_balance * self.rate_of_interest * self.time) / 100
        print("Interest calculated is: ", interest)


print("Creating two accounts :")
print("Account1 ::  name:name1, number:100, type:'current', balance:1000")
print("Account2 ::  name:name2, number:200, type:'saving', balance:2000, time:5")
acc1 = CurrentAccount("name1", 100, "current", 1000)
acc2 = SavingAccount("name2", 200, "saving", 2000, 5)

acc1.check_balance()
acc2.check_balance()

while True:
    print("Enter 1 to deal with 1st account")
    print("Enter 2 to deal with 2nd account")
    print("Enter 3 to exit program")
    response1 = int(input())

    if response1 == 1:
        while True:
            print("Enter 1 to deposit")
            print("Enter 2 to withdraw")
            print("Enter 3 to display all information")
            print("Enter 4 to exit account1")
            response2 = int(input())

            if response2 == 1:
                acc1.accepting_deposit()
            elif response2 == 2:
                acc1.withdrawing()
            elif response2 == 3:
                acc1.display_all_info()
            elif response2 == 4:
                break
            else:
                print("invalid input")
                continue

    elif response1 == 2:

        while True:
            print("Enter 1 to calculate and display interest")
            print("Enter 2 to display all information")
            print("Enter 3 to exit account2")
            response2 = int(input())

            if response2 == 1:
                acc2.interest_calculation_and_displaying()

            elif response2 == 2:
                acc2.display_all_info()

            elif response2 == 3:
                break

            else:
                print("invalid input")
                continue

    elif response1 == 3:
        break

    else:
        print("invalid input")
        continue
