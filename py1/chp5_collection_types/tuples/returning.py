def minmax(items):
    return min(items), max(items)


x = minmax([1, 2, 3, 4, 5])  # tuple returned without unpacking
print(x)
print(type(x))

# when multiple items are returned by the function , they are returned as a tuple

lower, upper = minmax([-10, 2, 3, 4, 5, 8])  # tuple returned with unpacking
print(lower)
print(upper)
