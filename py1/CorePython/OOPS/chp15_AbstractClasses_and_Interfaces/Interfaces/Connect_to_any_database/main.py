from abc import ABC, abstractmethod


class MyClass(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class Oracle(MyClass):
    def connect(self):
        print("Connecting to Oracle Database")

    def disconnect(self):
        print("Disconnecting from Oracle Database")


class Sybase(MyClass):
    def connect(self):
        print("Connecting to Sybase Database")

    def disconnect(self):
        print("Disconnecting from Sybase Database")


class Database:
    print("Enter database name : ")
    str = input()

    classname = globals()[str]

    x = classname()

    x.connect()
    x.disconnect()
