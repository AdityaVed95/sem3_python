import copy

x = 5
y = copy.deepcopy(x)
m = copy.copy(x)
print(id(m))
print(id(x))
print(id(y))

z = [43, 432, 53245, 45, 432]
a = copy.copy(z)
b = z
print(id(a))
print(id(z))
print(id(b))
