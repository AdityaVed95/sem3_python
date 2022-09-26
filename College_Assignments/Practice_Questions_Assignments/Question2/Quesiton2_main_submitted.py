def input_equations():
    print("For the 1st Equation: ")
    print("Enter the degree of equation: ")
    degree1 = int(input())

    counter1 = degree1

    p_input_equations = []  # 1st equation

    while counter1 >= 0:
        print("Enter the coefficient of degree ", counter1)
        coefficient = float(input())
        temp = [coefficient, float(counter1)]
        p_input_equations.append(temp)
        counter1 -= 1

    q_input_equations = []

    print("For the 2nd equation: ")
    print("Enter the degree of equation: ")
    degree2 = int(input())

    counter2 = degree2

    while counter2 >= 0:
        print("Enter the coefficient of degree ", counter2)
        coefficient = float(input())
        temp = [coefficient, float(counter2)]
        q_input_equations.append(temp)
        counter2 -= 1
        
    return p_input_equations, q_input_equations


def normalise(p_norm, q_norm):
    length_of_p_norm = len(p_norm)
    length_of_q_norm = len(q_norm)

    if length_of_p_norm > length_of_q_norm:

        difference = length_of_p_norm - length_of_q_norm
        degree_of_q = q_norm[0][1]
        counter = 1

        while difference > 0:
            q_norm.insert(0, [0, (degree_of_q + counter)])
            difference -= 1
            counter += 1

        return p_norm, q_norm

    elif length_of_p_norm < length_of_q_norm:
        difference = length_of_q_norm - length_of_p_norm
        degree_of_p = p_norm[0][1]
        counter = 1

        while difference > 0:
            p_norm.insert(0, [0, degree_of_p + counter])
            difference -= 1
            counter += 1

        return p_norm, q_norm

    else:
        return p_norm, q_norm
        # both the equations are of the same degree and thus there is no need of normalisation


def add(p_add, q_add):
    add_final = []
    # 5 degree equation contains 6 terms from degree 5 to 0
    # 5 degree equation ka list contains 6 terms

    sum = 0
    for iterable1, iterable2 in zip(p_add, q_add):
        sum = iterable1[0] + iterable2[0]
        add_final.append([sum, iterable1[1]])

    return add_final


def subtract(p_sub, q_sub):
    subtract_final = []
    difference = 0
    for iterable1, iterable2 in zip(p_sub, q_sub):
        difference = iterable1[0] - iterable2[0]
        subtract_final.append([difference, iterable1[1]])

    return subtract_final


def main():
    p_input, q_input = input_equations()
    p_normalised, q_normalised = normalise(p_input, q_input)

    print("Adding two polynomials:")
    addition = add(p_normalised, q_normalised)
    print(addition)

    print("Subtracting two polynomials:")
    subtraction = subtract(p_normalised, q_normalised)
    print(subtraction)


if __name__ == "__main__":
    main()
