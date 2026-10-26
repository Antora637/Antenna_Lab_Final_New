import numpy as np
import matplotlib.pyplot as plt

# Define angles
theta = np.linspace(0, np.pi, 220)
phi = np.linspace(0, 2*np.pi, 240)

TH, PH = np.meshgrid(theta, phi)

# Approximate aperture effect
u = 10*np.sin(TH)*np.cos(PH)
v = 8*np.sin(TH)*np.sin(PH)

# Calculate approximate radiation pattern
E = np.abs(np.sinc(u/np.pi) * np.sinc(v/np.pi)) \
    * (1 + np.cos(TH))/2

# Normalize radiation values
E = E / E.max()

# Convert to dB scale and limit to -40 dB
E = np.maximum(
    20*np.log10(np.maximum(E, 1e-6)), -40
)

# Normalize values to the range 0 to 1
E = (E + 40) / 40

# Convert to Cartesian coordinates
X = E*np.sin(TH)*np.cos(PH)
Y = E*np.sin(TH)*np.sin(PH)
Z = E*np.cos(TH)

# Plot the 3D radiation pattern
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(X, Y, Z, cmap="inferno", linewidth=0)

ax.set_title("Approximate 3D Horn Antenna Pattern")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.set_box_aspect((1, 1, 1))
ax.set_zlim(-0.3, 1)

plt.tight_layout()
plt.show()