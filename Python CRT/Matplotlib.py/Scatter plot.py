#creating  scatter plot
#with Pyplot,you can use the scatter() function to draw a graph
import matplotlib.pyplot as  plt
import numpy as np
x=np.array([5,7,4,2,1])
y=np.array([6,9,10,15,21])
plt.scatter(x,y)
plt.show()

#color
plt.scatter(x,y,color='green')
