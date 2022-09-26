class BalanceException(Exception):
    pass


def checkbalance():
    money = 10000
    withdraw = 9000

    # whenever we have a doubt that in this part of the code an exception can occur
    # we should put that part of the code in the try block

    try:
        balance = money - withdraw
        if balance <= 2000:
            raise BalanceException('Insufficient Balance')
            # here 'Insufficient Balance' is a message
        print(balance)

    except BalanceException as be:
        print(be)
        # here be is an object
        # the message that we write is passed to the be object


checkbalance()

print("Normal execution continues here")
# the same code can be written in a different way like in balance2.py
