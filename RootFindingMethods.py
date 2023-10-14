import matplotlib.pyplot as plt
import numpy as np
# Grade 5.0
print("The chosen original function is x**3-33*x**2+120*x+5")

def fx(x):  # Original function
    return x**3 - 33*x**2 + 120*x + 5

def fxd(x):  # Original function and its derivative (needed for Newton's method)
    return x**3 - 33*x**2 + 120*x + 5, 3*(40 - 22*x + x**2)

# Function to plot f(x) with matplotlib
def plot(f, a, b, rate):  # Function that plots f in the interval [a, b] with increment rate
    x = np.arange(a, b, rate)
    y = f(x)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    ax.grid(True)
    plt.show()

# Secant Method Algorithm to find roots of f(x)
def secant(func, x0, x1, eps):
    itmax = 100  # Maximum number of iterations
    for it in range(0, itmax):
        f1 = func(x1)
        f0 = func(x0)
        df = (f1 - f0) / (x1 - x0)
        x2 = x1 - f1 / df
        # print("it = ", it, x1, x2)  # Write the iteration, x1, and x2
        if abs(x2 - x1) <= eps:
            print("A root of f(x) using the secant method is", x2)
            break
        x0 = x1
        x1 = x2

# Newton's Method Algorithm to find roots of f(x)
def Newton(func, x, eps):  # Enter the function and the initial value x0
    itmax = 10000  # Maximum number of iterations
    for i in range(0, itmax):
        f, df = func(x)  # Find f(x) and f'(x)
        x = x - f / df  # xi + 1 = xi - f(xi)/f'(xi)
        dx = -f / df  # dx = xi+1-xi
        # print(i, x, f, dx)
        if abs(dx) <= eps:
            print("A root of f(x) using Newton's method is", x)
            break

# Bisection Method Algorithm to find roots of f(x)
def bisection(f, a, b, eps):
    for i in range(0, 100):
        c = (a + b) / 2  # Midpoint
        if f(c) == 0:
            print("A root of f(x) using the bisection method is", c)
            break
        if f(c) * f(a) < 0:
            b = c  # Reduce the interval to the right
        else:
            a = c  # Reduce the interval to the left
        if abs(b - a) < eps:
            print("A root of f(x) using the bisection method is", c)
            # print("f(c) = ",f(c))
            break
        if (i == 100):
            print("Root not found")

# Calling the functions. The intervals and points used are based on the graph.

plot(fx, 25, 35, 0.01)
eps = 1e-7
secant(fx, 28., 30, eps)
bisection(fx, 28., 30., eps)
Newton(fxd, 30., eps)
