from abc import ABC, abstractmethod


class InternationalCreditCard(ABC):
    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass


class BankAccount(InternationalCreditCard):
    def withdraw(self):
        print("here we can withdraw in rupees, dollars or pounds")

    def deposit(self):
        print("here we can deposit in rupees, dollars or pounds")

# interfaces is to describe and deal with behaviour(methods) and not attributes(variables)
# abstract classes consists of only abstract methods and no concrete methods
