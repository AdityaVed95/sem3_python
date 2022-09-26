class A:
    def __init__(self):
        super.__init__()
        print("i am in class A")


class B:
    def __init__(self):
        print("i am in class B")


class C:
    def __init__(self):
        print("i am in class C")


class D(A, B, C):
    def __init__(self):
        print("I am in class D")
        A.__init__(self)


d1 = D()
