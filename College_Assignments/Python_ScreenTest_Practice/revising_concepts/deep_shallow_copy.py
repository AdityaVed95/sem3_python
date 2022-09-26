import copy

list1 = ["apple", "banana", "cherry"]
list2 = list1.copy()
print(id(list1))
print(id(list2))
# .copy() function returns a deep copy of the list

tuple1 = ("apple", "banana", "cherry")
# cannot use copy function for tuples
# tuple2 = tuple1.copy()
# print(tuple2)

tuple2 = copy.deepcopy(tuple1)
print(tuple2)
print(id(tuple1))
print(id(tuple2))
