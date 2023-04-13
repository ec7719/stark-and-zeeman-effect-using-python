import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Define constants
h = 6.626e-34     # Planck's constant
c = 3e8           # Speed of light
m_e = 9.11e-31    # Mass of electron
e = 1.6e-19       # Elementary charge
B = 1             # Magnetic field strength
E = np.linspace(0, 5e5, 1000)  # Electric field strength

# Calculate Zeeman effect
g_j = 1.5        # Landé g-factor
J = 2            # Total angular momentum quantum number
m_j = np.arange(-J, J+1, 1)  # Magnetic quantum number
mu_B = 9.27e-24  # Bohr magneton
delta_E = g_j*mu_B*B*m_j

# Calculate Stark effect
n = 4           # Principal quantum number
l = 2           # Orbital angular momentum quantum number
j = 1.5         # Total angular momentum quantum number
s = 0.5         # Spin quantum number
g_L = 1         # Landé g-factor for orbital angular momentum
g_S = 2         # Landé g-factor for spin
g_j = (g_L*(j*(j+1) + l*(l+1) - s*(s+1))/(2*j*(j+1)) + g_S*(j*(j+1) + s*(s+1) - l*(l+1))/(2*j*(j+1)))  # Total Landé g-factor
alpha = e**2/(4*np.pi*8.854e-12)  # Electric constant
delta_E = [0]*1000
for i in range(5):
    delta_E += alpha*(n/(j+0.5))**4*E[i]


# Plot Zeeman effect
fig, ax = plt.subplots()
for m in m_j:
    ax.plot(E, delta_E[m_j==m]/e, label=f"$m_j={m}$")
ax.set_xlabel("Electric field strength (V/m)")
ax.set_ylabel("Energy shift (eV)")
ax.set_title("Zeeman Effect")
ax.legend()

# Plot Stark effect
fig2, ax2 = plt.subplots()
for l in range(j, -1, -1):
    for m in np.arange(-l, l+1, 1):
        ax2.plot(E, delta_E[(l, m)]/e, label=f"$l={l}, m_l={m}$")
ax2.set_xlabel("Electric field strength (V/m)")
ax2.set_ylabel("Energy shift (eV)")
ax2.set_title("Stark Effect")
ax2.legend()

plt.show()
