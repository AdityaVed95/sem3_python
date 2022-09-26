class A(object):
    def __init__(self):
        self.a = "a"
        print(self.a)
        super().__init__()


class B(object):
    def __init__(self):
        self.b = "b"
        print(self.b)
        super().__init__()


class D(object):
    def __init__(self):
        self.d = "d"
        print(self.d)
        super().__init__()


class E(object):
    def __init__(self):
        self.e = "e"
        print(self.e)
        super().__init__()


class C(A, B, D, E):
    def __init__(self):
        self.c = "c"
        print(self.c)
        super().__init__()


obj1 = C()

# printing the order in which the members are searched from left to right
x = C.mro()
print(x)
