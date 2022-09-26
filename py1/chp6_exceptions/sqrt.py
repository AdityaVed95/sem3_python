def sqrt(x):
    """Compute square roots using the method of Heron of Alexandria.

    Args:
        x: The number for which the square root is to be computed.

    Returns:
        The square root of x."""

    guess = x  # guess will be the square root of x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1

    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("This is never printed")

    except ZeroDivisionError:
        print("Cannot compute sqrt of -ve no")

    print("program execution continues normally here")
    print(sqrt(25))


if __name__ == '__main__':
    main()
