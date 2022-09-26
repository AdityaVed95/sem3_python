# filter even numbers from a list

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


lst = [10, 15, 151, 32, 53521, 523532, 32145, 31532]

lst1 = list(filter(is_even, lst))
print(lst1)

# using lambda fxn:

lst2 = list(filter(lambda x: (x % 2 == 0), lst))
print(lst2)
