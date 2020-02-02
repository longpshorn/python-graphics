#!/usr/local/bin/python3

"""
DOTLINE
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_grid(extents, axis_on='on', plot_grid=True):
    plt.axis(extents)
    plt.axis(axis_on)
    plt.grid(plot_grid)


def plot_reference_frame():
    plt.arrow(0, 0, 20, 0, head_length=4, head_width=3, color='k')
    plt.arrow(0, 0, 0, 20, head_length=4, head_width=3, color='k')

    plt.text(15, -3, 'x')
    plt.text(-5, 15, 'y')


def plot_scatter_line(xy, step_size=.5, dot_size=1, color_name='g'):
    x1 = xy[0][0]
    x2 = xy[1][0]
    y1 = xy[0][1]
    y2 = xy[1][1]
    q = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    ux = (x2 - x1) / q
    uy = (y2 - y1) / q

    for l in np.arange(0, q, step_size):
        px = x1 + l * ux
        py = y1 + l * uy
        plt.scatter(px, py, s=dot_size, color=color_name)


def main():
    plot_grid([-20, 130, 80, -20])

    plot_reference_frame()

    # Green line
    x1 = 20
    x2 = 120
    y1 = 40
    y2 = 20

    plot_scatter_line([[x1, y1], [x2, y2]])

    # Blue line
    x1 = 20
    x2 = 120
    y1 = 45
    y2 = 25

    plot_scatter_line([[x1, y1], [x2, y2]], step_size=2, color_name='b')

    plt.show()


main()
