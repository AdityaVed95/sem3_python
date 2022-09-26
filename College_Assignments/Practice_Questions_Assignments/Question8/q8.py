print("Enter number of rows: ")
n = int(input())

i = 0
while i <= n - 1:
    j = 0

    while j <= i + 1:
        print(j, end=" ")
        j += 1

    i += 1
    print()
