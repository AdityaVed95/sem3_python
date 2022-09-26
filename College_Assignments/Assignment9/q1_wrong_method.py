class RegistrationException(Exception):
    def __init__(self):
        print("Student is not eligible for registration")


def checking_registration():
    print("Input the age of the student")
    age = int(input())

    print("Input weight of student")
    weight = float(input())

    if age < 12 and weight < 40:
        print("Hurray you can register")

    else:
        raise RegistrationException


while True:
    print("Enter 1 to check registration eligibility of student ")
    print("Enter 2 to exit the program")
    response1 = int(input())

    if response1 == 1:
        checking_registration()

    elif response1 == 2:
        break
    else:
        print("Invalid input")
        print("Please Try again")
