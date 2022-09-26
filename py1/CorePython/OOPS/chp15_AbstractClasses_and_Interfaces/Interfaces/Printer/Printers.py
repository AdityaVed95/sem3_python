from abc import *


class Printer(ABC):
    @abstractmethod
    def printit(self, text):
        pass

    def disconnect(self):
        pass


class IBM(Printer):
    def printit(self, text):
        print(text)

    def disconnect(self):
        print("Printing done on IBM ")


class Epson(Printer):
    def printit(self, text):
        print(text)

    def disconnect(self):
        print("Printing done on Epson ")


class UsePrinter:
    with open("config.txt", "r") as f:
        str = f.readline()

    # str = Epson or IBM

    classname = globals()[str]

    x = classname()

    x.printit("Hello , this is sent to the printer")
    x.disconnect()
