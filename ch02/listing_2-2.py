#!/usr/local/bin/python3

"""
DOTART
"""

import numpy as np
import matplotlib.pyplot as plt
import random


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


def plot_scatter_simple(xmin, xmax, dx, ymin, ymax, dy=1, dot_size=8, dot_color='b'):
    for x in np.arange(xmin, xmax, dx):
        for y in np.arange(ymin, ymax, dy):
            plt.scatter(x, y, s=dot_size, color=dot_color)


def plot_scatter_klee(xmin, xmax, dx, ymin, ymax, dy=2, dot_size=25, color_min=0, color_max=100, dcolor=1):
    for x in np.arange(xmin, xmax, dx):
        for y in np.arange(ymin, ymax, dy):
            rr = random.randrange(color_min, color_max, dcolor) / color_max
            rg = random.randrange(color_min, color_max, dcolor) / color_max
            rb = random.randrange(color_min, color_max, dcolor) / color_max
            plt.scatter(x, y, s=dot_size, color=(rr, rg, rb))


def main():
    plot_grid([-10, 140, 90, -10], 'off', False)

    plot_reference_frame()

    # Plot Seurat
    plot_scatter_simple(20, 40, 4, 10, 60, 4, 8, 'b')
    plt.text(21, 67, 'Seurat')

    # Plot Mondrian
    plot_scatter_simple(60, 80, 1, 10, 40, 1, 8, 'y')
    plot_scatter_simple(60, 80, 1, 40, 60, 1, 8, 'g')
    plot_scatter_simple(65, 80, 1, 25, 30, 1, 8, 'b')
    plt.scatter(70, 30, s=50, color='r')
    plt.text(60, 67, 'Mondrian')

    # Plot Klee
    plot_scatter_klee(100, 120, 2, 10, 60, 2, 25, 0, 100, 1)
    plt.text(105, 67, 'Klee')

    plt.show()


main()
