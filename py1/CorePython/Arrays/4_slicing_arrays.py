# is similar to how we do it for lists

from array import *

array1 = array('i', [10, 20, 30, 40, 50, 60, 70])

array2 = array1[1:3]
print(array2)

array2 = array1[-4:-1:1]
print(array2)

array2 = array1[-1:-4:-1]
print(array2)

array2 = array1[-1:-4:1]
print(array2)
