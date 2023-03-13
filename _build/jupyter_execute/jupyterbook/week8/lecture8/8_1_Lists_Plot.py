#!/usr/bin/env python
# coding: utf-8

# # Lists
# 

# ## Constructing a list
# 
# Let's use an example from the lab you did in ENGR 111 to build a car with a mousetrap. 
# 
# Consider collecting the data from different lengths of fishing wire to find the greatest distance you could get the car to travel.

# In[1]:


# length of fishing wire in inches
fishingWireLength = [0.5, 2.5, 1.0, 2.2, 1.7, 1.4]

# distance traveled in feet
distanceTraveled = [0.3, 1.1, 0.8, 1.2, 1.3, 1.5]


# Now, you have two lists. We'll look at how you can use python to plot the data you collected in an activity. 
# 

# We can use operations on lists and list methods to find the maximum distance traveled and the corresponding fishing wire length.

# In[2]:


# find shortest distance traveled
shortestDistance = max(distanceTraveled)

# find the location in the list
indexShortestDistance = distanceTraveled.index(shortestDistance)

# determine the corresponding fishing wire length
worstFishingWireLength = fishingWireLength[indexShortestDistance]


# ## List comprehensions
# 
# Perhaps you got access to a new set of fishing wires that are 3 inches longer. 
# 
# You want to design a similar experiment to find the distances the car would travel using these fishing wire instead of the shorter ones.
# 
# Constructing a list using list comprehension could help design lengths to try.

# In[3]:


# make a new list with every element of the fishing wire length list increased by three inches
longerFishingWireLength = [(i + 3) for i in fishingWireLength]


# ## Basic plotting
# 
# Lists make it very easy to plot one variable against another.
# 
# Make sure you have imported the `matplotlib` package then apply the [`plot` method](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot).

# In[4]:


import matplotlib.pyplot as plt

# make lists
a = [4, 3, 2, 1]
b = [1, 4, 2, 3]

# make a scatter plot of b against a with circle markers
plt.plot(a, b, "o")

# label x- and y-axes
plt.xlabel("a")
plt.ylabel("b")


# In[ ]:




