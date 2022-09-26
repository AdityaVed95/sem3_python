import sys

from enhanced_by_me_super_stack import Stack

first_stack = Stack()
# first_stack.isEmpty()
# first_stack.push(10)
# first_stack.push(20)
# first_stack.push(5)
# first_stack.push(100)
# first_stack.push(20)
# first_stack.push(40)
# first_stack.display()

response = 1

while response != "13":
    print("Enter Your Choice ")
    print("1 to check for is empty")
    print("2 to push at tos {original definition of push}")
    print("3 to pop from tos {original definition of pop}")
    print("4 to pop an element by finding from bos to tos")
    print("5 to pop an element by finding from tos to bos")
    print("6 to pop all occurrences of given element")
    print("7 to peep tos {original definition of peep}")
    print("8 to peep bos {to know what is at the bos")
    print("search : meaning to know the position of an element inside the stack from the tos")
    # the same element might be at multiple positions in the stack
    # search from tos to bos means that the we will start seraching for the
    # positon of the element from the tos and then in the process if we get
    # some element above then the positon of that element will be returned,
    # and the same element that might be near the bottom will not get preference
    # as only 1 position is searched for in 9 and also in 10

    print("9 to search from tos to bos ")
    print("10 to search from bos to tos")
    print("11 to search for all positions of an element in the stack")
    print("12 to display stack")
    print("13 to exit")
    response = input()

    if response == "1":
        ans = first_stack.isEmpty()
        print(ans)

    elif response == "2":
        print("Enter the element to be pushed to tos")
        element = input()
        ans = first_stack.push(element)
        if ans == -1:
            print("Enhanced_Stack is empty")
        else:
            print("successfully pushed {} to tos".format(element))


    elif response == "3":
        ans = first_stack.pop_tos()
        if ans == -1:
            print("Enhanced_Stack is empty, No pop possible")
        else:
            print("Successfully poped {} from the tos".format(ans))


    elif response == "4":
        print("Enter the element to be poped out or removed")
        element = input()
        ans = first_stack.pop_1st_from_bos(element)

        if ans == -1:
            print("Enhanced_Stack is empty")
        else:
            print("Successfully poped {} from stack".format(element))



    elif response == "5":
        print("Enter the element to be poped out or removed")
        element = input()
        first_stack.pop_1st_from_tos(element)




    elif response == "6":
        print("Enter the element to be poped out or removed")
        element = input()
        first_stack.pop_all_occurrences_of_given_element(element)

    elif response == "7":
        first_stack.peep_TOS()

    elif response == "8":
        first_stack.peep_BOS()

    elif response == "9":
        print('Enter the element whose position is to be searched')
        element = input()
        position = first_stack.search_from_TOS(element)
        print("the position of the element is : ", position)

    elif response == "10":
        print('Enter the element whose position is to be searched')
        element = input()
        position = first_stack.search_from_BOS(element)
        print("the position of the element is : ", position)

    elif response == "11":
        print('Enter the element whose position is to be searched')
        element = input()
        positions = first_stack.search_all_positions_of_element(element)
        print("positions of the element is : ", positions)


    elif response == "12":
        display_me = first_stack.display()
        print(display_me)

    elif response == "13":
        sys.exit()

    else:
        print("Invalid Input")
