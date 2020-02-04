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
    plot_grid([0, 150, 100, 0], 'on', True)

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

    Rx = radians(0)
    xc = 25
    yc = 40
    zc = 20
    plotcirclex(xc, yc, zc, x, y, z, Rx)

    Rx = radians(45)
    xc = 55
    yc = 40
    zc = 20
    plotcirclex(xc, yc, zc, x, y, z, Rx)

    Ry = radians(70)
    xc = 85
    yc = 40
    zc = 20
    plotcircley(xc, yc, zc, x, y, z, Ry)

    Rz = radians(90)
    xc = 115
    yc = 40
    zc = 20
    plotcirclez(xc, yc, zc, x, y, z, Rz)

    plt.text(23, 63, '(a)')
    plt.text(53, 63, '(b)')
    plt.text(83, 63, '(c)')
    plt.text(112, 63, '(d)')
    plt.text(21, 73, 'R=0')
    plt.text(47, 73, 'Rx=45°')
    plt.text(77, 73, 'Rx=30°')
    plt.text(107, 73, 'Rx=90°')
    plt.arrow(42, 40, 25, 0, head_width=2, head_length=3, color='r')
    plt.arrow(42, 40, 28, 0, head_width=2, head_length=3, color='r')
    plt.arrow(85, 25, 0, 27, head_width=2, head_length=2, color='r')
    plt.arrow(85, 25, 0, 29, head_width=2, head_length=2, color='r')
    plt.plot([8, 130], [8, 8], color='k')
    plt.plot([8, 8], [8, 85], color='k')
    plt.text(120, 6, 'X')
    plt.text(3, 80, 'Y')
    plt.scatter(115, 40, s=30, color='r')

    plt.show()


main()
