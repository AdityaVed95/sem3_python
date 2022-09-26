count = 0


def fxn1():
    count = 5
    print("count 2 in fxn1 is :", count)


def fxn2():
    global count
    count = 10
    print("count 4 is ", count)


print("count 1 is :", count)
fxn1()
print("count 3 is : ", count)
fxn2()
print("count 5 is :", count)
