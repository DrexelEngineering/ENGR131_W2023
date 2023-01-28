#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Initialize Otter
import otter
grader = otter.Notebook("hw4-functions.ipynb")


# # 🏡📝 Homework 4 - Applying Functions with Engineering Applications
# 
# This assignment includes three problems on the topic of functions.
# 
# 

# **Question 1: Volume of a Sphere** 
# 
# The volume of a sphere with radius $r$ is calculated using the equation:
# 
# $$ V = \frac{4}{3} \pi r^{3}$$
# 
# Write python code to do the following:
# 
# * Define a function called `sphere_volume` which accepts one input argument `r`
# * Implement your function so that it returns the volume of a sphere with radius $r$
# 
# 
# Your code replaces the prompt:  `...`

# In[ ]:


...


# In[ ]:


grader.check("q1-sphere")


# **Question 2: Simple Statistics** 
# 
# If you have a list which contains $N$ values, $x_1$ through $x_N$, the mean $\mu$ is calculated as follows:
# 
# $$ \mu = \sum_{i=1}^{N} \frac{x_{i}}{N}  $$ 
# 
# To calculate the standard deviation of the data, you use the formula:
# 
# $$ \sigma = \sqrt{ \sum_{i=1}^{N} \frac{\left(x_{i} - \mu \right) ^ 2}{N - 1} } $$
# 
# Note: Python actually has a built-in `statistics` library that can be used to compute the mean $\mu$ and standard deviation $\sigma$. The code below uses the library to compute these statsics from a list of numbers `L`:
# 
# 

# In[ ]:


import statistics

L = [1,2,3,4,5]

print(statistics.mean(L))
print(statistics.stdev(L))


# For this problem, the goal is to implement your own function which computes these statistics. You may not use the `statistics` library in your code (or any other library that can compute these statistics automatically), but may find it useful for checking your answer. A partial function is provided below and you are asked to complete it.
# 
# Your task is to do the following:
# 
# * Read the provided code and the comments
# * Add a single line of code, indented under the first for loop, which adds to the `mean` variable the value: $\frac{x_i}{N}$  
# * Add a single line of code, indented under the first for loop, which adds to the `std` variable the value: $\frac{\left(x_{i} - \mu \right) ^ 2}{N - 1}$ 
# * Return from the function a tuple containing ($\mu$, $\sigma$)
# 
# Your code replaces the prompt:  `...`

# In[ ]:


def stats(L):
    """This function takes in a list L and returns a tuple containing its (mean, standard deviation)"""

    N = len(L) # Compute the length of list L using the len() function, and store it in N.
    mean = 0  # Set a variable called mean to zero. We will add to this variable until it accumulates its proper value.
    std = 0   # Set a variable called std to zero. We will add to this variable until it accumulates its proper value.

    
    # The following for loop iterates over every value of x_i
    for x_i in L:
        # Your code below will add the appropriate value to mean and store the result back in mean  
        ...

    # The following for loop iterates over every value of x_i
    for x_i in L:
        # Your code below will add the appropriate value to std and store the result back in std 
        ...
        
    std = std ** (1/2) # To arrive at the standard deviation, we must take the square root of the accumulated value.

    # Your code below should return a tuple containing the mean and standard deviation.
    ...


# In[ ]:


grader.check("q2-stats")


# **Question 3: Kinetic Energy** 
# 
# The kinetic energy of an object $E_k$ of an object is computed using its mass $m$ and velocity $v$ using the following equation: 
# 
# $$ E_k = \frac{1}{2} m v^2  $$ 
# 
# 
# Write python code to do the following:
# 
# * Define a function called `kinetic_energy` that takes input arguments `m` and `v`
# * The function should return the kinetic energy
# 
# Your code replaces the prompt:  `...`

# In[ ]:


...


# In[ ]:


grader.check("q3-kinetic")


# 
