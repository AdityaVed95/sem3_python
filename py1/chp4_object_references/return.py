def f(d):
    return d


c = [6, 8, 10]
g = f(c)

print(g is c)

x = 100
y = f(x)

print(y is x)
