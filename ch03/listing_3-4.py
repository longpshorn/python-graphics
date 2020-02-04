#!/usr/local/bin/python3

"""
SEQUENTIALCIRCLES
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians


def plot_grid(extents, axis_on='on', plot_grid=True):
    plt.axis(extents)
    plt.axis(axis_on)
    plt.grid(plot_grid)


def rotx(xc, yc, zc, xp, yp, zp, Rx):
    a = [xp, yp, zp]
    b = [1, 0, 0]  # [cx11, cx12, cx13]
    xpp = np.inner(a, b)
    b = [0, cos(Rx), -sin(Rx)]  # [cx21, cx22, cx23]
    ypp = np.inner(a, b)
    b = [0, sin(Rx), cos(Rx)]  # [cx31, cx32, cx33]
    zpp = np.inner(a, b)
    [xg, yg, zg] = [xpp + xc, ypp + yc, zpp + zc]
    return [xg, yg, zg]


def roty(xc, yc, zc, xp, yp, zp, Ry):
    a = [xp, yp, zp]
    b = [cos(Ry), 0, sin(Ry)]  # [cy11, cy12, cy13]
    xpp = np.inner(a, b)
    b = [0, 1, 0]  # [cy21, cy22, cy23]
    ypp = np.inner(a, b)
    b = [-sin(Ry), 0, cos(Ry)]  # [cy31, cy32, cy33]
    zpp = np.inner(a, b)
    [xg, yg, zg] = [xpp + xc, ypp + yc, zpp + zc]
    return [xg, yg, zg]


def rotz(xc, yc, zc, xp, yp, zp, Rz):
    a = [xp, yp, zp]
    b = [cos(Rz), -sin(Rz), 0]  # [cz11, cz12, cz13]
    xpp = np.inner(a, b)
    b = [sin(Rz), cos(Rz), 0]  # [cz21, cz22, cz23]
    ypp = np.inner(a, b)
    b = [0, 0, 1]  # [cz31, cz32, cz33]
    zpp = np.inner(a, b)
    [xg, yg, zg] = [xpp + xc, ypp + yc, zpp + zc]
    return [xg, yg, zg]


def plotcircle(xc, yc, xg, yg, zg):
    lastxg = xg[0]
    lastyg = yg[0]
    for i in range(len(xg)):
        color = 'r'
        if (i < len(xg) / 2):
            color = 'g'
        plt.plot([lastxg, xg[i]], [lastyg, yg[i]], linewidth=1, color=color)
        lastxg = xg[i]
        lastyg = yg[i]

    plt.scatter(xc, yc, s=5)
    plot_grid([0, 150, 100, 0], 'on', True)
    plt.show()


def plotcirclex(xc, yc, zc, x, y, z, Rx):
    xg = [0] * len(x)
    yg = [0] * len(x)
    zg = [0] * len(x)
    for i in range(len(xg)):  # Rotate eight corners
        [xg[i], yg[i], zg[i]] = rotx(xc, yc, zc, x[i], y[i], z[i], Rx)
        [x[i], y[i], z[i]] = [xg[i] - xc, yg[i] - yc, zg[i] - zc]
    plotcircle(xc, yc, xg, yg, zg)


def plotcircley(xc, yc, zc, x, y, z, Ry):
    xg = [0] * len(x)
    yg = [0] * len(x)
    zg = [0] * len(x)
    for i in range(len(xg)):  # Rotate eight corners
        [xg[i], yg[i], zg[i]] = roty(xc, yc, zc, x[i], y[i], z[i], Ry)
        [x[i], y[i], z[i]] = [xg[i] - xc, yg[i] - yc, zg[i] - zc]
    plotcircle(xc, yc, xg, yg, zg)


def plotcirclez(xc, yc, zc, x, y, z, Rz):
    xg = [0] * len(x)
    yg = [0] * len(x)
    zg = [0] * len(x)
    for i in range(len(xg)):  # Rotate eight corners
        [xg[i], yg[i], zg[i]] = rotz(xc, yc, zc, x[i], y[i], z[i], Rz)
        [x[i], y[i], z[i]] = [xg[i] - xc, yg[i] - yc, zg[i] - zc]
    plotcircle(xc, yc, xg, yg, zg)


def main():
    # Lists
    x = []
    y = []
    z = []

    xg = []
    yg = []
    zg = []

    phi1 = radians(0)
    phi2 = radians(360)
    dphi = radians(5)

    r = 10

    for phi in np.arange(phi1, phi2 + dphi, dphi):
        xp = r * cos(phi)
        yp = r * sin(phi)
        zp = 0
        x.append(xp)
        y.append(yp)
        z.append(zp)
        xg.append(xp)
        yg.append(yp)
        zg.append(zp)

    xc = 75
    yc = 50
    zc = 50

    while True:
        axis = input('x, y, or z?: ')
        if axis == 'x':
            Rx = radians(float(input('Rx degrees?: ')))
            plotcirclex(xc, yc, zc, x, y, z, Rx)
        if axis == 'y':
            Ry = radians(float(input('Ry degrees?: ')))
            plotcircley(xc, yc, zc, x, y, z, Ry)
        if axis == 'z':
            Rz = radians(float(input('Rz degrees?: ')))
            plotcirclez(xc, yc, zc, x, y, z, Rz)
        if axis == '':
            break


main()
