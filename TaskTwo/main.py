# Coding project 2. For the 50 km jump from space, plot a graph of v(h) for 
# i) free fall:  a=-9.8
# ii) free fall with varying field strength: a=-GM/(r+h)2 where r= earth radius = 6.38e6 and h is the current altitude
# iii) gravity and quadratic drag a= -GM/(r+h)**2  +.  Cv*2 where C was given in class is the constant drag co-efficient and v is the current speed
# iv) gravity and quadratic drag with a varying air density:  a= -GM/(r+h)**2  +.  C. exp(-h/H)  v*2. where H=10000m and h is the current altitude
import numpy as np
import matplotlib.pyplot as plt

#constants
g = 9.81
R = 6.38e6 # Earth radius [m]
GM = g * R**2 # Choose GM such that g at surface is 9.81
h0 = 52_000.0 # initial altitude [m]
v0 = 0.0 # initial velocity (jumping off, start at rest relative to air)
dt = 0.1 # time step [s]
H = 10_000.0 # scale height for air density [m]
C_base = g / (55.0**2) # ~0.00324 so terminal speed at sea level ~55 m/s with a = -C v|v|

def simulate(accel_fn, h0=h0, v0=v0, dt=dt, h_stop=0.0, max_steps=2_000_000):
    h = h0
    v = v0
    hs = [h]
    vs = [v]
    steps = 0

    while h > h_stop and steps < max_steps:
        a = accel_fn(h, v)
        v =  v + a*dt
        h = h + v*dt
        hs.append(h)
        vs.append(v)
        steps+=1
    return np.array(hs), np.array(vs)

# (i) free fall
def a_const_g(h, v):
    return -g
# (ii) var gravity
def a_var_g(h , v):
    return -GM / (R+h)**2
# (iii) var gravity + const density drag
def a_var_g_const_drag(h, v, C=C_base):
    # Drag opposes motion: -C * v * |v|
    return -GM / (R+h)**2 - C*v*abs(v)
# (iv) var gravity + varying density drag
def a_var_g_var_drag(h, v, C0=C_base, H=H):
    rho_rel = np.exp(-h/H)
    return -GM / (R+h)**2 - (C0 * rho_rel) *v * abs(v)

h1, v1 = simulate(a_const_g)
h2, v2 = simulate(a_var_g)
h3, v3 = simulate(a_var_g_const_drag)
h4, v4 = simulate(a_var_g_var_drag)

def plot(hs, vs, label):
    plt.figure()
    plt.plot(hs/1000.0, np.abs(vs), label=label)
    # plt.gca().invert_xaxis
    plt.xlabel("Altitude h (km)")
    plt.ylabel("Speed |v| (m/s)")
    plt.title(label)
    plt.grid(True)
    plt.legend()
    plt.show()

plot(h1, v1, "(i) free fall, constant g")
plot(h2, v2, "(ii) free fall, variable g")
plot(h3, v3, "(iii) var gravity + quadratic drag (const rho)")
plot(h4, v4, "(iv) var gravity + quadratic drag (exp. rho)")