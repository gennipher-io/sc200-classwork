#Gennipher Ricks
#SC 200 Module 4c, 4d
#Programming Assignment
#04/14/2022

#Evaluate the campus dining experience at Southeastern.
#Using Python, determine the long-term percentages of
#eating at each dining hall: Mane Dish, Panda Express,
#and Chick-fil-A; assuming that 100% of students all
#chose Panda Express initially. Also observe the long-term
#percentages for different initial conditions in your notes.

import numpy as np
import matplotlib.pyplot as plt

#Initialize your variable for the number of cycles/trials you will run
n = 6 # num of cycles

#Initialize your empty lists the size of your trials
Mane = (n+1)*[0]
Chick = (n+1)*[0]
Panda = (n+1)*[0]

#Initially, 100% of students eat at Panda Express
Mane[0] = 0
Chick[0] = 0
Panda[0] = 1

#Set your tolerance, the higher the precision the longer it takes to achieve equilibrium
tol = 10**-2

#Initialize an empty list for tracking when you achieve equilibrium
equilibrium = []

#Setup your for loop to execute the number of times you have your trials/cycles set to
for i in range(n):
    #Set up your Markov Chain for each dining hall
    Mane[i+1] = 0.25*Mane[i] + 0.10*Chick[i] + 0.05*Panda[i]
    Chick[i+1] = 0.25*Mane[i] + 0.3*Chick[i] + 0.15*Panda[i]
    Panda[i+1] = 0.5*Mane[i] + 0.6*Chick[i] + 0.8*Panda[i]
    
    #Check if you've met equilibrium and add the cycle you are at to your list
    if abs(Mane[i+1]-Mane[i]<=tol) and abs(Chick[i+1]-Chick[i]<=tol)     and abs(Panda[i+1]-Panda[i]<=tol):
        equilibrium.insert(1, i)

cycles = np.arange(0,n+1,1)

#Plot your probabilities
plt.plot(cycles, Mane)
plt.plot(cycles, Chick)
plt.plot(cycles, Panda)

#Add a title, labels and legend to your plot
plt.title('Campus Dining Behaviors of Southeastern Students')
plt.legend(['Mane Dish', 'Chick-Fil-A', 'Panda Express'])
plt.xlabel('Times Dined Out')
plt.ylabel('Dining Hall Probability')
plt.show()

#Print what cycle you reached equilibrium at
print('Equilibrium reached after', min(equilibrium), 'cycles!')
print()

#Print your observations from changing initial starting values
print('Changing your initial observations affect the number of trials/cycles ')
print('that it takes to reach equilibrium. ')
print()
print('For instance, if you weight Panda Express at the lowest initial observation')
print('it takes about 7 cycles to reach equilibrium.')
print()
print('Additionally, if you change your tolerance to a higher precision,')
print('it will take you slightly longer to reach equilibrium.')
