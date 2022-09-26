from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, registration_no):
        self.registration_no = registration_no

    def open_tank(self):
        print("Opening tank with the same mechanism in all cars")
        print("Filling the fuel in car number : ", self.registration_no)

    @abstractmethod  # different steering mechanism in different cars
    def steering(self):
        pass

    @abstractmethod  # different braking mechanism in different cars
    def braking(self):
        pass

# all cars can steer : this is why steering method is in super class
# steering mechanism is different for different cars : this is why steering is an abstract method

# all cars have fuel tank : this is why open_tank method is in super class
# open_tank mechanism is same for all cars : this is why open_tank is a concrete method

# abstract class can cater the common needs as well as individual needs of objects
# open_tank : common need
# steering and braking : individual need : since mechanism is diff for diff cars
