from array import *

array1 = array('i', [10, 20, 30, 40, 50])

print("1: ", array1)

x = 60
y = 70
array1.append(x)
array1.append(y)
array1.append(50)

print("2: ", array1)

counter = array1.count(50)  # no of 50's in the array

# array2 = array('u', ['A', 'd', 'i', 't', 'y', 'a'])
# array1.extend(array2)
# the above 2 lines generate error : TypeError: can only extend with array of same kind

array2 = array('i', [100, 200, 300])
array1.extend(array2)
print(array1)

list1 = [1000, 2000, 3000]
tuple1 = (500, 600, 700)
dict1 = {1: 2, 3: 4, 5: 6}

array1.extend(list1)
array1.extend(tuple1)
array1.append(dict1[1])
array1.extend(dict1)
print(array1)

print(array1.typecode)
print(array1.itemsize)
