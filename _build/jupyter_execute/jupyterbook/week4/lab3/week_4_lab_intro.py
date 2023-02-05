#!/usr/bin/env python
# coding: utf-8

# # 📝Week 4 - Lab Intro
# 
# In this lab introduction we will briefly revisit the topic of functions from lecture, and then go over an introduction to image processing using Numpy, the topic of today's lab.

# ## Functions

# ### Defining a function
# A function is defined using the `def` keyword. All code within the function must be indented.

# In[1]:


def myfunc():
    x = 300
    print(x)


# ### Calling a function
# To run the code within a function, we can write the name of a function followed by parentheses. This is called "calling the function." The code below can be used to call the myfunc function.

# In[2]:


myfunc()


# ### Function inputs
# A function can be given input arguments which are included within the parentheses of the function definition.

# In[3]:


def dbl(x):
    print(2 * x)


# When you call a function that requires arguments, the input is included in the parantheses of the function call.

# In[4]:


dbl(6)


# ### Function outputs
# A function can output data by using the `return` keyword. After the return statement, the function is exited immediately, so no indented code below the return statement gets run.

# In[5]:


def square(x):
    return x**2


# Notice that the square function doesn't print, it returns an output value which can then be stored in a variable.

# In[6]:


y = square(3)
print(y)


# ### Multiple inputs and outputs
# Functions can have multiple inputs and outputs, separated by commas. The example function below takes in two inputs, a rectangle's length and width, and it returns the rectangle's area and perimeter.

# In[7]:


def area_and_perim(length, width):
    area = length * width
    perim = (length + width) * 2
    return area, perim


# In[8]:


print(area_and_perim(3,4))


# ## Image Processing in Python

# We will now go over a brief introduction to image processing in Python, which can be found at the top of today's lab assignment.
