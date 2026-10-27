#lab-04: Study and Simulation of the 2D Radiation Pattern of a Linear Antenna Array 
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, np.pi, 800)
N = 10
d = 0.5
k = 2*np.pi

num = np.sin(N * k * d * np.cos(theta) / 2)
den = N * np.sin(k * d * np.cos(theta) / 2)
AF = np.abs(num / den)

ax = plt.subplot(111, projection="polar")
ax.plot(theta, AF)
ax.set_title("Linear Antenna Array (2D)\n")
plt.show()
