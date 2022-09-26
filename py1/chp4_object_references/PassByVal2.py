# trying pass by value

f = [14, 23, 37]

print("initially f is : ", f)


def fxn(g):
    k = g  # k is pointing to the original copy
    g = [17, 28, 45]
    print("k inside the function is :", k)
    print()
    print("g inside the function is : ", g)
    print()


fxn(f)

print("after fxn , f is : ", f)