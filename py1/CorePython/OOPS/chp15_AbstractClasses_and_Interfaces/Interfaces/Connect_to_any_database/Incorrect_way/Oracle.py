from Main import MyClass


class Oracle(MyClass):
    def connect(self):
        print("Connecting to Oracle Database")

    def disconnect(self):
        print("Disconnecting from Oracle Database")
