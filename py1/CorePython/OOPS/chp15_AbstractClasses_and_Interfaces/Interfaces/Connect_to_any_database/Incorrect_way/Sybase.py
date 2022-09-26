from Main import MyClass


class Sybase(MyClass):
    def connect(self):
        print("Connecting to Sybase Database")

    def disconnect(self):
        print("Disconnecting from Sybase Database")
