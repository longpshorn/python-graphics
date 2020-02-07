#!/usr/local/bin/python3

"""
PERSPECTIVE
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians


def plot_grid(extents, axis_on='on', plot_grid=True):
    plt.axis(extents)
    plt.axis(axis_on)
    plt.grid(plot_grid)


def plothouse(xg, yg, zg):
    plt.plot([xg[0], xg[3]], [yg[0], yg[3]], color='k')
    plt.plot([xg[1], xg[2]], [yg[1], yg[2]], color='k')
    plt.plot([xg[4], xg[7]], [yg[4], yg[7]], color='k')
    plt.plot([xg[5], xg[6]], [yg[5], yg[6]], color='k')
    plt.plot([xg[8], xg[9]], [yg[8], yg[9]], color='k')
    plt.plot([xg[4], xg[0]], [yg[4], yg[0]], color='k')
    plt.plot([xg[5], xg[1]], [yg[5], yg[1]], color='k')
    plt.plot([xg[6], xg[2]], [yg[6], yg[2]], color='r')
    plt.plot([xg[7], xg[3]], [yg[7], yg[3]], color='r')
    plt.plot([xg[0], xg[8]], [yg[0], yg[8]], color='k')
    plt.plot([xg[1], xg[8]], [yg[1], yg[8]], color='k')
    plt.plot([xg[2], xg[9]], [yg[2], yg[9]], color='r')
    plt.plot([xg[3], xg[9]], [yg[3], yg[9]], color='r')
    plt.plot([xg[4], xg[5]], [yg[4], yg[5]], color='k')
    plt.plot([xg[6], xg[7]], [yg[6], yg[7]], color='r')


def plothousey(xc, yc, zc, x, y, z, Ry):
    xg = [0] * len(x)
    yg = [0] * len(x)
    zg = [0] * len(x)
    for i in range(len(x)):
        [xg[i], yg[i], zg[i]] = roty(xc, yc, zc, x[i], y[i], z[i], Ry)
    return [xg, yg, zg]


def roty(xc, yc, zc, x, y, z, Ry):
    a = [x, y, z]
    b = [cos(Ry), 0, sin(Ry)]
    xpp = np.inner(a, b)
    b = [0, 1, 0]
    ypp = np.inner(a, b)
    b = [-sin(Ry), 0, cos(Ry)]
    zpp = np.inner(a, b)
    [xg, yg, zg] = [xpp + xc, ypp + yc, zpp + zc]
    return [xg, yg, zg]


def perspective(xg, yg, zg, xfp, yfp, zfp):
    for i in range(len(xg)):
        a = xg[i] - xfp
        b = yg[i] - yfp
        c = zg[i] + abs(zfp)
        q = np.sqrt(a * a + b * b + c * c)
        ux = a / q
        uy = b / q
        uz = c / q
        qh = q * abs(zfp) / (zg[i] + abs(zfp))
        xg[i] = ux * qh + xfp
        yg[i] = uy * qh + yfp
        zg[i] = 0
    return [xg, yg, zg]


def main():
    plot_grid([0, 150, 100, 0], 'on', True)

    x = [-20, -20, 20, 20, -20, -20, 20, 20, -20, 20]
    y = [-10, -10, -10, -10, 10, 10, 10, 10, -20, -20]
    z = [5, -5, -5, 5, 5, -5, -5, 5, 0, 0]

    xc = 30
    yc = 50
    zc = 10

    xg = []
    yg = []
    zg = []

    for i in np.arange(len(x)):
        xg.append(x[i] + xc)
        yg.append(y[i] + yc)
        zg.append(z[i] + zc)

    xfp = 80
    yfp = 50
    zfp = -100

    xc = 80
    yc = 50
    zc = 50
    Ry = radians(45)

    [xg, yg, zg] = plothousey(xc, yc, zc, x, y, z, Ry)
    [xg, yg, zg] = perspective(xg, yg, zg, xfp, yfp, zfp)
    plothouse(xg, yg, zg)

    plt.show()


main()
