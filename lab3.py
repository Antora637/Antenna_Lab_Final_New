# Horn Antenna - 3D
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, np.pi/2, 250)    # শুধু সামনের hemisphere
phi = np.linspace(0, 2*np.pi, 250)
theta, phi = np.meshgrid(theta, phi)

n = 6
R = np.cos(theta)**n                    # এখানে abs লাগে না, cos ≥ 0

X = R * np.sin(theta) * np.cos(phi)
Y = R * np.sin(theta) * np.sin(phi)
Z = R * np.cos(theta)

ax = plt.figure().add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap="inferno")
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(0, 1)
ax.set_title("Horn Antenna (3D)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()