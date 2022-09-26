import sys
from collections import deque

de1 = deque([])  # creating an empty deque

choice = "0"

while choice != "8":
    print("1 to add element at the front")
    print("2 to remove element at the front")
    print("3 to add element at the rear")
    print("4 to remove element at the rear")
    print("5 to remove element in the middle")
    print("6 to count number of occurrences of an element")
    print("7 to display")
    print("8 to exit")

    choice = input()

    if choice == "1":
        print("Enter the element to be appended at front")
        element = input()
        de1.appendleft(element)

    elif choice == "2":
        de1.popleft()

    elif choice == "3":
        print("Enter the element to be appended at rear")
        element = input()
        de1.append(element)

    elif choice == "4":
        de1.pop()

    elif choice == "5":
        print("Enter the element to be removed")
        element = input()
        try:
            de1.remove(element)
        except ValueError:
            print("Element not found")



    elif choice == "6":
        print("Enter the element that you want to count")
        element = input()
        num = de1.count(element)
        print("Number of times the element was found in the deque : ", num)

    elif choice == "7":
        print(de1)

    elif choice == "8":
        print("Exiting")
        sys.exit()

    else:
        print("invalid input , try again")
