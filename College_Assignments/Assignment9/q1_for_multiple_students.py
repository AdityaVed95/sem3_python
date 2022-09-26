class RegistrationException(Exception):
    # def __init__(self, arg):
    #     self.msg = arg
    # the above two lines are not affecting the behaviour of the program
    pass


def check(age, weight):
    if age >= 12 or weight >= 40:
        raise RegistrationException("Student is not eligible for registration")


def main():
    print("Welcome to the Registration Portal")

    while True:
        print()
        print("Enter 1 to check registration eligibility of student ")
        print("Enter 2 to exit the program")
        response1 = int(input())

        if response1 == 1:
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

            finally:
                print("Eligibility check for current student is completed")

        elif response1 == 2:
            break
        else:
            print("Invalid input")
            print("Please Try again")


if __name__ == "__main__":
    main()
