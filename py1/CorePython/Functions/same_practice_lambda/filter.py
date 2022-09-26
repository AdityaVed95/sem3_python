def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


lst1 = [10, 20, 30, 45, 79, 43, 56]

lst_main = list(filter(is_even, lst1))
print(lst_main)

lst_main2 = list(filter(lambda x: x % 2 == 0, lst1))
print(lst_main2)
