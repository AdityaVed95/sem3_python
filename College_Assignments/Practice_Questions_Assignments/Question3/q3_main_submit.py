def input_equations():
    # 0th element is coefficient of x, 1st element is coeff of y , 2nd element is constant on RHS
    print("For equation : ax + by = e ")
    print("enter the value of a:")
    a = float(input())
    print("enter the value of b:")
    b = float(input())
    print("enter the value of e:")
    e = float(input())

    eq1 = [a, b, e]

    print("For Equation : cx + dy = f ")
    print("enter the value of c:")
    c = float(input())
    print("enter the value of d:")
    d = float(input())
    print("enter the value of f:")
    f = float(input())

    eq2 = [c, d, f]

    return eq1, eq2


def calculating_delta(eq1, eq2):
    a = eq1[0]
    b = eq1[1]
    e = eq1[2]

    c = eq2[0]
    d = eq2[1]
    f = eq2[2]

    delta = (a * d) - (c * b)
    delta_x = (e * d) - (f * b)
    delta_y = (a * f) - (c * e)

    return delta, delta_x, delta_y


def main():
    equation1 = []
    equation2 = []
    equation1, equation2 = input_equations()
    delta, delta_x, delta_y = calculating_delta(equation1, equation2)
    if (delta == 0 and delta_x != 0) or (delta == 0 and delta_y != 0):
        print("The given system of equations is inconsistent and has no solution")

    elif delta == 0 and delta_x == 0 and delta_y == 0:
        print("The given system of equations is consistent and has infinite solution")

    elif delta != 0:
        print("The given system of equations is consistent and has Unique solution")
        x = delta_x / delta
        y = delta_y / delta
        print("x = ", x)
        print("y = ", y)


if __name__ == "__main__":
    main()
