n1 = 0
n2 = 1
print("Enter number of terms")

num = int(input())

if num < 0:
    print("Invalid input")

elif num == 1:
    print(n1)
elif num == 2:
    print("{} {}".format(n1, n2))

else:

    count = 0
    while count < num:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
