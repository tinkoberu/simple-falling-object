import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
y1 = 50
vy = 0
g = -9.8

time =10
dt = 0.1;
n = int(round(time/dt))
t = np.linspace(0,10,n) # time axis with n-points
y = 0+y1*t-0.5*9.8*t**2 # height equation

plt.plot(t, y, color ='m')
plt.title('Position vs Time')

# Add X and y Label
plt.xlabel('t (sec)')
plt.ylabel('y (meters)')

# Add a grid
plt.grid(alpha=.4,linestyle='--')

# Show the plot
plt.show()

df.to_excel('saved_file.xlsx', index = False)