import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
import math

a = 1


def f(x):
    return x ** 2
    # (a ** (2 / 3) - x ** (2 / 3)) ** (3 / 2)


x = sy.Symbol("x")
print(sy.integrate(f(x), (x, 0, a)))
