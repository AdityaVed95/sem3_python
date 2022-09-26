# x = b'hello'
# print(memoryview(x))

def minmaxpow(items):
    return min(items), (max(items), pow(min(items), max(items)))


# when multiple items are returned by the function , they are returned as a tuple

(lower, (upper, power)) = minmaxpow([-10, 2, 3, 4, 5, 8])  # tuple returned with unpacking
print(lower)
print(upper)
print(power)
print(len(str(power)))
