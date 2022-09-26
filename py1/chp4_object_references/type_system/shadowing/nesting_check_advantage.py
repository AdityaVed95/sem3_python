x = 5


def main():
    x = 10
    print(x)
    y = 10

    while y == 10:
        x = 20
        print(x)
        z = 10

        while z == 10:
            print(x)
            z += 1

        y += 1

    print(x)


if __name__ == "__main__":
    main()

print(x)
