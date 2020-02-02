#!/usr/local/bin/python3

"""
PARC
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


def plot_scatter_arc(xc, yc, radius, p1, p2, dp, dot_size=1, dot_color='g'):
    for p in np.arange(p1, p2, dp):
        x = xc + radius * np.cos(p)
        y = yc + radius * np.sin(p)
        plt.scatter(x, y, s=dot_size, color=dot_color)


def main():
    plot_grid([-10, 140, 90, -10], 'off', False)
    plot_reference_frame()

    xc = 20
    yc = 20
    radius = 40

    # Plot arc
    p1 = 20 * np.pi / 180
    p2 = 70 * np.pi / 180
    dp = (p2 - p1) / 100
    plot_scatter_arc(xc, yc, radius, p1, p2, dp)

    # Labels
    plt.text(61, 34, '(x1, y1)')
    plt.text(16, 60, '(x2, y2)')
    plt.scatter(xc, yc, s=10, color='k')
    plt.text(xc + 4, yc - 4, '(xc, yc)', color='k')

    plt.show()


main()
