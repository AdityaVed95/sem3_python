class MyException(Exception):
    def __int__(self):
        pass


def check(dictionary1):
    for i, j in dictionary1.items():
        print("Name : {}  ::  Balance : {}".format(i, j))
        if j < 2000:
            raise MyException()


try:
    dict1 = {"Name1": 10000, "Name2": 2500, "Name3": 1000, "Name4": 5000, "Name5": 500, "Name6": 7000}
    check(dict1)

except MyException:
    print("The balance in your account is less than 2000")
