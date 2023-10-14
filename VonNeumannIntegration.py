# -*- coding: utf-8 -*-
"""
Von Neumann numerical integral method

Student: Sebastian Montoya Hernandez
"""
# Grade: 5.0 (the points are quite large)

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import random

print('*****************************************************************')
print('This program uses Von Neumann\'s numerical integration method')
print('to calculate the area between two curves in the interval [0,1].')
print('The plotting is done using the Matplotlib library with 4000 points.')
print('*****************************************************************')

# This draws a rectangle where the functions will be contained
someX, someY = 0.5, 0.5
currentAxis = plt.gca()
currentAxis.add_patch(Rectangle((someX - .5, someY - .5), 1, 1, facecolor="grey"))

# Defines the functions
def f1(x):
    return x**2

def f2(x):
    return np.sqrt(x)

# This draws the functions
def plotfunction():
    xx = np.arange(0, 1., 1/100)
    plt.plot(xx, f1(xx), label='f(x) = x^2')
    plt.plot(xx, f2(xx), label='f(x) = sqrt(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()

plotfunction()

# This loop uses Von Neumann's method
j = 0  # Counter for f1
k = 0  # Counter for f2
Npts = 4000  # Drawn points

for i in range(0, Npts):

    x = random.random()  # random between 0 and 1
    y = random.random()  # random between 0 and 1

    if y <= f1(x):
        j += 1
        plt.plot(x, y, 'ro')

    if y <= f2(x):
        k += 1

    if y <= f2(x) and y > f1(x):
        plt.plot(x, y, 'bo')

    if y > f2(x):
        plt.plot(x, y, 'go')

    area1 = j / Npts
    area2 = k / Npts

print("Area under f(x) = x^2 is", area1)
print("Area under f(x) = sqrt(x) is", area2)
print("Area between the curves x^2 and sqrt(x) is", area2 - area1)
print("The theoretical area between the curves is approximately 0.33...")

plt.show()
