# Linear Antenna Array - 2D Radiation Pattern

import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 8                 # Number of elements
d = 0.5               # Spacing (lambda / 2)
k = 2 * np.pi         # Wave number
beta = 0              # Phase difference

# Angle
theta = np.linspace(0, 2 * np.pi, 1000)

# Array Factor
AF = np.zeros_like(theta, dtype=complex)

for n in range(N):
    AF += np.exp(1j * n * (k * d * np.cos(theta) + beta))

# Magnitude
AF = np.abs(AF)

# Normalize
AF = AF / np.max(AF)

# Plot
ax = plt.subplot(111, projection="polar")
ax.plot(theta, AF)

ax.set_title("Linear Antenna Array (2D)")

plt.show()