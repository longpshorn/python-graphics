#!/usr/local/bin/python3

"""
DOTDISCS
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
    plot_grid([0, 133, 100, 0], 'off', False)
    plot_reference_frame()

    # Simple r,p dot pattern
    xc = 40
    yc = 25

    p1 = 0
    p2 = 2 * np.pi
    dp = np.pi / 20

    rmax = 20
    dr = 2

    for r in np.arange(dr, rmax, dr):
        for p in np.arange(p1, p2, dp):
            x = xc + r * np.cos(p)
            y = yc + r * np.sin(p)
            plt.scatter(x, y, s=2, color='k')

    # Equal arch length dot pattern
    xc = 105
    yc = 25

    p1 = 0
    p2 = 2 * np.pi

    rmax = 20
    dr = 2
    dc = np.pi * rmax / 40

    for r in np.arange(dr, rmax, dr):
        dpr = dc / r
        for p in np.arange(p1, p2, dpr):
            x = xc + r * np.cos(p)
            y = yc + r * np.sin(p)
            plt.scatter(x, y, s=2, color='k')

    # Labels
    plt.text(38, 66, 'r,p')
    plt.text(95, 66, 'equal arc')

    plt.show()


main()
