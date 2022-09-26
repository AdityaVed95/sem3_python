no_of_prime = 0
no_of_composite = 0

j = 1

while True:
    print("For the {}th iteration , please enter a number".format(j))
    num = int(input())

    if num == -1:
        break

    if num <= 1:
        no_of_composite += 1
        j += 1
        continue

    i = 1
    counter = 0

    while i <= (num / 2):

        if num % i == 0:
            counter += 1

        i += 1

    if counter == 1:
        no_of_prime += 1
        j += 1
        continue

    else:
        no_of_composite += 1
        j += 1
        continue

print("Number of Prime Numbers are :", no_of_prime)
print("Number of Composite Numbers are : ", no_of_composite)
