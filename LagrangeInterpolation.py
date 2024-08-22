# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:29:51 2017

@author: Sebastian_Montoya

We have N pairs of points in the form (xi, g(xi)) = (xi, gi).
g(x) = g0*p0(x) + g1*p1(x) + ... + gN-1*pN-1(x)
where pi = Product of j (j != i) from 0 to N-1 of (x - xj) / (xi - xj)

"""
import matplotlib.pyplot as plt
import numpy as np
# Grade 5.0
N = 3  # Points to interpolate per trajectory

# Experimental points classified in trajectories of 3 points

X1 = np.array([0, 25, 50])
X2 = np.array([50, 75, 100])
X3 = np.array([100, 125, 150])
X4 = np.array([150, 175, 200])

Y1 = np.array([10.6, 16.0, 45.0])
Y2 = np.array([45.0, 83.5, 52.8])
Y3 = np.array([52.8, 19.9, 10.8])
Y4 = np.array([10.8, 8.25, 4.7])

def Lagrange(x, X, Y, N):  # Enter x, experimental points, and N
    y = 0.0
    for i in range(N):  # Up to N-1
        p = 1.0  # For the product
        for j in range(N):
            if i != j:  # i is different from j
                p *= (x - X[j]) / (X[i] - X[j])  # Calculate the lambdas
        y += Y[i] * p  # Sum the gi*pi
    return y

# Define the routine that plots each 2nd-degree polynomial for 3 experimental points

def plotpol():
    # Convert to float for proper interpolation
    xx = np.linspace(0, 50, 100)
    yy = Lagrange(xx, X1, Y1, N)
    plt.plot(xx, yy, label='Trajectory 1')
    plt.plot(X1, Y1, 'ro')

    xx = np.linspace(50, 100, 100)
    yy = Lagrange(xx, X2, Y2, N)
    plt.plot(xx, yy, label='Trajectory 2')
    plt.plot(X2, Y2, 'ro')

    xx = np.linspace(100, 150, 100)
    yy = Lagrange(xx, X3, Y3, N)
    plt.plot(xx, yy, label='Trajectory 3')
    plt.plot(X3, Y3, 'ro')

    xx = np.linspace(150, 200, 100)
    yy = Lagrange(xx, X4, Y4, N)
    plt.plot(xx, yy, label='Trajectory 4')
    plt.plot(X4, Y4, 'ro')

    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Lagrange Interpolation for Multiple Trajectories')
    plt.grid(True)

# Plot the concatenated polynomials as a single polynomial
plotpol()

# Now show the plot
plt.show()
