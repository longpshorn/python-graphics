#!/usr/local/bin/python3

import numpy as np
import matplotlib.pyplot as plt

plt.grid(True)
plt.axis('on')
plt.axis([-10, 10, 10, -10])

# Custom grid
x1 = -10
x2 = 10
y1 = 10
y2 = -10

dx = 0.5
dy = -0.5

for x in np.arange(x1, x2, dx):
    for y in np.arange(y1, y2, dy):
        plt.scatter(x, y, s=1, color='lightgray')

# Square box
plt.plot([-5, 5], [-5, -5], linewidth=2, color='k')
plt.plot([5, 5], [-5, 5], linewidth=2, color='k')
plt.plot([5, -5], [5, 5], linewidth=2, color='k')
plt.plot([-5, -5], [5, -5], linewidth=2, color='k')

# Correct distortion
# plt.axes().set_aspect('equal')

plt.show()
