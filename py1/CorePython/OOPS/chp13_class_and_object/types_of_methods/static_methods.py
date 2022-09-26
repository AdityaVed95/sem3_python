class ClassName:
    n = 0

    def __init__(self):
        ClassName.n += 1

    @staticmethod
    def NoOfObjects():
        print("No of instances/objects created are : ", ClassName.n)


obj1 = ClassName()
obj2 = ClassName()
obj3 = ClassName()

ClassName.NoOfObjects()
