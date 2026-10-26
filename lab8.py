# Two Isotropic Sources (Unequal Amplitude + Opposite Phase)
import numpy as np
import matplotlib.pyplot as plt

# Parameters
lam = 1.0
d = lam / 2
k = 2 * np.pi / lam

# Amplitude weights
A1 = 1
A2 = 0.5  # Unequal amplitude

# Angle range
theta = np.linspace(0, 2*np.pi, 1000)

# Array Factor
AF = A1 - A2 * np.exp(1j * k * d * np.cos(theta))

# Normalize
AF_norm = np.abs(AF) / np.max(np.abs(AF))

# Plot
plt.figure(figsize=(6,6))
plt.polar(theta, AF_norm)
plt.title("Far-Field Pattern\nUnequal Amplitude + Opposite Phase\n(d = λ/2)")
plt.show()