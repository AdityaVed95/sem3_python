# note : code not working for all test cases, some bug maybe in the calculations function


def calculate_LCM(n1, n2):
    i = 1

    n1 = 0
    n2 = 14

    LCM = 0

    if n1 == 0 or n2 == 0:
        LCM = 0
        return LCM

    else:
        while i <= n1 * n2:

            if i % n1 == 0 and i % n2 == 0:
                LCM = i
                break
            i += 1

        return LCM


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


# Function to return LCM of two numbers
def lcm(a, b):
    return (a / gcd(a, b)) * b


def input_equations():
    # 0th element is coefficient of x, 1st element is coeff of y , 2nd element is constant on RHS
    print("For equation : ax + by = e ")
    print("enter the value of a:")
    a = int(input())
    print("enter the value of b:")
    b = int(input())
    print("enter the value of e:")
    e = int(input())

    eq1 = [a, b, e]

    print("For Equation : cx + dy = f ")
    print("enter the value of c:")
    c = int(input())
    print("enter the value of d:")
    d = int(input())
    print("enter the value of f:")
    f = int(input())

    eq2 = [c, d, f]

    return eq1, eq2


def calculations(equation1, equation2, LCM):
    # multiply each element of equation1 and equation 2 with lcm so that the coeff of y
    # becomes the same for both the eqns
    # x + y = z

    multiply1 = LCM / equation1[1]
    multiply2 = LCM / equation2[1]

    for item in equation1:
        item = item * multiply1
    for item in equation2:
        item = item * multiply2

    x1 = equation1[0] - equation2[0]
    z1 = equation1[2] - equation2[2]

    x = z1 / x1
    y = (equation1[2] - equation1[0] * x) / equation1[1]
    return x, y


def main():
    equation1 = []
    equation2 = []
    equation1, equation2 = input_equations()
    LCM = lcm(equation1[1], equation2[1])
    x, y = calculations(equation1, equation2, LCM)
    print("Value of x is : ", x)
    print("Value of y is : ", y)


if __name__ == "__main__":
    main()
