from functools import *

lst1 = [1, 2, 3, 4, 5, 6]
result = reduce(lambda x, y: x + y, lst1)
print(result)

result2 = reduce(lambda x, y, z: x + y + z, lst1)
print(result2)

# IN reduce function : we can only take 2 elements at a time
