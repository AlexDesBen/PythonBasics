#!/usr/bin/env python3

import math
# import matplotlib.pyplot as plt
import numpy as np


###############################################################################
###############################################################################


def Majuscule(s):
    output = ""
    i = 0
    for lettre in s:
        if i == 0:
            output += lettre.upper()
        else:
            output += lettre.lower()
        i += 1
    return output


def RadToDeg(x):
    return x*180/math.pi


def Gauss(x, a, s, m):
    return a*np.exp(-0.5*np.power((x - m)/s, 2))


###############################################################################
###############################################################################


if __name__ == "__main__":
    for x in range(0, 11):
        print("sin de %6.2f = %6.2f" % (x, math.sin(x)))
    x = np.arange(0, 10, 0.5)
    y = Gauss(x, 2, 10, 5)
    # plt.plot(x, y, '.k')
    # plt.show()
    print(x)
