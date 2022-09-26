# print new list containing square of all numbers of list 
# map(function,sequence)

# is used to change each and every element of the list and then create a new list of 
# those changed elements

from math import prod


def squares(x):
    return x**2

lst1 = [12,532,21,35]

lst2 = list(map(squares,lst1))

print(lst2)

lst3 = list(map(lambda x: x**2,lst1))

print(lst3)

exp1 = [1,2,3,4,5]
exp2 = [6,7,8,9,10]

product = list(map(lambda x,y: x*y,exp1,exp2))
print(product)



