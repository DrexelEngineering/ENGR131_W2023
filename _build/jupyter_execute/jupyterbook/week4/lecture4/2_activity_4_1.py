#!/usr/bin/env python
# coding: utf-8

# # 💻 Activity 4.1: Build a function to convert inches to feet
# 
# It is common to use a function to conduct a useful conversion in a program. Try to make a function that converts inches to feet. Your function should print `x inches is equal to y feet and z inches`. Make your function called inches_to_feet.

# Your function

# In[ ]:


...


# In[1]:


def inches_to_feet(inches):
    feet = inches // 12
    inches_ = inches % 12
    print(f"{inches} is equal to {feet} feet and {inches_} inches")


# Tests

# In[ ]:


...


# In[2]:


inches_to_feet(37)


# Now build a function feet_to_inches that converts feet to inches. You function should print `x feet and y inches is equal to y inches`

# Your function

# In[ ]:


...


# In[3]:


def feet_to_inches(feet, inches):
    inches_ = feet * 12 + inches
    print(f"{feet} feet and {inches} inches is equal to {inches_} inches")


# Tests

# In[ ]:


...


# In[4]:


feet_to_inches(3, 1)

