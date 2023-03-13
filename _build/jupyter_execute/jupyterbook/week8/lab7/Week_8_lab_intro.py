#!/usr/bin/env python
# coding: utf-8

# # 📝 Week 8 - Lab Intro
# 
# In this lab introduction we will briefly review how Arrays and broadcasting for this lab

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# ## Creating Arrays

# ### Creating an array of zeros,
# We often want an empty array to begin iterative calculations. We can use `np.zeros()` to create an array of zeros. If you forget what the inputs are, hover over the function, and press `shift + tab` to view the docstring.

# In[ ]:


print(np.zeros(10))


# In[ ]:


print(np.zeros((2,3)))


# ### Creating an array with equal spacing
# To make an array with equal spacing, use `np.linspace()`. This method can only create 1D arrays.

# In[ ]:


print(np.linspace(0,1))


# The default number of points is 50. If we want to change the number of points, we can use input `num=...`

# In[ ]:


print(np.linspace(0,1,num=10))


# If we want to exclude the endpoint, we can use input `endpoint=False`.

# In[ ]:


print(np.linspace(0,1,num=10,endpoint=False))


# ## Create array from list

# In[ ]:


num_list = [0,3,4,5,7]
arr = np.array(num_list)

print(arr, type(num_list), type(arr))


# ## Broadcasting
# Numpy arrays can infer how to distribute a calculation across axes. This is called *broadcasting*. For example, let's try some basic operations

# In[ ]:


test_array = np.zeros(5)
print(test_array)


# In[ ]:


test_array = test_array+1
print(test_array)


# In[ ]:


test_array = test_array * 6
print(test_array)


# ### What happens when we perform operations on arrays of different shapes?

# In[ ]:


test_array = np.ones(5)
print(test_array)


# In[ ]:


test_linspace_array = np.linspace(0,1,num=10,endpoint=False)
print(test_linspace_array)


# In[ ]:


test_array + test_linspace_array


# We see that need to perform operations on arrays with similiar shapes

# ### np functions and broadcasting
# 
# Many numpy function will automatically broadcast depending on the shape of your input

# In[ ]:


np.sin(np.pi/2)


# In[ ]:


test_linspace_array = np.linspace(0,1,num=10,endpoint=False)
print(test_linspace_array.shape)

print(np.sin(np.pi * test_linspace_array))


# ## Plotting arrays
# 
# To plot, we can use the `plt.plot(x_array,y_array)`
# 
# We can also add a title and axis labels using `plt.title()`, `plt.xlabel()` and `plt.ylable()`

# In[ ]:


t = np.linspace(0,2*np.pi,num=20,endpoint=False)
y = np.sin(t)

plt.plot(t,y)
plt.title('Example Sine curve')
plt.xlabel('time (s)')
plt.ylabel('amplitude (a.u.)')


# In[ ]:




