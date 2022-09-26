try:
    f = open("myfile", "w")

    print("Enter the 1st number")
    x = input()
    a = int(x)

    print("Enter the 2nd number")
    x = input()
    b = int(x)

    c = a / b
    f.write("Writing %f to myfile" % c)

except ZeroDivisionError:
    print("Division by zero is not allowed")

finally:
    f.close()
    print("File closed")

# note : check the variable scoping of variables in try block inside the finally block
