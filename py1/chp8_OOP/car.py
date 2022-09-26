def vehicle():
    print("car")


class Car:

    def __init__(self, brand, number, model, tyre):
        self._brand = brand
        self._number = number
        self._model = model
        self._tyre = tyre
        x = 4  # all the above variables could be accessed by other methods inside the class
        # but x cannot be accessed by other methods inside the class

    def tyre(self):
        print(x)
        return self._tyre

    def brand(self):
        return self._brand

    def number(self):
        return self._number

    def model(self):
        return self._model


c1 = Car("BMW", 4574, "X76", "MRF")

print(c1.brand())
print(c1.number())
print(c1.model())
print(c1.tyre())
