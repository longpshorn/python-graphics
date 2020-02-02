#!/usr/local/bin/python3

"""
CIRCLES
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


def plot_line_arc(xc, yc, radius, p1, p2, dp, color='k', linestyle='-', linewidth=1):
    xlast = xc + radius * np.cos(p1)
    ylast = yc + radius * np.sin(p1)
    for p in np.arange(p1 + dp, p2, dp):
        x = xc + radius * np.cos(p)
        y = yc + radius * np.sin(p)
        plt.plot([xlast, x], [ylast, y], color=color,
                 linestyle=linestyle, linewidth=linewidth)
        xlast = x
        ylast = y


def main():
    plot_grid([-75, 75, 50, -50], 'on', True)
    plot_reference_frame()

    p1 = 0 * np.pi / 180
    p2 = 360 * np.pi / 180
    dp = (p2 - p1) / 100

    # Green circle
    xc = 0
    yc = 0
    r = 40
    plot_line_arc(xc, yc, r, p1, p2 / 2, dp, 'g')
    plot_line_arc(xc, yc, r, p2 / 2, p2, dp, 'g', linestyle=':')
    plt.scatter(xc, yc, s=15, color='g')

    # Red circle
    xc = -20
    yc = -20
    r = 10
    plot_line_arc(xc, yc, r, p1, p2, dp, 'r', linewidth=4)
    plt.scatter(xc, yc, s=15, color='r')

    # Purple circle
    xc = 20
    yc = 20
    r = 50
    plot_line_arc(xc, yc, r, p1, p2, dp, (0.8, 0, 0.8), linewidth=2)
    plt.scatter(xc, yc, s=15, color=(0.5, 0, 0.5))

    # Blue disc
    xc = -53
    yc = -30
    r1 = 0
    r2 = 10
    dr = 1
    for r in np.arange(r1, r2, dr):
        plot_line_arc(xc, yc, r, p1, p2, dp, (0, 0, .8), linewidth=4)

    plt.show()


main()
