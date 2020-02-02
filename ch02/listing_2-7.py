#!/usr/local/bin/python3

"""
ELLIPSES
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_grid(extents, axis_on='on', plot_grid=True):
    plt.axis(extents)
    plt.axis(axis_on)
    plt.grid(plot_grid)


def plot_reference_frame():
    plt.arrow(0, 0, 60, 0, head_length=4, head_width=3, color='k')
    plt.arrow(0, 0, 0, 45, head_length=4, head_width=3, color='k')

    plt.text(58, -3, 'x')
    plt.text(-5, 44, 'y')


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
    plot_grid([-67, 67, 50, -50], 'on', True)
    plot_reference_frame()

    # Red ellipse
    a = 40
    b = 20.
    p1 = 0
    p2 = 180 * np.pi / 180
    dp = .2 * np.pi / 180

    xplast = a
    yplast = 0
    for p in np.arange(p1, p2, dp):
        xp = np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5)
        yp = np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5)
        if p > np.pi / 2:
            xp = -xp
        plt.plot([xplast, xp], [yplast, yp], color='r')
        plt.plot([xplast, xp], [-yplast, -yp], color='r')
        xplast = xp
        yplast = yp

    # Green ellipse
    a = 20.
    b = 40.
    xp1 = -a
    xp2 = a
    dx = .1

    xplast = -a
    yplast = 0
    for xp in np.arange(xp1, xp2, dx):
        yp = b * (1 - xp ** 2. / a ** 2.) ** .5
        plt.plot([xplast, xp], [yplast, yp], linewidth=1, color='g')
        plt.plot([xplast, xp], [-yplast, -yp], linewidth=1, color='g')
        xplast = xp
        yplast = yp

    plt.plot([xplast, a], [yplast, 0], linewidth=1, color='g')
    plt.plot([xplast, a], [-yplast, 0], linewidth=1, color='g')

    # Blue ellipse
    a = 5.
    b = 15.
    p1 = 0
    p2 = 180 * np.pi / 180
    dp = .2 * np.pi / 180

    for p in np.arange(p1, p2, dp):
        xp = np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5)
        yp = np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5)
        if p > np.pi / 2:
            xp = -xp
        plt.plot([xp, xp], [yp, -yp], linewidth=1, color='b')

    plt.show()


main()
