def matrix(r, c):
    row_counter = 0
    column_counter = 0
    i = 1
    while row_counter <= r - 1:

        while column_counter <= c - 1:
            print(i, end=" ")
            i += 1
            column_counter += 1

        print()
        row_counter += 1
        column_counter = 0


def main():
    print("Enter the number of rows :")
    rows = int(input())

    print("Enter the number of columns: ")
    columns = int(input())

    matrix(rows, columns)


if __name__ == "__main__":
    main()
