# this program is zero index based, so for n=9 actually 10th term of fiboncci sequence is printed

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..


def Fibonacci(n):
    if n < 0:
        print("incorrect input")

    elif n == 0:
        return 0
    
    elif n == 1 or n == 2:
        return 1
    
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


print(Fibonacci(9))
