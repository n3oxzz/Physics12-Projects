# 6. Consider a 20 degree ramp 10m high with friction μ=0.1 and a 5 kg mass that starts at rest at the top. Use F=ma and Python to calculate v,KΕ,PΕ,E,Q,TE at 2 m intervals of height and create a bar graph by hand excel or python to illustrate the principle. Note: do not (emphasis) use energy conservation to do these calculations since that is the conclusion we wish to verify, instead use force analysis as indicated

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

hl=[10, 8, 6, 4, 2, 0]
mu = 0.1
angle = np.deg2rad(20)
g = 9.8
m = 5
h=10
a = g*np.sin(angle) - mu * g * np.cos(angle)

Fn = m * g * np.cos(angle)
Ff = Fn * mu

# velocity
def findV(Vi, dx, a=a):
    return np.sqrt(Vi**2 + (2*a*dx))

# kinetic energy
def findKE(V):
    return (m * V**2) / 2
 
 #potential energy
def findPE(h):
    return m * g * h

# mechanical energy
def findE(KE, PE):
    return KE + PE

# heat (absolute)
def findQ(dx):
    return Ff * dx

# total energy
def findTE(KE, PE, Q):
    return KE + PE + Q

heights = []
vels = []
KEs = []
PEs = []
Es = []
Qs = []
TEs = []

prev_h = h

V=0.0
Q=0.0

for i in hl:
    heights.append(i)
    dx = (prev_h-i) / np.sin(angle)
    Vi = V
    V = findV(Vi, dx); vels.append(V) 
    KE = findKE(V); KEs.append(KE)
    PE = findPE(i); PEs.append(PE)
    E = findE(KE, PE); Es.append(E)
    Q += findQ(dx); Qs.append(Q)
    TE = findTE(KE, PE, Q); TEs.append(TE)
    print(f"At height {i}: Velocity = {V}\tKinetic energy = {KE}\tPotential energy = {PE}\tMechanical energy = {E}\tHeat energy = {Q}\tTotal energy = {TE}\n")
    prev_h = i


df = pd.DataFrame({
    "h": heights,
    "V": vels,
    "KE": KEs,
    "PE": PEs,
    "E": Es,
    "Q": Qs,
    "TE": TEs,
})

df.to_csv("results.csv", index=False)

plt.plot(heights, vels, label="Velocity", color="green")
plt.xlabel("Height (m)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Height")
plt.grid(True)
plt.gca().invert_xaxis()
plt.show()

plt.plot(heights, KEs, label="Kinetic Energy", color="blue")
plt.plot(heights, PEs, label="Potential Energy", color="green")
plt.plot(heights, Es, label="Mechanical Energy", color="purple")
plt.plot(heights, Qs, label="Heat Energy", color="red")
plt.plot(heights, TEs, label="Total Energy", color="black")
plt.xlabel("Height (m)")
plt.ylabel("Energy (J)")
plt.title("Energies vs Height")
plt.legend()
plt.grid(True)
plt.gca().invert_xaxis()
plt.show()
