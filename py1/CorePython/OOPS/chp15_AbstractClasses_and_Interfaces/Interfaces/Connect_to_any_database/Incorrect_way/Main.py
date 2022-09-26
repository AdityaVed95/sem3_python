from abc import ABC, abstractmethod


class MyClass(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class Database:
    print("Enter database name : ")
    str = input()

    classname = globals()[str]

    x = classname()

    x.connect()
    x.disconnect()
