def square(x):
    counter = 0
    list1 = []
    while counter <= x - 1:
        list1.append(counter)
        counter += 1

    counter = 0
    while counter <= x - 1:

        for item in list1:
            print(item, end=" ")

        temp = list1[0]
        list1.pop(0)
        list1.append(temp)
        print()
        counter += 1


def main():
    print("Enter the number of rows or columns:")
    num = int(input())

    square(num)


if __name__ == "__main__":
    main()
