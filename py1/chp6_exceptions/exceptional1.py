"""A module for demonstrating exceptions"""


def convert(s):
    """Convert to an integer"""

    try:
        x = int(s)
        print("Conversion successful ! x = ", x)

    except ValueError:
        print("Conversion Failed")
        x = -1

    except TypeError:
        print("Conversion failed")
        x = -1

    print("Normal execution of the program continues here")
    return x
