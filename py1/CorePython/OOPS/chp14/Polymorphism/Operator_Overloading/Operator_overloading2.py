class Employee:
    def __init__(self, name, daily_salary):
        self.name = name
        self.daily_salary = daily_salary

    def __mul__(self, other):
        return self.daily_salary * other.no_of_days_worked


class Attendance:
    def __init__(self, name, no_of_days_worked):
        self.name = name
        self.no_of_days_worked = no_of_days_worked


e1 = Employee("Aditya", 10000)
a1 = Attendance("Aditya", 22)

print("The final income for the month is : ", e1 * a1)
