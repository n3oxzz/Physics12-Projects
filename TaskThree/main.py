#Coding project 3

# For xi=0 and vi=+3m/s, a 5 kg mass and a k=100 horizontal spring on a frictionless surface, find an expression for the acceleration. Then use the Euler method to calculate a list of x and v. In your loop also create a list of times. (Times[i+1]=times[i]+dt).  Graph x-t and v-t for several cycles.
import matplotlib.pyplot as plt
import pandas as pd

x0 = 0
v0 = 3

m = 5
k = 100

dt = 0.01

# F = -kx
# F = ma
# a = -kx/m
# Vn+1 = Vn + (an*dt)

def findAccel(x, k=k, m=m):
    return -k * x / m

def findVel(v, a, dt=dt):
    return v + a * dt

def findDist(x, v, dt):
    return x + v * dt

xs = [x0]
vs = [v0]
ts = [0.0]

x = x0
v = v0
t = 0.0
for i in range(0, 1400):
    a = findAccel(x)
    v_old = v
    v = findVel(v, a, dt)
    x = findDist(x, v_old, dt)
    vs.append(v)
    xs.append(x)
    t+=dt
    ts.append(t)
    
df = pd.DataFrame({
    "t": ts,
    "V": vs,
    "x": xs
})

df.to_csv("results.csv", index=False)

#plots

plt.plot(ts, vs, label="Velocity", color="green")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Time")
plt.grid(True)
plt.show()

plt.plot(ts, xs, label="Position", color="red")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid(True)
plt.show()

