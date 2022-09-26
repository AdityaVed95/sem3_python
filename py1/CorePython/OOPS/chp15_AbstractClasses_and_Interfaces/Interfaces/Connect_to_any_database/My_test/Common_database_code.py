# common super class for connecting to any database in the world
# this is an INTERFACE : with only abstract methods

from abc import ABC, abstractmethod


class CommonDatabase(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass
