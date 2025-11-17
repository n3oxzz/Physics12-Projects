import numpy as np, matplotlib.pyplot as plt

height = 30
v = 20.5
theta = np.deg2rad(25)

flght_t = 4
fig, axis = plt.subplots()

for t in np.arange(0, flght_t, 0.1):
    x = np.cos(theta) * v * t
    y = height + np.sin(theta) * v * t - 4.9*(t**2)
    axis.plot(x, y, 'go', markersize='2')

for x in np.arange(-3, 0, 0.01):
    y = 30
    axis.plot(x, y, 'o', markersize='2')
for y in np.arange(0, 30, 0.01):
    x = 0
    axis.plot(x, y, 'o', markersize='2')

for x in np.arange(0, 50, 0.01):
    y = 0
    axis.plot(x, y, 'o', markersize='2')

for y in np.arange(0, 8, 0.1):
    x = 50
    axis.plot(x, y, 'o', markersize='2')

for x in np.arange(50, 58, 0.01):
    y = 8
    axis.plot(x, y, 'o', markersize='2')

for y in np.arange(8, 12, 0.01):
    x = 58
    axis.plot(x, y, 'o', markersize='2') 



plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.title('Projectile motion')
plt.show()
