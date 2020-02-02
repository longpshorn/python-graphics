#!/usr/local/bin/python3

import numpy as np
import matplotlib.pyplot as plt

x1 = -10
x2 = 123
y1 = 90
y2 = -10

plt.axis([x1, x2, y1, y2])
plt.axis('on')
plt.grid(True)
plt.title('Sample Axes')

# Grid
dx = 5
dy = -5
for x in np.arange(x1, x2, dx):
    for y in np.arange(y1, y2, dy):
        plt.scatter(x, y, s=1, color='lightgray')

plt.arrow(0, 0, 20, 0, head_length=4, head_width=3, color='k')
plt.arrow(0, 0, 0, 20, head_length=4, head_width=3, color='k')

plt.show()
