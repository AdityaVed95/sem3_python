"""Model for aircraft flights."""


# SN060 is valid number : SN is the airline code and 060 is the route number

class Flight:

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No Airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid Airline code in '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number in '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]  # return just the airline code.

    def aircraft_model(self):
        return self._aircraft.model()  # here we are accessing the method of another class


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])  # a tuple is returned

#
# f = Flight("3s060")  # f is an object of class Flight
#
# print(f.number())
# print(Flight.number(f))
# print(f._number)
