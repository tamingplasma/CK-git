#!/bin/python

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 150)
y = np.cos(x)

plt.plot(x,y,'.')
plt.show()
