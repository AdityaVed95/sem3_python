class RegistrationException(Exception):
    def __init__(self, arg):
        self.msg = arg


def check(age, weight):
    if age >= 12 or weight >= 40:
        raise RegistrationException("Student is not eligible for registration")


try:
    print("Enter age")
    age = int(input())
    print("Enter weight")
    weight = float(input())
    check(age, weight)

except RegistrationException as reg:
    print(reg)

else:
    print("Hurray , you can register")
