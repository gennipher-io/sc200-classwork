#Gennipher Ricks
#SC 200 Module 5a, 5b
#Programming Assignment
#04/26/2022

# Create a Python function, dist(), 
# which takes no inputs, generates 4 random
# numbers between 0 and 1 (x1, x2, y1, y2), 
# and returns the distance between the points
# (x1, y1) and (x2, y2). Call the function
# 1000 times in parallel.

import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import math
import timeit
import multiprocessing
from joblib import Parallel, delayed #delayed prevents it from passing everything to your first core

# Initialize your number of executions and your empty list 
n = 1000
dist = n*[0]

# Define your function that generates 4 random numbers and calculates the distance between
# the corresponding x and y points
def dist():
    # Generate 4 random floats and round them to 4 decimal places
    x1 = round(rand.uniform(0, 1), 4)
    y1 = round(rand.uniform(0, 1), 4)
    x2 = round(rand.uniform(0, 1), 4)
    y2 = round(rand.uniform(0, 1), 4)
    
    # Calculate the distance between the 2 points and round that to 4 decimal places
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 4)

# Get number of cores available to you and display them
num_cores = multiprocessing.cpu_count()
print('Number of cores available:', num_cores) 
print()

# Start your timer to see how long the parallel execution takes
start = timeit.default_timer()

# Run your function 1000 times and store the returned distance into your list
dist = Parallel(n_jobs = num_cores)(delayed(dist)() for i in range(1, n+1))

# Display the total time it took to run your parallel execution
print('Total time to execute:', timeit.default_timer() - start)
print()

# Print all of your calculated distances
print('Your 1000 calculated distance values are:')
print(dist)
