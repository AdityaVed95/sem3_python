# clerk not having access to the loan amount


class Bank(object):

    def __init__(self):
        self.accno = 10
        self.name = "Ram"
        self.balance = 5000
        self.__loan = 15 * (10 ** 5)

    def display(self):
        print(self.accno)
        print(self.name)
        print(self.balance)
        # this will generate error : print(self.loan)


b1 = Bank()

# two ways to achieve the same thing

Bank.display(b1)
b1.display()
