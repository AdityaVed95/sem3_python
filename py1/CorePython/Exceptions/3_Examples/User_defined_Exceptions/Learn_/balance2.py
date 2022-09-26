class BalanceException(Exception):
    pass

    # the below statements are optional
    # def __int__(self, arg):
    #     self.msg = arg


def checkbalance():
    money = 10000
    withdraw = 9000
    balance = money - withdraw

    if balance <= 2000:
        raise BalanceException('Insufficient Balance')

    print(balance)


try:
    checkbalance()

except BalanceException as be:
    print(be)
