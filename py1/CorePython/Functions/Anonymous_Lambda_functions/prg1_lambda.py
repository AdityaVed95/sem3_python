f1 = lambda x: x * x
val1 = f1(5)
print(val1)

f2 = lambda x, y: x + y
val2 = f2(5, 10)
print(val2)

maximum = lambda x, y: x if x > y else y  # maximum is like f3
a, b = 10, 20
print("bigger num is : ", maximum(a, b))
