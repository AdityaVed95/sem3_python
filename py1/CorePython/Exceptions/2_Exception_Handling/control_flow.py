# to see the control flow of the program in case of multiple exceptions and exception handlers :

try:
    print("for the 1st case: ")
    print("Enter 1st number")
    a = int(input())
    print("Enter 2nd number")
    b = int(input())

    c = a / b
    print("lets see if c is printed for the 1st test")

except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Note that Exception block is not executed")

except TypeError:
    print("Type error has occurred")

except ValueError:
    print("Value error has occurred")

except Exception:
    print("This is Exception block which is common for all types of exceptions")
    print("If this block is executed , it means that the exception which has occurred is not"
          "handled by other except blocks created by the programmer")
    print("Thus exceptions other then what is covered by except block has occurred")
    # exception block is meant to cover all types of exceptions which is not mentioned in the other except blocks

else:
    print("Wow no exceptions have occurred till now , thanks for being an ideal user")

finally:
    print("Now the exception handler is ending irrespective of whether you gave bad or good input")

print("program execution continues normally here")

# run this program by giving wrong input and see the control flow of the program

# defining the purpose of except Exception: block
# if there occurs some exception which is not listed by any of the except blocks then
# Exception block gets executed

# for eg , if we comment the zero division error vala except block and run the same program
# then the except Exception: block will get executed
