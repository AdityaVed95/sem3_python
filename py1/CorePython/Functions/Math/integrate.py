import matplotlib.pyplot as plt
import numpy as np
import sympy as sy


def run():
    def f(x):
        return x * x

    x = sy.Symbol("x")
    print(sy.integrate(f(x), (x, 0, 2)))


if __name__ == "__main__":
    run()
