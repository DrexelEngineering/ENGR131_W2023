#!/usr/bin/env python
# coding: utf-8

# # Using Dictionaries for Physics
# 

# ## Arrange information
# 
# To compare different scenarios, one can arrange essential information in a dictionary where it is easily accessible for calculations.
# 
# Let's consider an example from a construction site where four different objects need to be lifted to the appropriate floor.
# 

# In[1]:


# create dictionary for scenarios in which work is completed

beam1 = {"floor": 18, "weight": 5000}
beam2 = {"floor": 20, "weight": 4000}
window1 = {"floor": 10, "weight": 200}
window2 = {"floor": 7, "weight": 200}

construction = [beam1, beam2, window1, window2]


# ## Calculate work
# 
# We know that the work required to lift an object is given by 
# 
# $W = Fd = mgd$
# 
# where $W$ is work, $m$ is mass, $g$ is gravity, and $d$ is distance from the ground.
# 
# Each floor of a building is approximately 10 feet high.

# In[2]:


# iterate through the list to add the work required for each
for i in range(len(construction)):
    work = construction[i]["weight"] * construction[i]["floor"] * 10
    construction[i].update({"work": work})

print(construction)


# Determine the most and least work-intensive objects to lift.

# In[3]:


# iterate over list of items to form list of work
workRequired = []
for items in construction:
    workRequired.append(items.get("work"))

mostWork = max(workRequired)
leastWork = min(workRequired)


# In[ ]:




