# proving mutability of list and immutability of int data types


def fxn1(x):
    x = 100
    print("x in fxn1 is ", x)


def fxn2(x: list):
    x.append(5)  # note : assigning x to a completely new list will not cause a change in the original z
    print("x in fxn2 is ", x)


y = 50
z = [2, 3, 4]

print("initially y is ", y)
print("initially z is", z)

fxn1(y)
fxn2(z)

print("after fxn call y is ", y)
print("after fxn call z is", z)

print()
print("trying different :")

fxn1(z)

print("z is unchanged : ", z)
