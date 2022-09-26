import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
import math


def f(x):
    return math.exp(-(1 + (x ** 2))) / (1 + (x ** 2))


x = sy.Symbol("x")
print(sy.integrate(f(x), (x, 0, 1000000)))
