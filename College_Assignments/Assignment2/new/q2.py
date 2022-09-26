list1 = []
list2 = []

while True:
    print("Enter y to continue and n to exit inputting of numbers in list")
    choice = input()

    if choice == "y" or choice == "Y":
        print("Enter the number you want to add to the list")
        num = int(input())
        list1.append(num)

    elif choice == "n" or choice == "N":
        break

    else:
        print("Incorrect Input")

for item in list1:
    if item in list2:
        continue
    else:
        list2.append(item)

print("The list without any duplicates is :")
print(list2)
