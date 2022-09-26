# subclass of the Super class , to connect specially to the Sybase database

from CorePython.OOPS.chp15_AbstractClasses_and_Interfaces.Interfaces.Connect_to_any_database.My_test.Common_database_code import \
    CommonDatabase


class SybaseDatabase(CommonDatabase):
    def connect(self):
        print("Connecting to Sybase Database")

    def disconnect(self):
        print("Disconnecting from Sybase Database")


Connection1 = SybaseDatabase()
Connection1.connect()
Connection1.disconnect()
