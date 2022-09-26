from Quesiton2_OOP import Equations


def test_single_eq(single_eq):
    object1 = single_eq
    object1.calculate_degree_of_eqn()
    print(object1.degree)
    object1.normalizing_the_eqn_phase1()
    object1.normalizing_the_eqn_phase2(6)
    print(object1.normalised_equation)


def test_multi_eq():
    eq_list = [
        Equations([[52, 5], [3, 2], [5, 1], [12, 0]]),
        Equations([[90, 4], [32, 3], [3, 2], [5, 1], [12, 0]])
    ]

    for item in eq_list:
        test_single_eq(item)


test_single_eq(
    Equations([[52, 5], [3, 2], [5, 1], [12, 0]]))  # passing object as a parameter to test_single_eqn function
# test_multi_eq()
