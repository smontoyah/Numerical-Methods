# -*- coding: utf-8 -*-
"""
Sebastián Montoya Hernández

Using rk4 to solve the system

dx/dt = ax + by + cz
dy/dt = dx + ey + fz
dz/dt = gx + hy + iz

with:

a = e = f = g = h = i = 0
b = -1.0
d = 1
c = -0.2

Plot:

x vs t
y vs t
z vs t

Invent the initial conditions for x, y, z
"""
import numpy as np
import matplotlib.pyplot as plt

tt = np.zeros(20000)
xx = np.zeros(20000)
yy = np.zeros(20000)
zz = np.zeros(20000)

def f(t, y):
    a = e = f = g = h = i = 0
    b = -1.0
    c = -0.2
    d = 1.0
    rhs = [0] * 3
    rhs[0] = a * y[0] + b * y[1] + c * y[2]
    rhs[1] = d * y[0] + e * y[1] + f * y[2]
    rhs[2] = g * y[0] + h * y[1] + i * y[2]
    return rhs

def rk4(t, h, y, n):
    
    fd = [0] * (n + 1)
    k1 = [0] * (n + 1)
    k2 = [0] * (n + 1)
    k3 = [0] * (n + 1)
    k4 = [0] * (n + 1)
    ymuda = [0] * (n + 1)
    fd = f(t, y)  # Right-hand side
    for i in range(0, n + 1):
        k1[i] = h * fd[i]
    for i in range(0, n + 1):
        ymuda[i] = y[i] + k1[i] / 2
    fd = f(t + h / 2, ymuda)
    for i in range(0, n + 1):
        k2[i] = h * fd[i]
        ymuda[i] = y[i] + k2[i] / 2.
    fd = f(t + h / 2., ymuda)
    for i in range(0, n + 1):
        k3[i] = h * fd[i]
        ymuda[i] = y[i] + k3[i]
    fd = f(t + h, ymuda)
    for i in range(0, n + 1):
        k4[i] = h * fd[i]
    for i in range(0, n + 1):
        y[i] = y[i] + (k1[i] + 2 * (k2[i] + k3[i]) + k4[i]) / 6.
    return y

dt = 1e-2
y = [0] * 3  # For initial conditions
y[0] = 4.3
y[1] = -1.8
y[2] = 0.9

f(0, y)  # Call for initial conditions
i = 0

for t in np.arange(0, 200, dt):
    r = rk4(t, dt, y, 2)
    tt[i] = t
    xx[i] = r[0]
    yy[i] = r[1]
    zz[i] = r[2]
    i += 1

fig = plt.figure()

ax1 = plt.subplot(211)
ax1.plot(tt, xx)
ax1.set_title('X vs t')

ax2 = plt.subplot(223)
ax2.plot(tt, yy)
ax2.set_title('Y vs t')

ax3 = plt.subplot(224)
ax3.plot(xx, yy)
ax3.set_title('Y vs X')

plt.show()
