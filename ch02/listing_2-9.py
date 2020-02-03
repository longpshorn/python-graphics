#!/usr/local/bin/python3

"""
2DTRANSLATION
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_grid(extents, axis_on='on', plot_grid=True):
    plt.axis(extents)
    plt.axis(axis_on)
    plt.grid(plot_grid)


def main():
    plot_grid([-10, 140, 90, -10], 'on', True)
    plt.title('Translation')

    # Triangle
    x = [20, 30, 40, 20]
    y = [40, 20, 40, 40]
    plt.plot(x, y, color='k')
    plt.plot(x, y, color='k')
    plt.plot(x, y, color='k')

    # Translate triangle dx=60
    x = [60, 70, 80, 60]
    plt.plot(x, y, color='g')
    plt.plot(x, y, color='g')
    plt.plot(x, y, color='g')

    # Translate triangle dy=40
    y = [80, 60, 80, 80]
    plt.plot(x, y, color='r')
    plt.plot(x, y, color='r')
    plt.plot(x, y, color='r')

    # Box
    x = [0, 0, 5, 5, 0]
    y = [55, 50, 50, 55, 55]
    plt.plot(x, y, 'b')

    # Translate box
    y = [55, 50, 50, 55, 55]
    for x in np.arange(0, 130, 10):
        x = [x, x, x + 5, x + 5, x]
        plt.plot(x, y, 'b')

    plt.show()


main()
