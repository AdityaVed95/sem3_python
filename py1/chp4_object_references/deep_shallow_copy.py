import copy

x = [1, 2, 3, 4, 5]
y = copy.deepcopy(x)
print(id(x))
print(id(y))

z = x
print(id(x))

x[0] = 12
print(x)
print(z)
print(id(z))
print(id(x))

print(y)
print(id(y))

print("-----------------------------------------------------")

x = [20, 30, 40]
print(id(x))
print(z)
print(id(z))
