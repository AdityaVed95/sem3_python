from queues import Queues
import sys

q1 = Queues()

choice = "1"

while choice != "6":
    print("1 to check if queue is empty")
    print("2 to add an element at the bottom of queue")
    print("3 to remove an element from the top of queue")
    print("4 to search for position of an element from the top of que")
    # top is front is 0th element of the list and bottom is rear is the last
    # element of the list
    print('5 to display queue from top to bottom : from front to rear')
    print("6 to exit the program")

    choice = input()

    if choice == '1':
        ans = q1.isempty()
        print(ans)

    elif choice == "2":
        print("Enter the element to be inserted at the bottom of the queue")
        # or at the end of the list
        element = input()
        q1.add(element)
        print("successfully inserted {} at the bottom of the queue ".format(element))

    elif choice == "3":
        removed_element = q1.delete()
        print("removed element from the top of queue is : ", removed_element)

    elif choice == "4":
        print("Enter the element whose position is to be searched")
        element = input()

        ans = q1.search(element)

        if ans == -1:
            print("The queue is empty")

        if ans == -2:
            print("The entered element doesnt exist inside the queue")

        else:
            print("The position of the element in queue from the top of queue is : ", ans)


    elif choice == "5":
        display_que = q1.display()
        print(display_que)


    elif choice == "6":
        print("Exiting")
        sys.exit()

    else:
        print("Invalid Input")
        print("Please try again")
