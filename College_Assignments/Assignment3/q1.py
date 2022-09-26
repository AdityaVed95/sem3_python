def is_prime(n):
    counter = 0

    if n <= 1:
        return False

    i = 1

    while i <= (n / 2):

        if n % i == 0:
            counter += 1

        i += 1

    if counter == 1:
        return True

    else:
        return False


def main():
    no_of_prime = 0
    no_of_composite = 0

    j = 1

    while True:
        print("For the {}th iteration , please enter a number".format(j))
        num = int(input())

        if num == -1:
            break

        ans = is_prime(num)

        if ans:
            no_of_prime += 1
        else:
            no_of_composite += 1

        j += 1

    print("Number of Prime Numbers are :", no_of_prime)
    print("Number of Composite Numbers are : ", no_of_composite)


if __name__ == '__main__':
    main()
