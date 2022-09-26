from array import *

# array1 = array('i', [10, 20, 30, 40])
array1 = array('u', ['A', 'd', 'i', 't', 'y', 'a'])

f1 = open("read_me", "r")
array1.fromfile(f1, 2)
f1.close()

print(array1)
