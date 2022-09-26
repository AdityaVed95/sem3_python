import logging

logging.basicConfig(filename="mylog2", level=logging.ERROR)

try:
    a = int(input())
    b = int(input())
    c = a / b

except Exception as e:  # the exception which occurred is stored in the object e
    logging.exception(e)  # the object e is passed to logging.exception() method which will
    # print the exception in the given log file
    
else:
    print(c)
