#!/usr/bin/env python
# coding: utf-8

# # Variables and Objects

# Variables are containers for storing data values.
# 

# Python does note require that you declare variables, they are created once assigned with the `=` operator

# In[1]:


x = 5


# In[2]:


y = "Drexel"


# In[3]:


print(x)


# In[4]:


print(y)


# You do not need to declare the DataType of a variable it is inferred

# In[5]:


x = 5
print(type(x))


# In[6]:


x = 5.0
print(type(x))


# In[7]:


x = 'Drexel'
print(type(x))


# ## Assigning Strings
# 
# Strings can be assigned with " or ' quotes

# In[8]:


x = "Drexel"


# In[9]:


y = 'Drexel'


# You can check if two variable have the same value using the `==` operator

# In[10]:


x == y


# ## Case Sensitive
# 
# Variables are case sensitive

# In[11]:


a = "Drexel"
A = 5
print(a)
print(A)


# ## Variable Names

# * A variable name must start with a letter or the underscore character
# * A variable name cannot start with a number
# * A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# * Variable names are case-sensitive (age, Age and AGE are three different variables)

# In[12]:


myvar = "Drexel"
my_var = "Drexel"
_my_var = "Drexel"
myVar = "Drexel"
MYVAR = "Drexel"
myvar2 = "Drexel"


# ## Assigning Multiple Variables
# 
# Python allows you to assign values to multiple variables in one line:
# 

# In[13]:


x, y, z = "Drexel", "University", "Engineering"
print(x)
print(y)
print(z)


# ## Objects
# 
# All Python variables are objects who have behaviors based on their datatype. 
# 
# An object could be a:
# * Integer
# * String
# * Floating point number
# * Method
# 
# Or any other data type

# ### String Objects
# 
# When you define a string there are built-in method that can be applied. 

# In[14]:


DU = "Drexel University Engineering"

# splits based on a character
print(DU.rsplit(" "))


# In[15]:


print(DU.upper())


# ### Float Objects

# In[16]:


num = 500.


# In[17]:


num.is_integer()


# In[18]:


print(type(num))

