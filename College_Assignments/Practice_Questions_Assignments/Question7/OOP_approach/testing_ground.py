from Pattern1 import Pattern1


def main():
    object1 = Pattern1()
    print("Enter the number of rows or columns:")
    num = int(input())
    object1.square(num)


if __name__ == "__main__":
    main()

