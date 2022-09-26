print("Enter the length")
length = int(input())
print("Enter the breadth")
breadth = int(input())

k = 1

i = 0

while i <= (breadth - 1):
    j = 0
    while j <= (length - 1):
        print(k, end="")
        k += 1
        j += 1
    i += 1
    print()
