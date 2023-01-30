#!/usr/bin/env python
# coding: utf-8

# # 📝Week 1 - Lab Intro
# 
# In this lab introduction we will briefly revisit some of the key topics from lecture 1, focusing on those relevant to lab 1.  

# ## Python's Built-in Functions

# ### Print Function

# In[1]:


print("Drexel Engineering")


# You can find more [built-in functions](https://docs.python.org/3/library/functions.html)

# ## Importing Built-in Modules

# The base package of python contains built-in modules. These have to be imported before they can be used. 

# You import modules using 
# ```python
# import <Module Name>
# ```

# ### Random
# 
# We can use random to sample a random integer. This would make a 6-sided die. 

# In[2]:


import random


# In[3]:


dice = random.randint(1,6)
print(dice)


# You can view everything included in the [standard library here](https://docs.python.org/3/library/)

# ## Importing External Packages

# **Syntax**
# 
# Reminder: there are many ways to import packages
# 
# ```python
# from {package name} import {module}
# 
# from {package name} import {module} as {name}</code></pre>
# ```

# ### Importing Numpy

# A common package for scientific computing is Numpy, it is most commonly imported and given the shortened name ```np```.

# In[4]:


import numpy as np


# Use numpy to find the mean of a list of numbers

# In[5]:


print(np.mean([1,2,3,4]))


# ## Variables

# Variables are containers for storing data values.
# 

# In[6]:


x = 5


# In[7]:


y = "Drexel"


# In[8]:


print(x)


# In[9]:


print(y)


# ## Python Operators

# Operators are used to perform operations on variables and values.
# 

# For example we can use the `+` operator to add two number (or strings together)

# In[10]:


5 + 10


# In[11]:


'Drexel' + ' ' + 'Engineer'


# ## Reminder: a few useful operators 
# 
# Here's a reminder about a few of the operators that may be new to you

# ### Modulus `%`
# 
# The remainder after dividing by a number

# In[12]:


x = 5
y = 3

print(x % y)


# ### Floor Division `//`
# 
# The floor division `//` rounds the result of division down to the nearest whole number

# In[13]:


x = 5
y = 3

print(x // y)


# ### Addition and Assignment `+=`
# 
# Add to a variable and reassign the value

# In[14]:


x = 5
x += 3

print(x)


# ### Equal To `==`
# 
# Check to see if two variables are equal

# In[15]:


x = 3
y = 5

print(x == x)
print(x == y)

