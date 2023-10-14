# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 15:52:42 2017

@author: Sebastian Montoya Hernandez

THIS PROGRAM TAKES A FUNCTION WHOSE INTEGRAL IS KNOWN AND NUMERICALLY PERFORMS INTEGRATION USING
THE TRAPEZOID AND SIMPSON METHODS. IT ALSO COMPARES THE RESULTS
"""

# Grade: 5.0

import numpy as np

# Defining functions for integration
def trapezoid(func, a, b, N):  # Function to integrate, lower limit, upper limit, number of points
    h = (b - a) / (N - 1)
    sum = (func(a) + func(b)) / 2  # Initial term to sum
    for i in range(1, N - 1):
        sum = sum + func(a + i * h)
    return h * sum

def simpson(func, A, B, N):  # Enter the function, interval [a, b], and number of points
    if N % 2 == 0:  # The number of points is even
        N = N + 1
    s1 = 0
    s2 = 0
    h = (B - A) / N
    for i in range(1, N, 2):  # For odd values
        s1 += func(A + i * h)
    for i in range(2, N - 1, 2):
        s2 += func(A + i * h)
    return h * ((func(A) + func(B)) + 4 * s1 + 2 * s2) / 3.0

# Define the function to integrate
print("The function to integrate is f(x) = (sin(3x) + (e^(2x))/3) ")
print("**********************************************************")
def fx(x):
    return np.sin(3 * x) + 1/3 * (np.e**(2 * x))

# Integrate using two different methods in the interval [2, 6] with 1000 points
print("Using the trapezoid method, the integral of f(x) between 2 and 6 is APPROX = ", trapezoid(fx, 2, 6, 1000))
print("**********************************************************")
print("Using the Simpson method, the integral of f(x) between 2 and 6 is APPROX = ", simpson(fx, 2, 6, 1000))
print("**********************************************************")

# Analytically
print( "The indefinite integral of the function f(x) = (sin(3x) + (e^(2x))/3) is equal to 1/6 (e^(2x) - 2 cos(3x)) + constant. Using the fundamental theorem of calculus, the definite integral between 2 and 6 of f(x) is approximately 27116.7988293.")
print("**********************************************************")

# Error analysis
print("The error of the trapezoid method with respect to the analytical result with 7 decimal places is", abs(27116.7988293 - trapezoid(fx, 2, 6, 1000)))
print("**********************************************************")
print("The error of the Simpson method with respect to the analytical result with 7 decimal places is", abs(27116.7988293 - simpson(fx, 2, 6, 1000)))
print("**********************************************************")
print("It can be concluded that in this case, the trapezoid method is much more accurate than the Simpson method.")
