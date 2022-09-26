class A:
    a = 12
    b = 123

    def method1(self):
        print(self.a)
        print(self.b)


class B(A):
    c = 1234

    def method2(self):
        print(self.c)
        self.method1()
        print(self.a)
        print(self.b)


# b1 = B()
# b1.method1()
# b1.method2()
# print(b1.a)
# print(b1.b)
# print(b1.c)

b1 = B()
a1 = A()

print(b1.a)
b1.a = 100
print(b1.a)

a1.a = 500
print(a1.a)
print(b1.a)

print(id(b1.a) == id(a1.a))

b2 = B()
b2.a = 1000
print(b2.a)

a2 = A()
a2.a = 90
print(a2.a)

print(b1.a)
print(a1.a)
