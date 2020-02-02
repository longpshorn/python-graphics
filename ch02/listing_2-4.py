#!/usr/local/bin/python3

"""
PARCGEOMETRY
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


def plot_line_arc(xc, yc, radius, p1, p2, dp, color):
    xlast = xc + radius * np.cos(p1)
    ylast = xc + radius * np.sin(p1)
    for p in np.arange(p1 + dp, p2, dp):
        x = xc + radius * np.cos(p)
        y = yc + radius * np.sin(p)
        plt.plot([xlast, x], [ylast, y], color=color)
        xlast = x
        ylast = y


def plot_line_segment(xc, yc, r, offset1, offset2, phi):
    x1 = xc + (r + offset1) * np.cos(phi)
    x2 = xc + (r + offset2) * np.cos(phi)
    y1 = yc + (r + offset1) * np.sin(phi)
    y2 = yc + (r + offset2) * np.sin(phi)
    plt.plot([x1, x2], [y1, y2], color='k')


def main():
    plot_grid([-10, 140, 90, -10], 'off', False)
    plot_reference_frame()

    xc = 20
    yc = 20
    r = 40

    # Plot arc
    phi1 = 20 * np.pi / 180
    phi2 = 70 * np.pi / 180
    dphi = (phi2 - phi1) / 20
    plot_scatter_arc(xc, yc, r, phi1, phi2, dphi, dot_size=2, dot_color='g')
    plt.plot([xc, xc + r * np.cos(phi1)],
             [yc, yc + r * np.sin(phi1)], color='k')
    plt.scatter(xc, yc, s=5, color='b')

    plot_line_segment(xc, yc, r, 3, 10, phi1)
    plot_line_segment(xc, yc, r, 3, 30, phi1)

    plt.plot([xc, xc + r * np.cos(phi2)],
             [yc, yc + r * np.sin(phi2)], color='k')

    phihalf = (phi1 + phi2) / 2
    phi3 = phihalf - dphi / 2
    phi4 = phihalf + dphi / 2

    plt.plot([xc, xc + r * np.cos(phi3)],
             [yc, yc + r * np.sin(phi3)], color='k')
    plt.plot([xc, xc + r * np.cos(phi4)],
             [yc, yc + r * np.sin(phi4)], color='k')

    plot_line_segment(xc, yc, r, 3, 15, phi3)
    plot_line_segment(xc, yc, r, 3, 15, phi4)

    dphi = phi3 / 100
    # P1 arc
    plot_scatter_arc(xc, yc, r + 5, 0,
                     phi1 / 2 - 3.2 * np.pi / 180, dphi, .1, 'k')
    plot_scatter_arc(xc, yc, r + 5, phi1 / 2 + 3.3 * np.pi / 180,
                     phi1, dphi, .1, 'k')

    # P2 arc
    plot_scatter_arc(xc, yc, r + 25, 0,
                     phi2 / 2 - 3.2 * np.pi / 180, dphi, .1, 'k')
    plot_scatter_arc(xc, yc, r + 25, phi2 / 2 + 3.2 * np.pi / 180,
                     phi2, dphi, .1, 'k')

    # P arc
    plot_scatter_arc(xc, yc, r + 13, 0,
                     phi3 / 2 - .5 * np.pi / 180, dphi, .1, 'k')
    plot_scatter_arc(xc, yc, r + 13, phi3 / 2 + 9 * np.pi / 180,
                     phi3, dphi, .1, 'k')

    # dp arc
    plot_scatter_arc(xc, yc, r + 13, phi3 + 5 * dphi,
                     phi3 + 25 * dphi, dphi, .1, 'k')
    plt.plot([xc, 100], [yc, yc], 'k')
    plt.plot([xc, xc], [yc, 80], 'k')

    # Labels
    plt.text(71, 58, 'p2', size='small')
    plt.text(66, 44, 'p', size='small')
    plt.text(63, 29, 'p1', size='small')
    plt.text(45, 66, 'dp', size='small')
    plt.text(41, 26, 'r')
    plt.text(3, 17, '(xc, yc))', size='small')
    plt.plot([xc + r * np.cos(phi3), xc + r * np.cos(phi3)],
             [yc - 8, yc + r * np.sin(phi3)], 'k:')
    plt.plot([xc, xc], [yc - 2, yc - 8], 'k:')
    plt.text(25, 17, 'R*cos(p)', size='small')

    plt.plot([xc - 8, xc + r * np.cos(phi3)],
             [yc + r * np.sin(phi3), yc + r * np.sin(phi3)], 'k:')
    plt.plot([xc - 2, xc - 8], [yc, yc], 'k:')
    plt.text(13, 37, 'R * sin(p)', size='small', rotation=90)

    plt.text(49, 30, '(x1,y1)', size='small')
    plt.text(20, 62, '(x2,y2)', size='small')
    plt.text(51, 49, '(xp,yp)', size='small')

    # Arrow heads
    plt.arrow(47, 79, -2, 1, head_length=3, head_width=2, color='k')
    plt.arrow(62, 53, -2, 2, head_length=2.9, head_width=2, color='k')
    plt.arrow(64, 31, -.9, 3, head_length=2, head_width=2, color='k')
    plt.arrow(52, 63, 3, -3, head_length=2, head_width=2, color='k')

    plt.show()


main()
