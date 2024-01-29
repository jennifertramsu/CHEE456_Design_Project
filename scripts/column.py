import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 0.9
V0 = 2
X = 2
Y = 5
mu = 5
K = 1
m = 1
delta = 0.001

# Function definition
def dCgdz(Cg, z):
    return -alpha / V0 * X / Y * mu * Cg / m / (K + Cg / m) * delta

# Initial condition
Cg0 = 0.000195 # mg/l NH3

# Integration grid
z = np.linspace(0, 5, 100)

# Solve ODE
y = scipy.integrate.odeint(dCgdz, Cg0, z)

# Plot
plt.plot(z, y / Cg0)
plt.xlabel('z [m]')
plt.ylabel('Cg [g/L]')
plt.show()