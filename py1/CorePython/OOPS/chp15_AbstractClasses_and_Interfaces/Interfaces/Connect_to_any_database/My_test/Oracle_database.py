# subclass of the Super class , to connect specially to the Oracle database

from CorePython.OOPS.chp15_AbstractClasses_and_Interfaces.Interfaces.Connect_to_any_database.My_test.Common_database_code import \
    CommonDatabase


class OracleDatabase(CommonDatabase):
    def connect(self):
        print("Connecting to Oracle Database")

    def disconnect(self):
        print("Disconnecting from Oracle Database")


Connection1 = OracleDatabase()
Connection1.connect()
Connection1.disconnect()
