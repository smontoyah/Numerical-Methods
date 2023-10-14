# Hunter and Monkey
# *******************SEBASTIAN MONTOYA HERNANDEZ 99031713524********************
# Choose appropriate coordinates to keep the bullet's position always visible
# Doesn't plot the velocity vector (plots the components) Grade 3.5
from visual import *
# **************************Scene Parameters********************************
scene = display(width=800, height=800, range=400)
monkey = sphere(pos=(0, 380), color=color.orange, radius=10)
bullet = sphere(pos=(-200, 0), color=color.red, radius=10)
trail = curve(radius=1.5)
trail2 = curve(color=color.cyan, radius=1.5)

monkey_vec = arrow(color=color.cyan)  # Arrow associated with monkey's velocity
bullet_vec_y = arrow(color=color.red)  # Arrow associated with bullet's velocity in the y-axis
bullet_vec_x = arrow(color=color.red)  # Arrow associated with bullet's velocity in the x-axis

# ***********************Initial Data*****************************************
bullet_velocity = 100
initial_bullet_x = -200
initial_bullet_y = 0
initial_monkey_y = 380.
initial_monkey_x = 0
theta = -1 * atan(initial_monkey_y / initial_bullet_x)  # This is derived from the algebraic manipulation of
# the equations of bullet and monkey's position

# **********************Calculation of variables as a function of t*********************

for t in arange(0., 60., 0.4):
    rate(10)
    bullet_x = initial_bullet_x + bullet_velocity * cos(theta) * t  # Bullet's x-axis motion equation
    bullet_y = bullet_velocity * sin(theta) * t - 0.5 * (9.8) * t ** 2  # Bullet's y-axis motion equation
    bullet.pos = vector(bullet_x, bullet_y)
    trail.append(pos=((bullet_x, bullet_y)))
    monkey_y = initial_monkey_y - 0.5 * (9.8) * t ** 2  # Monkey's free fall
    monkey_x = initial_monkey_x
    monkey.pos = vector(monkey_x, monkey_y)  # Monkey's position vector
    trail2.append(pos=(monkey_x, monkey_y))
    monkey_vec.pos = monkey.pos  # Monkey's position = Arrow's position
    monkey_vec.axis = vector(0, -9.8 * t)  # Monkey's velocity vector in the y-axis
    bullet_vec_y.pos = bullet.pos  # Bullet's position = Arrow's position
    bullet_vec_y.axis = vector(0, bullet_velocity * sin(theta))  # Bullet's velocity vector in the y-axis
    bullet_vec_x.pos = bullet.pos  # Bullet's position = Arrow's position
    bullet_vec_x.axis = vector(bullet_velocity * cos(theta), 0)  # Bullet's velocity vector in the x-axis
