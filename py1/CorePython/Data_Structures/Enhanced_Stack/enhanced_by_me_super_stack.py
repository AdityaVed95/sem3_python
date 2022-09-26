# push pop peep search

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    # note that the push , pop and peep operations happen only fom the top of stack

    def push(self, element):
        self.stack.append(element)

    def pop_tos(self):
        if self.isEmpty():
            return -1  # stack is empty thus cannot pop
        else:
            return self.stack.pop()  # pop the element on the tos i.e. the last element of the list

    # in case the same element is at multiple places in the stack
    # we can pop that element while searching from bos ( pop_1st_from_bos ) or
    # while searching from tos (pop_1st_from_tos)
    # or we can pop all those elements from the stack (pop_all_occurrences_of_given_element)

    def pop_1st_from_bos(self, element):
        if self.isEmpty():
            return -1

        else:
            self.stack.remove(element)
            # remove function starts searching from the bos , 0th element and when it finds that element , it
            # stops there
            # and returns its positon without going all the way upto the tos

    def pop_1st_from_tos(self, element):
        position = None
        for iterator in range(len(self.stack) - 1, 0, -1):
            if self.stack[iterator] == element:
                position = iterator
                break

        self.stack.pop(position)  # pops the element at the specified position

    def pop_all_occurrences_of_given_element(self, element):
        positions = []

        for iterator in range(0, len(self.stack) - 1, 1):  # start,stop,step
            if self.stack[iterator] == element:
                positions.append(iterator)

        for position in positions:
            self.stack.pop(position)

    # peep means returning the top most element without removing it from the stack
    # but i have made peep for both tos and bos

    def peep_TOS(self):  # TOS is top of stack
        n = len(self.stack)

        if n != 0:
            return self.stack[n - 1]
        else:
            return -1

    def peep_BOS(self):
        n = len(self.stack)

        if n != 0:
            return self.stack[0]
        else:
            return -1

    # searching means knowing the position of the element in the stack ** from the tos **  ===> original definition
    # of searching
    # thus searching will not give us the [ position of the element in the list (i.e. num) ]
    # as the position of the elements of the list grows from bos to tos from 0 to len(stack) - 1
    # searching will give us the len(stack) - num and this position that we get from the tos will be 1 index based
    # and not zero index based

    def search_from_TOS(self, element):
        # note : here the position that we calculate is from bos {zero based index from the bottom of stack}

        position = None
        for iterator in range((len(self.stack) - 1), 0, -1):
            if self.stack[iterator] == element:
                position = iterator
                break

        if position is not None:
            return len(self.stack) - position
        else:
            return -1

    def search_from_BOS(self, element):  # bottom of stack
        if self.isEmpty():
            return -1  # stack is empty

        else:

            try:
                num = self.stack.index(element)
                return len(self.stack) - num  # zero based index

            except ValueError:
                return -2  # number not found

    def search_all_positions_of_element(self, element):
        positions = []

        for iterator in range(0, len(self.stack) - 1, 1):
            if self.stack[iterator] == element:
                positions.append(iterator)

        positions_final = []

        for position in positions:
            positions_final.append(len(self.stack) - position)

        return positions_final

    def display(self):
        return self.stack
