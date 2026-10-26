# Two Isotropic Point Sources (Opposite Phase)

import numpy as np
import matplotlib.pyplot as plt

# Parameters
lam = 1.0
d = lam / 2
k = 2 * np.pi / lam

# Angle range
theta = np.linspace(0, 2*np.pi, 1000)

# Array Factor (Opposite Phase)
AF = 2 * np.sin((k * d / 2) * np.cos(theta))

# Normalize
AF_norm = np.abs(AF) / np.max(np.abs(AF))

# Plot
plt.figure(figsize=(6, 6))
plt.polar(theta, AF_norm)
plt.title("Far-Field Pattern\nTwo Isotropic Sources (Opposite Phase)\n(d = λ/2)")
plt.show()