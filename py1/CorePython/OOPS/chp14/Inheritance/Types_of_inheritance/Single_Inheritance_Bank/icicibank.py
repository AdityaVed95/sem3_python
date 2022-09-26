from bank import Bank


class Icicibank(Bank):
    pass


i1 = Icicibank()
i1.available_cash()
i1.cash = 10
Bank.cash = 100
print(i1.cash)
print(Bank.cash)
