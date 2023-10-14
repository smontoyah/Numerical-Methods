from visual.graph import *
import numpy as np
pi = np.pi

# Initial data
rho = [4000, 11900, 13500]  # Density in kg/m^3
R = [1.2e6, 3.5e6, 6.5e6]  # Distance in meters
v = [(4./3)*pi*R[0]**3, (4./3)*pi*R[1]**3, (4./3)*pi*R[2]**3]  # Volume
m = [rho[0]*v[0], rho[1]*v[1] - rho[1]*v[0] + rho[0]*v[0], rho[2]*v[2] - rho[2]*v[1] + rho[1]*v[1]]  # Mass
G = 6.67e-11  # Gravitational constant in m^3/kg/s^2
mp = 0.1  # Particle mass in kg
d = 1e5 + R[2]  # Initial distance in meters
r = vector(d/2, d, 0)  # Initial position vector
v0y = 65  # Initial particle velocity in m/s
v = vector(v0y/2, v0y, 0)  # Initial velocity vector
dt = 1  # Time step in seconds

# Visualization
scene = display(title='Visualization')
core = sphere(radius=R[0], opacity=0.5, color=color.red)
mantle = sphere(radius=R[1], opacity=0.3, color=color.yellow)
crust = sphere(radius=R[2], opacity=0.3, color=color.cyan)
particle = sphere(pos=vector(r.x, r.y, 0), radius=1e5, color=color.green, make_trail=True)

position_label = label(pos=(-4e6, 4.6e6), text='Position [m] =', box=0)
position_number_label = label(pos=(-4e3, 4.6e6), box=0)

scene_velocity = gdisplay(y=350, x=500, title='Position vs Velocity', xtitle='r', ytitle='v')
velocity_curve = gcurve(color=color.cyan)

scene_acceleration = gdisplay(height=300, x=500, title='Position vs Acceleration', xtitle='r', ytitle='a')
acceleration_curve = gcurve(color=color.cyan)

# Functions for interior layers
def volume(r):
    return 4*pi*r**3/3

def mass(r):
    if abs(r) >= R[2]:
        me = m[2]
    if abs(r) < R[2] and abs(r) > R[1]:
        me = rho[2]*volume(abs(r)) - rho[2]*v[1] + rho[1]*v[1] - rho[1]*v[0] + rho[0]*v[0]
    if abs(r) < R[1] and abs(r) > R[0]:
        me = rho[1]*volume(abs(r)) - rho[1]*v[0] + rho[0]*v[0]
    if abs(r) < R[0]:
        me = rho[0]*volume(abs(r))
    return me

# Application of Euler's method
for i in range(0, 20000):
    rate(500)

    F = -G * mass(particle.pos.y) * mp * (particle.pos) / (abs(particle.pos.y))**3
    a = F / mp
    v = v + a * dt
    r = r + v * dt
    particle.pos = r

    position_number_label.text = '%8.5f' % (abs(particle.pos.y))
    velocity_curve.plot(pos=(particle.pos.y, v.y))
    acceleration_curve.plot(pos=(particle.pos.y, a.y))
