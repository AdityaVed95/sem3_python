from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def speed(self):
        pass


class FourWheeler(Vehicle):
    def __init__(self, name, speeds):
        self.speeds = speeds
        self.name = name

    def speed(self):
        print("The Name of the Vehicle is: ", self.name)
        print("The speed of the vehicle is: ", self.speeds)


class TwoWheeler(Vehicle):
    def __init__(self, name, speeds):
        self.speeds = speeds
        self.name = name

    def speed(self):
        print("The Name of the Vehicle is: ", self.name)
        print("The speed of the vehicle is: ", self.speeds)


f1 = FourWheeler("CIVIC", 100)
t1 = TwoWheeler("PULSAR", 55)
f1.speed()
print("\n")
t1.speed()
