def avg(list):
    tot = 0
    for x in list:
        tot += x

    avg = tot / len(list)

    return tot, avg


try:
    t, a = avg([1, "a", 2])
    print(t, a)

except TypeError:
    print("incorrect datatype")
except ZeroDivisionError:
    print("dont pass empty iterable")

# this program shows that if an error occurs in the function that is called , then the control
# of the program goes back to the calling function if the function call is in the try block

