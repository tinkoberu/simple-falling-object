import math
import matplotlib.pyplot as plt
import pandas as pd
# Constants
g = 9.81   # acceleration due to gravity (m/s^2)
m = 1      # mass of the ball (kg)
dt = 0.1  # time step (s)
Kp = 0.001  # proportional gain
Ki = 0.001   # integral gain
Kd = 0    # derivative gain
Cd = 0.47 # drag coefficient of the ball
rho = 1.2 # density of air (kg/m^3)
A = math.pi * 0.02**2 # cross-sectional area of the ball (m^2)
v0 = 0 # initial velocity (m/s)
y0 = 50 # initial height (m)
dt = 0.01 # time step (s)

# Initial conditions
h0 = 50  # initial height (m)
v0 = 0   # initial velocity (m/s)

# Setpoint
h_setpoint = 10  # desired height (m)

# PID controller
error = h_setpoint - h0
integral = 0
derivative = 0

# Lists for storing data
times = [0]
heights = [h0]
velocities = [v0]
accel = [0]
cs=[0]
er=[0]

# Simulation loop
while heights[-1] > h_setpoint:
    # Calculate drag force
    #Fd = 0.5 * Cd * rho * A * velocities[-1]**2

    # Calculate net force
    Fnet = m * g #- Fd
    
    # Calculate error, integral, and derivative
    error = h_setpoint - heights[-1]
    integral += error * dt
    derivative = (error - (heights[-1] - h_setpoint) / dt) / dt
    #print (error, integral, derivative)
   
    
    # Calculate control signal
    control_signal = Kp * error + Ki * integral + Kd * derivative
    #print (control_signal)

    # Apply braking acceleration
    Fnet += m * control_signal
   
    # Calculate acceleration
    #a = -g + control_signal / m
    a = Fnet / m
    
    # Update velocity and height
    #v = velocities[-1] + -a * dt
    #h = heights[-1] + v * dt
    velocities[-1] += a * dt
    heights[-1] -= velocities[-1] * dt
    
    # Add data to lists
    times.append(times[-1] + dt)
    heights.append(heights[-1])
    velocities.append(velocities[-1])
    accel.append(a)
    cs.append(control_signal)
    er.append(error)

# Plot results
plt.plot(times, heights)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.show()

plt.plot(times, velocities)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/2)')
plt.show()

data = {'waktu': times, 'kecepatan': velocities}
df=pd.DataFrame(data)
df.to_csv(r'E:\BRATI\latihan\PYTHON\bolajatuh2.csv', index=False)
