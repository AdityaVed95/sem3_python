def multiply(num):
    if num > 1:
        return num * multiply(num - 1)
    else:
        return 1


print("Input a number: ")
n = int(input())

if n < 0:
    print("The factorial of the given number doesn't exist")
    exit()

factorial = multiply(n)

print("The factorial of the given number is: ", factorial)
