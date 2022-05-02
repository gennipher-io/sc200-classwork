#Gennipher Ricks
#SC 200 Module 5a, 5b
#Programming Assignment
#04/24/2022

# Create a function, dist(), which takes no inputs, generates 4 random
# numbers between 0 and 1 (x1, x2, y1, y2), and returns the distance between 
# the points (x1, y1) and (x2, y2). Call the function 1000 times in parallel.

library('foreach')
library('doParallel')

# Define your function dist() and setup your equation
dist_func <- function(){
  
  # Generate your 4 random variables using runif()
  x1 <- runif(1) 
  y1 <- runif(1) 
  x2 <- runif(1) 
  y2 <- runif(1) 
  
  # Calculate the distance between the 2 points
  d <- sqrt((x2 - x1)**2 + (y2 - y1)**2)
  return(d)
}

# Set up your parallel variables
num_cores <- detectCores()
par_cores = 0


# Assign your parallel workers according to this logic
# If you have more than 2 cores, register half 
# If you have 2 or less cores, register all
if (num_cores > 2) {
  par_cores <- registerDoParallel(cores=round(num_cores/2))
  num_cores <- num_cores/2
} else {
  par_cores <- registerDoParallel(cores=num_cores)
}

# Now specifically register the right amount of cores
registerDoParallel(cores=par_cores)

# Create your vector to hold your distance values
vals <-c()

# Call the function 1000 times using a for loop and store all the 
# calculated distance values in a vector
dist_vals <- foreach(i = 1:1000) %dopar% {
  vals[i] <- dist_func()
}

# Print your results
dist_vals
print("These are your 1000 calculated distances above")
cat("Cores used for this parallel processing:", num_cores)
