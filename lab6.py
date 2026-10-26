# Two Isotropic Point Sources (Equal Amplitude & Phase)

import numpy as np
import matplotlib.pyplot as plt

# Parameters
lam = 1.0
d = lam / 2
k = 2 * np.pi / lam

# Angle range
theta = np.linspace(0, 2*np.pi, 1000)

# Array Factor
AF = 2 * np.cos((k * d / 2) * np.cos(theta))

# Normalize
AF_norm = np.abs(AF) / np.max(np.abs(AF))

# Plot
plt.figure(figsize=(6, 6))
plt.polar(theta, AF_norm)
plt.title("Far-Field Pattern\nTwo Isotropic Point Sources\nEqual Amplitude & Phase (d = λ/2)")
plt.show()