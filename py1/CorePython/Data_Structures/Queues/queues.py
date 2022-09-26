# creating a class as a true service which is callable from both cui
# and gui interface


class Queues:
    def __init__(self):
        self.que = []

    def isempty(self):
        return self.que == []

    def add(self, element):
        self.que.append(element)

    def delete(self):
        return self.que.pop(0)

    def search(self, element):  # searching performed from the top to bottom of que
        # from the front to rear [0,1,2,3,4,5,6]
        # from 0 to end
        if self.isempty() == True:
            return -1
        else:
            try:
                position = self.que.index(element)
                return position + 1
            except ValueError:
                return -2

    def display(self):
        return self.que
