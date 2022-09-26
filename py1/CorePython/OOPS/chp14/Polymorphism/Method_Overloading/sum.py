class Sum:
    # create the below method as a static method by adding @staticmethod decorator above it
    # just remove the self argument if you make it a static method

    def summation(self, no1=None, no2=None, no3=None):  # overloaded method

        if no1 is not None and no2 != None and no3 != None:
            print("The sum of 3 numbers are : ", no1 + no2 + no3)
            # "no1 != None" is equivalent to : "no1 is not None"

        elif no1 is not None and no2 != None:
            print("The sum of 2 numbers are : ", no1 + no2)

        else:
            print("please enter 2 or 3 arguments")


def summation2(no1=None, no2=None, no3=None):  # overloaded function

    if no1 is not None and no2 != None and no3 != None:
        print("The sum of 3 numbers are : ", no1 + no2 + no3)
        # "no1 != None" is equivalent to : "no1 is not None"

    elif no1 is not None and no2 != None:
        print("The sum of 2 numbers are : ", no1 + no2)

    else:
        print("please enter 2 or 3 arguments")


s1 = Sum()
s1.summation(20, 30)

s2 = Sum()
s2.summation(100, 1000, 400)

summation2(20, 30)
summation2(100, 1000, 400)

# achieving method overloading.py with instance method of a class or just a normal function
