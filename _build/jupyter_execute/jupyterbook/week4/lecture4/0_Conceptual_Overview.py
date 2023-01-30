#!/usr/bin/env python
# coding: utf-8

# # 📝 Conceptual Overview
# 

# 
# We have covered a lot of topics so far. It is important to consolidate this information.

# ## Variables
# 
# Variables provide a simple human-readable reference to a python object. 
# 

# 
# Anything can be stored as a variable using an assignment `=` operator
# 

# 
# Variables are important because they allow you to reuse and transport python objects in useful ways

# ### Defining an integer variable

# In[1]:


number = 1


# ### Defining a string variable

# In[2]:


string = "string"


# ## DataTypes

# We have used DataTypes and there are many different DataTypes. The most common are:
# 1. Strings - a series of characters interpreted literally

# 2. Integers - A whole number that is not a fraction

# 3. Float - A number that has a decimal point

# 
# Unlike humans that know that 1 can be represented as a number or a string computers do not.
# 

# 
# When a computer tries to perform an operation (e.g. add) a string it is completely different than the same operation on an integer. 
# 

# 
# A good analogy is that the method you would take to get to Drexel via public transportation or driving is different. If you have a car and are provided with a bus pass you will not get to class. Similarly, if you are presented with a bus and a car key you will also not get to class. 
# 

# ### Operations on DataTypes
# 
# For operations to work the DataType and the method must match.
# 

# In[3]:


"2" + "2"


# In[4]:


2 + 2


# In[3]:


"2" + 2


# ## Mutability
# 
# Object in computers are stored in binary 1s and 0s. There are many structures that can be used to store objects and they effect the behavior. 
# 

# 
# As a very simple example assume a simple coding: 
# 

# 
# Binary	Symbol
# 
# 
# | Binary | Symbol |
# |---|---|
# | 0101 | ☮️ |
# | 1010 | ❤️ |
# | 1111 | 😀 |
# 

# 
# If you had a string made up of 3 emojis ☮️❤️😀 010110101111 and you wanted to add a fourth, you may, or may not be able to do that depending on how your memory is allocated. This is why string are immutable. 
# 

# **Aside:** There is an additional layer between the ID and the physical location in memory which can be changed. Thus there can be changes in memory allocation without changing the object ID.  
# 

# ### Immutable
# 
# Immutable - unable to be changed
# 

# 
# In practice, some objects types are made immutable to ensure object permanence and minimize the chance for bugs
# 

# 
# **Immutable DataTypes:** integer, string, float, tuple

# In[5]:


string = "100"
print(id(string))
print(type(string))


# In[6]:


string += "1"
print(id(string))
print(type(string))


# In[7]:


integer = 100
print(id(integer))
print(type(integer))


# In[8]:


integer += 101
print(id(integer))
print(type(integer))


# The ID is different, a new object was created. 

# ### Mutable
# 
# List, Dictionaries, Functions are mutable - This means they can be directly changed.
# 

# In[9]:


string = ["100"]
print(id(string))
print(type(string))


# In[10]:


string[0] = ["101"]
print(id(string))
print(type(string))


# In[11]:


integer = [100]
print(id(integer))
print(type(integer))


# In[12]:


integer[0] = [101]
print(id(integer))
print(type(integer))


# ## Objects in Python
# 
# Everything in memory in Python is an object. 
# 

# 
# **Why are objects important?**
# 
# 

# ```{toggle}
# When you have an object you can assign multiple variables to that object
# ```

# In[13]:


a = "string object"
b = a


# In[14]:


a is b


# This means the object is the same and has a physical location in memory

# In[15]:


print(f"The id of a is {id(a)}")
print(f"The id of b is {id(b)}")


# ### Copying Objects

# You can make copies of an object (if they are mutable)

# In[43]:


a = "string object"
a.copy()


# In[16]:


a = ["string object"]
b = a.copy()


# In[17]:


print(a is b)
print(a == b)


# `a` and `b` have the same values but they are not the same objects

# ### Attributes of Objects
# 
# Objects have can have attributes beyond just their values

# For example, consider your car. Besides having a unique identifier to your car you might also want to know the year, make, and model, an object allows you to bundle that information into the same variable. 

# Objects of a common type can also have methods. Continuing the analogy, a car has a method to drive in forward or reverse. 

# A list has a method to show the sort, and length. In the future you will learn how to make custom methods. 

# In[18]:


simple_list = [2, 1, 3]
simple_list.__len__()


# In[19]:


simple_list.sort()
print(simple_list)

