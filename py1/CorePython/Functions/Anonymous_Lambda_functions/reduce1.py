from functools import *

lst1 = [1, 2, 3, 4, 5, 6]
# lst2 = list(map(lambda x, y: x * y, lst1))
# print(lst2)
# the above wont work because if we wish to pass two elements of list at a time as parameters
# to the lambda function then it is not possible to achieve that in case of map function


# but it is possible to pass two parameter of the list(or any sequence) at a time to the
# lambda function then it is possible in case of reduce function

# because reduce function aims to reduce the entire sequence to a single element by performing
# some action on each element of the sequence

result = reduce(lambda x, y: x * y, lst1)
print(result)

result2 = reduce(lambda a, b: a + b, lst1)
print(result2)

# printing sum of nos from 1 to 50 :

result3 = reduce(lambda a, b: a + b, range(0, 51))
print(result3)
