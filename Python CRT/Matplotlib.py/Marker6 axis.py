import numpy as np
import matplotlib.pyplot as plt
x=np.array([80,85,90,95,100,105,110])
y=np.array([240,250,260,270,280,290,300])
plt.plot(x,y)
plt.title("Sports watch data",loc='right')#loc for position
plt.xlabel("Average pilse")
plt.ylabel("Calorie Burnage")
plt.show()

plt.plot(x,y)
plt.grid(axis='x',color='green',linestyle='--',linewidth='1')
plt.show()