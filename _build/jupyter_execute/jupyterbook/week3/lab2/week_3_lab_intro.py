#!/usr/bin/env python
# coding: utf-8

# # 📝Week 3 - Lab Intro
# 
# In this lab introduction we will briefly revisit some of the key topics from lecture and discuss the map function, which is used in the lab assignment.

# ## Strings

# The string data type stores a string of characters. Create a string by enclosing text in single or double quotes. 

# In[1]:


s1 = "This is an example string"
s2 = 'So is this'


# Find the string length with ```len()```.

# In[2]:


alphabet = "abcdefghijklmnopqrstuvwxyz"
print(len(alphabet))


# You can slice strings by supplying indices in square brackets. 
# 
# To slice a list ```L``` from a start index ```start``` up to (but not including) index ```stop``` with a step size of ```step```, do the following:
# 
# ```L[start:stop:step]```

# In[3]:


# slice from index 0 up to (not including 5)
print(alphabet[:5]) 

# slice from index -3 to the end
print(alphabet[-3:]) 

# slice from index 0 to the end, stepping by 2
print(alphabet[::-1])


# You can use f-string formatting to easily include variable values in a string

# In[4]:


year = 2023
year_message = f"The current year is {year}."

print(year_message)


# ## Lists and dictionaries

# Lists are ordered collections of data. Dictionaries are a data structure that have (key, value) pairs.

# In[5]:


# this is a list
L = ["abc", 42, True] 

# this is a dictionary
D = {
    "color": "green",
    "number": 12,
    "result": True
}


# Square brackets are used to access values in a list or dictionary.

# In[6]:


# get the list item at index 1
print(L[1])

# get the dictionary item at key "color"
print(D["color"])


# ## Map function

# We can use the map function to apply the same function to all elements of a list.

# ### Example: squaring a list of numbers

# In[7]:


# a simple fucntion that squares a number
def square(x):
    return x*x 


# In[8]:


L = [0,1,2,3,4,5,6,7,8,9,10]

print(map(square, L))


# The map function returns a map object that can be converted to a list as follows:

# In[9]:


squared_L = list(map(square, L))
print(squared_L)

