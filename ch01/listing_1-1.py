#!/usr/local/bin/python3

import numpy as np
import matplotlib.pyplot as plt


def main():
    x1 = -10
    x2 = 10
    y1 = 10
    y2 = -10

    plt.axis([x1, x2, y1, y2])
    plt.axis('on')
    plt.grid(True)
    plt.show()


main()
