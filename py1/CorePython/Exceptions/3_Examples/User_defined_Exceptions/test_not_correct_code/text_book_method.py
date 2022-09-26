class MyException(Exception):
    def __int__(self, arg):
        self.msg = arg

    def check(dict):
        for k, v in dict.items():
            print("Name: {}  Balance: {} ".format(k, v))
            if (v < 2000):
                raise MyException('Balance less than 2000 for ' + k)

    bank = {"Name1": 10000, "Name2": 2500, "Name3": 1000, "Name4": 5000, "Name5": 500, "Name6": 7000}


try:
    check(bank)
except MyException as me:
    print(me)
