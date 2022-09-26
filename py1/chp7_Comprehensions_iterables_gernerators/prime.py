#!/home/aditya/miniconda3/envs/py3.10/bin/python

from pprint import pprint as pp

dummy = "i am global"


def main():
    print("input the range starting value:")
    _ = input()
    start = int(_)
    print("input the range ending value")
    _ = input()
    stop = int(_)

    print_prime_nos(start, stop)
    print_prime_square_divisors(start, stop)
    temp()


def is_prime(num):
    if num < 0:
        return False

    elif num == 0 or num == 1:
        return False

    counter = 0

    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1

    if counter == 2:
        return True
    else:
        return False


def print_prime_nos(start, stop):
    prime_nos = "dummy"  # just for the sake of declaration to avoid confusion in variable scoping

    # solving optimization issues :

    if start > 0:
        prime_nos = [i for i in range(start, stop + 1) if is_prime(i)]

    if start < 0:
        prime_nos = [i for i in range(0, stop + 1) if is_prime(i)]

    # so that if someone enters a huge negative value then it wont have performance impact on the program

    print("The list of all the prime numbers in the given range including endpoints are:")
    print(prime_nos)


def print_prime_square_divisors(start, stop):
    prime_square_divisors = "dummy"

    if start > 0:
        prime_square_divisors = {i * i: (1, i, i * i) for i in range(start, stop + 1) if is_prime(i)}

    if start < 0:
        prime_square_divisors = {i * i: (1, i, i * i) for i in range(0, stop + 1) if is_prime(i)}

    print("All the prime square divisors are :")
    pp(prime_square_divisors)


def temp():
    global dummy
    dummy = "i changed the global"
    print(dummy)


# fun is in putting the cursor on the dummy variable and seeing its value in different parts of the program
# useful when using a local variable with the same name as that of the global variable


print(dummy)

if __name__ == "__main__":
    main()

    # logic 2 : for prime nos calculation : logic with less computation
    #
    # for i in range(1, (num // 2) + 1):
    #     if num % i == 0:
    #         counter += 1
    #
    # if counter == 1:
    #     return True
    # else:
    #     return False
