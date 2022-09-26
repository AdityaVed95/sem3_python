# trying pass by value here , thinking that k will hold the copy of original and then modifying g wont change k , but
# that didnt happen

f = [14, 23, 37]

print("initially f is : ", f)


def fxn(g):
    k = g
    g[0] = 17
    g[1] = 28
    g[2] = 45
    print("k inside the function is :", k)
    print()
    print("g inside the function is : ", g)
    print()


fxn(f)

print("after fxn , f is : ", f)
