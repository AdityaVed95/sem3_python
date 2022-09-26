def divide(nume, deno):
    try:
        quo = nume / deno
        print("quo is : ", quo)

    except ZeroDivisionError:
        print("You cannot divide a number by 0")

    print("Normal execution continues here irrespective of whether exception occurred")


def main():
    print("Case1 :")
    divide(10, 20)

    print()
    print("Case2: ")
    divide(10, 0)


if __name__ == "__main__":
    main()
