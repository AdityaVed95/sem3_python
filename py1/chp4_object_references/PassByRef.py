# m is passed by ref

m = [9, 15, 24]
print("initially m is : ", m)


def modify(k):
    k.append(39)
    print("k inside function is : ", k)


modify(m)

print("after modify , m is : ", m)
