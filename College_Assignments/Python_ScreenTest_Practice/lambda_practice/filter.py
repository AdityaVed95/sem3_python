# filter(function,sequence)

# is used to filter and get only few elements of the sequence

# elements taken up from sequence one at a time and then passed to the function
# the function returns true or false
# if function returns true then that element of sequence is extracted else if it returns
# false then the element is ignored and then the next element of sequence is passed 
# to the function

# filter all even numbers


def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False

lst = [10,521,5213,3134,43215,5213552]

lst1 = list(filter(is_even,lst))
print(lst1)

lst2 = list(filter(lambda x : x%2==0,lst))
print(lst2)

