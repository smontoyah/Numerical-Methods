import numpy as np
import matplotlib.pyplot as plt
# Grade 5.0

# ******************************Bisection Algorithm*****************************

# 1) Plot the function
# 2) Determine the interval where the function changes sign
# 3) Divide the interval by 2 -> c = (a+b)/2
# 4) Is f(c)*f(a) < 0?
#    if 4 is true -> b = c and repeat 3
#    otherwise -> a = c and repeat 3
# 5) Is |b-a| < epsilon? (predefined epsilon)
#    if 5 is true -> the root is c
#    otherwise -> repeat 3

# def bisection(f, a, b, epsilon)

# *********************************Application***********************************
# Initial data for Halley's comet
t = 1986.2491  # years
t0 = 1986.1113  # years
e = 0.9672671
T = 75.9600  # years
M = (2*np.pi/T)*(t-t0)
# By equating M with M = E - e*sin(E), we get the Kepler's equation

def Kep(E):
    return M - E + e*np.sin(E)

def plot(f, a, b, rate):  # Function that plots f in the interval [a, b] with increment rate
    x = np.arange(a, b, rate)
    y = f(x)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(x, y)
    ax.grid(True)
    plt.show()

plot(Kep, 0.1, 0.5, 0.01)

def bisection(f, a, b, eps):
    for i in range(0, 100):
        c = (a + b) / 2  # Midpoint
        if f(c) == 0:
            print("The root is ", c)
            break
        if f(c) * f(a) < 0:
            b = c  # Reduce the interval to the right
        else:
            a = c  # Reduce the interval to the left
        if abs(b - a) < eps:
            print("Iter = ", 1, "E is ", c)
            print("f(c) = ", f(c))
            break
        if i == 100:
            print("Root not found")

eps = 1e-7
bisection(Kep, 0.1, 0.5, eps)  # Interval chosen by observing the graph
