# Coding Task 4
# Consider a rocket of mass 10 tonnes with 5 tonnes of fuel initially at rest in deep space (no gravity). Fuel burns at rate 2 kg/s and the gas products are ejected backwards at speed u=1000m/s relative to the rocket. Use the Euler method to plot v(t) for the rocket if we burn until the remaining fuel is down to 2 tonnes.
# Note: consider a small element of fuel that will burn in time dt.
#        it's mass is:
#        the remaining fuel mass is: m= m 
#        it's velocity change upon burning is: the force that the rocket (engine) exerts on the fuel is:
# Now apply Newton's third law to find the force on the rocket.
# As part of your code you will need to track the decreasing mass of the rocket.

import matplotlib.pyplot as plt

dt = 0.1 #time step is small (s)
m0 = 5e3 #initial fuel mass
M = 1e4#rocket mass when empty
fuelRate = 2#kg/s burn rate
u = 1000 #m/s fuel ejection relative speed
v = 0 #rocket speed
t = 0 #time
m = m0

#dm = fuelrate * dt

#dv = (u*dm)/Mtotal

vs = [u]
ts = [t]

while m>2000:            
   dm = fuelRate * dt
   m -= dm #fuel mass after burn 
   Mtotal = M + m #rocket and fuel
   dv = u * dm / Mtotal
   v+=dv; vs.append(v)
   t+=dt; ts.append(t)

plt.plot(ts, vs, label="Velocity", color="green")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Time")
plt.grid(True)
plt.show()


