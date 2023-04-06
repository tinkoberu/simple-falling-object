import math
import pandas as pd
import matplotlib.pyplot as plt 

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
rho = 1.225  # Air density (kg/m^3)
Cd = 0.5  # Drag coefficient
A = 0.01  # Cross-sectional area (m^2)

# Input parameters
v0 = 100  # Initial velocity (m/s)
theta = math.radians(45)  # Launch angle (radians)
x0 = 0  # Initial x-position (m)
y0 = 0  # Initial y-position (m)
dt = 0.01  # Time step (s)
tmax = 10  # Maximum time (s)

# Calculate trajectory
x = [x0]
y = [y0]
vx = v0 * math.cos(theta)
vy = v0 * math.sin(theta)

while y[-1] >= 0 and len(x) < tmax / dt:
    v = math.sqrt(vx**2 + vy**2)
    ax = -rho * Cd * A * v * vx / 2
    ay = -g - rho * Cd * A * v * vy / 2
    vx += ax * dt
    vy += ay * dt
    x.append(x[-1] + vx * dt)
    y.append(y[-1] + vy * dt)

time = [i * dt for i in range(len(x))]

plt.plot(time,y, color ='m')
# Add X and y Label
plt.xlabel('t (sec)')
plt.ylabel('y (meters)')
plt.show()

# Save results to Excel
data = {'Time': [i * dt for i in range(len(x))], 'X': x, 'Y': y, 'V': v, 'ax':ax, 'ay':ay,'vx':vx, 'vy':vy}
df = pd.DataFrame(data)
df.to_excel('trajectory.xlsx', index=False)

directory_path = 'E:\BRATI\latihan'
file_name = 'my_data1.xlsx'
full_file_path = f'{directory_path}/{file_name}'
df.to_excel(full_file_path, index=False)
