import plotly.graph_objects as go
import numpy as np

# Constants
alpha = 1/137
hbar = 1.054571817e-34 # J.s
c = 299792458 # m/s
e = 1.602176634e-19 # C
a0 = 5.29177210903e-11 # m (Bohr radius)
me = 9.10938356e-31 # kg (electron mass)
n = 3 # Principal quantum number
j = 1/2 # Total angular momentum quantum number
l = 1 # Orbital angular momentum quantum number
S = 0.5 # Spin quantum number
m = 1 # Magnetic quantum number

# Energy levels
delta_E = np.zeros(5)
for k in range(1, 6):
    delta_E[k-1] = -alpha**2 * me * c**2 / (32 * np.pi**2 * hbar**3 * k**3 / (n**2 * a0**4))

# Electric field strength
E = np.linspace(0, 0.05, 1000)

# Energy shift due to Stark effect
delta_E_stark = np.zeros((5, len(E)))
for k in range(1, 6):
    for i in range(len(E)):
        delta_E_stark[k-1][i] = alpha * (n/(j+0.5))**4 * E[i]

# Total energy levels
E_total = np.zeros((5, len(E)))
for k in range(1, 6):
    E_total[k-1] = delta_E[k-1] + delta_E_stark[k-1]

# Plot energy shift due to Stark effect
fig = go.Figure()
for k in range(1, 6):
    fig.add_trace(go.Scatter(x=E, y=delta_E_stark[k-1], name=f'k={k}'))

fig.update_layout(title=f'Stark effect in hydrogen: n={n}, l={l}, S={S}, j={j}, m={m}',
                  xaxis_title='Electric field strength (V/m)',
                  yaxis_title='Energy shift (J)',
                  legend_title='k')
fig.show()

# Plot total energy levels
fig = go.Figure()
for k in range(1, 6):
    fig.add_trace(go.Scatter(x=E, y=E_total[k-1], name=f'k={k}'))

fig.update_layout(title=f'Stark effect in hydrogen: n={n}, l={l}, S={S}, j={j}, m={m}',
                  xaxis_title='Electric field strength (V/m)',
                  yaxis_title='Energy (J)',
                  legend_title='k')
fig.show()
