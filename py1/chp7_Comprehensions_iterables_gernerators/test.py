million_squares = (x * x for x in range(1, 1000001))  # using comprehensions and generators

mill_lis = [x * x for x in range(1, 1000001)]  # using comprehensions only

print(type(million_squares))
print(type(mill_lis))

copy = list(million_squares)
print(type(copy))

print(copy == mill_lis)
print(copy is mill_lis)
# equality in value but not in identity (both are not referring to the same list object in the memory)

addition1 = sum(x * x for x in range(1, 10000001))
print(addition1)

# note that to support readability : we have optional parenthesis in this case:
# sum(x * x for x in range(1, 10000001)) , actually it should have been this acc to definition:
# sum((x * x for x in range(1, 10000001)))

addition2 = sum(mill_lis)
print(addition2)


def is_prime(num):
    if num < 0:
        return False

    elif num == 0 or num == 1:
        return False

    counter = 0

    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1

    if counter == 2:
        return True
    else:
        return False


# using an if-clause in generator expressions

# printing sum of prime nos between 0 and 1000

add_prime = sum((x for x in range(1001) if is_prime(x)))

print(add_prime)
