# Dipole Antenna - 3D Radiation Pattern

import numpy as np
import matplotlib.pyplot as plt

# Angle values
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)

# Create coordinate grids
theta, phi = np.meshgrid(theta, phi)

# Simplified normalized radiation pattern
R = np.abs(np.sin(theta))

# Convert spherical coordinates to Cartesian coordinates
X = R * np.sin(theta) * np.cos(phi)
Y = R * np.sin(theta) * np.sin(phi)
Z = R * np.cos(theta)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot the radiation surface
ax.plot_surface(X, Y, Z)

# Add title and axis labels
ax.set_title("3D Radiation Pattern of Dipole Antenna")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Display the plot
plt.show()