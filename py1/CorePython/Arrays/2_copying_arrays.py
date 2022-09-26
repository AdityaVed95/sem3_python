import array as ar

array1 = ar.array('u', ['a', 'b', 'c'])
array2 = array1

array3 = ar.array(array1.typecode, [a for a in array1])
array4 = ar.array(array1.typecode, (a for a in array1))

print(array1)
print(array2)
print(array3)
print(array4)

print(id(array1))
print(id(array2))
print(id(array3))
print(id(array4))
