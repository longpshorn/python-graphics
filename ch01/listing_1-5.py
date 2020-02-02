#!/usr/local/bin/python3

import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 150, 0, 100])

plt.scatter(60, 50, s=1000, color='b', alpha=1)
plt.scatter(80, 50, s=1000, color='b', alpha=.5)
plt.scatter(100, 50, s=1000, color='b', alpha=.1)

plt.show()
