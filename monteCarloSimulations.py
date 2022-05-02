#Gennipher Ricks
#SC 200 Module 4a, 4b
#Programming Assignment
#04/08/2022

#EXAMPLE 1: Estimate the area under the curve
#f(x) = sqrt(x)
#by choosing random points in the
#interval 1/2 <= x <= 3/2

import numpy as np
import matplotlib.pyplot as plt

#Set your trial n at high enough value to reach area approximation
n = 100000  

#Set your bounds from the instructions above for x and y
a = 1/2 
b = 3/2 

#Set your upper bound
M = np.sqrt(b)

#Initialize your area counter
counter = 0

#Create your x and y values from your instructions
x = np.linspace(0, 2, 100)
y = np.sqrt(x)

#Create your figure plot windows
plt.figure(1)
plt.subplot()

#Plot your function from 0 - 2
plt.plot(x,y)

#Plot your first bound
plt.plot(a, np.sqrt(a), '*', color="red", markersize=7)

#Plot your second bound
plt.plot(b, np.sqrt(b), '*', color="red", markersize=7)

#Add a title, labels and legend to your plot
plt.title('Function f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Function','First Bound', 'Second bound'])

#Add some fancy shading to visualize the area in question (literally :D)
plt.fill_between(x, y, where=((x >= a) & (x <= b)), color='pink')

#Add gridlines and show your plot
plt.grid()
plt.show()

#Create your function to evaluate points under the curve
for i in range(n): 
    
    #Pick a random point for x and y in your given interval
    x = a + (b-a)*np.random.rand() 
    y = a + (b-a)*np.random.rand()
    
    #Check if the point is below the surface(area) and increment your counter
    if y <= np.sqrt(x): 
        counter += 1 
    
#After you get some approximation of points below the surface 
#of the curve, calculate your area
area = (M * (b-a) * counter)/n

#Display your answer for Example 1
print('The area under the curve f(x) = sqrt(x) is:', area)


# In[42]:


#EXAMPLE 2: Use Monte Carlo simulation to 
#calculate the volume bounded by:
# z = 1 - 1/2x^2 - 1/2y^2

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

#Define your function for this example
def f(v):
    return 1 - .5*v[0]**2 - .5*v[1]**2

#Create a 3d figure plot 
plt.figure()
ax = plt.axes(projection = '3d')

#Set up your 3d grid area and plot your function
x = np.linspace(0, 2, 1000)
y = np.linspace(0, 2, 1000)

#Create your meshgrid and plot your surface plot
X,Y = np.meshgrid(x,y)
Z= f([X,Y])
ax.plot_surface(X,Y,Z)

#Add a title and labels
plt.title('Function z')
plt.xlabel('x')
plt.ylabel('y')

#Set your trial n at high enough value to reach volume approximation
n = 1000000 

#Set your bounds from the instructions above for x and y
a = 0
b = 1

#Use c and d so you can code to a non-box shape
c = 0
d = 1

#Set your upper bound
M = 1 

#Initialize your volume counter
counter = 0

##Create your function to evaluate points under the curve
for i in range(n):
    
    #Pick a random point for x, y and z in your given interval
    x = a + (b-a)*np.random.rand()
    y = c + (d-a)*np.random.rand()
    z = M*np.random.rand() 
    
    #Check if the point is below the surface(volume) and increment your counter
    if z <= 1 - .5*x**2 - .5*y**2:
        counter += 1

#After you get some approximation of points below the surface 
#of the curve, calculate your volume
volume = (b-a) * (d-c) * M * counter/n 

#Display your answer for Example 2
print('The volume bounded by z = 1 - 1/2x^2 - 1/2y^2 is:', volume)

