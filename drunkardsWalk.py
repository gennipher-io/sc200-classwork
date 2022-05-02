#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Drunkard's walk simulation
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

#Plot starting point, (x,y) = (0,0)
#Loop over your number of steps
#Generate new theta in [0, 2pi]
#Plot new x,y coordinates

n = 1000 #number of steps
start_x = 0 #starting x coordinate
start_y = 0 #starting y coordinate
theta = 0 #theta is your angle that you will step out at

plt.xlim([-10,10])
plt.ylim([-10,10])
plt.plot(start_x,start_y)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Drunkards Walk')

for i in range(n):
    #theta = np.random.randint(0, 2*np.pi) #generate a new angle to step out at, don't use this....
    theta = 2*np.pi*np.random.rand() #this will generate any real number in the interval 0 - 2pi ([0, 2pi])
    new_x = start_x + np.cos(theta) #starting from your origin x, step out new x
    new_y = start_y + np.sin(theta) #starting from your origin y, step out new y
    
    start_x = new_x #put a marker for the steps
    start_y = new_y #put a marker for your steps
    
    plt.scatter(new_x,new_y) #plot your new position

    n += 1 #increment your steps

distance = np.sqrt(new_x**2 + new_y**2) #distance formula = sqrt[(x2 -x1)**2 + (y2 -y1)**2]
print('Distance traveled:', distance)
distance_sq = new_x**2 + new_y**2
print('Distance squared:', distance_sq)


# In[ ]:




