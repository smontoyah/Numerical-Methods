# -*- coding: utf-8 -*-
"""
Created on Mon May  8 21:53:36 2017

Author: Sebastian Montoya Hernandez

Assignment 7: Using Euler's method for harmonic motion. That is,
the force in the form F = -k*x.

1) Graph the motion.
2) Add a friction force Fr = b*v^2.
"""
from visual.graph import *

# Create graphs for position and velocity
escena1 = gdisplay(width=700, height=300, title='Position')
distance = gcurve(color=color.cyan)
escena2 = gdisplay(x=500, width=700, height=300, title='Speed')
velocity = gcurve(color=color.yellow)
escena3 = gdisplay(y=300, width=700, height=300, title='Position with Friction')
posifriction = gcurve(color=color.orange)
escena4 = gdisplay(x=500, y=300, width=700, height=300, title='Speed with Friction')
velofriction = gcurve(color=color.green)

# Initial conditions
m = 1  # Mass in Kg
k = 1  # Spring constant
x = 0  # Initial position
v = 3  # Initial speed
h = 0  # Time interval
dh = 0.1  # Differential time interval

# Using Euler's method without friction
for i in range(0, 300):
    v = v - dh * (k / m) * x
    x = x + dh * v
    distance.plot(pos=(h, x))
    velocity.plot(pos=(h, v))
    h += dh

# Using Euler's method with friction
m = 1  # Mass in Kg
k = 1  # Spring constant
x = 0  # Initial position
v = 3  # Initial speed
h = 0  # Time interval
dh = 0.1  # Differential time interval
b = 0.2  # Friction constant

for i in range(0, 300):
    v = v - dh * (k * x - b * v**2) / m
    x = x + dh * v
    posifriction.plot(pos=(h, x))
    velofriction.plot(pos=(h, v))
    h += dh
