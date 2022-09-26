from array import *

array1 = array('i', [10, 20, 30, 40, 50])

array2 = array(array1.typecode, (a * 5 for a in array1))

# array 2 contains elements that are 5 times the value of array1 elements

print(array2)

n1 = len(array1)
print(n1)
