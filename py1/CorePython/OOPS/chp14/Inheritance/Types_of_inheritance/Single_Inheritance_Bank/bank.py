class Bank(object):
    cash = 1000  # class variable

    # of super class

    @classmethod
    def available_cash(cls):
        print(cls.cash)

