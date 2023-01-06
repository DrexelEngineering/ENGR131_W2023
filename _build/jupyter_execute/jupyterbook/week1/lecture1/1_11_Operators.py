#!/usr/bin/env python
# coding: utf-8

# # Python Operators

# Operators are used to perform operations on variables and values.
# 

# For example we can use the `+` operator to add two number (or strings together)

# In[1]:


5 + 10


# In[2]:


'Drexel' + ' ' + 'Engineer'


# ## Arithmetic Operators
# 
# These are operators that perform basic mathematical functions

# ### Addition `+`

# In[3]:


x = 5
y = 3

print(x + y)


# ### Subtraction `-`

# In[4]:


x = 5
y = 3

print(x - y)


# ### Multiplication `*`

# In[5]:


x = 5
y = 3

print(x * y)


# ### Division `/`

# In[6]:


x = 5
y = 3

print(x / y)


# ### Modulus `%`
# 
# The remainder after dividing by a number

# In[7]:


x = 5
y = 3

print(x % y)


# ### Exponential `**`

# In[8]:


x = 5
y = 3

print(x ** y)


# ### Floor Division `//`
# 
# the floor division `//` rounds the result of division down to the nearest whole number

# In[9]:


x = 5
y = 3

print(x // y)


# ## Assignment Operators 
# 
# These are operators that allow you to assign a value to a variable.

# ### Equals `=`

# In[10]:


x = 5

print(x)


# ### Addition and Assignment `+=`

# In[11]:


x = 5
x += 3

print(x)


# ### Subtraction and Assignment `-=`

# In[12]:


x = 5
x -= 3

print(x)


# ### Multiplication and Assignment `*=`

# In[13]:


x = 5
x *= 3

print(x)


# ### Division and Assignment `/=`

# In[14]:


x = 5
x /= 3

print(x)


# ### Modulus and Assignment `%=`

# In[15]:


x = 5
x %= 3

print(x)


# ### Floor Division and Assignment `//=`

# In[16]:


x = 5
x //= 3

print(x)


# ### Exponential and Assignment `**=`

# In[17]:


x = 5
x **= 3

print(x)


# ## Comparison Operators
# 
# There are operators that allow you to compare two values or variables to see if they are the same or different. 

# ### Equal To `==`

# In[18]:


x = 3
y = 5

print(x == x)
print(x == y)


# ### Not Equal To `!=`

# In[19]:


x = 3
y = 5

print(x != x)
print(x != y)


# ### Greater Than `>`

# In[20]:


x = 3
y = 5

print(x > x)
print(x > y)


# ### Less Than `<`

# In[21]:


x = 3
y = 5

print(x < x)
print(x < y)


# ### Greater Than Equal To `>=`

# In[22]:


x = 3
y = 5

print(x >= x)
print(x >= y)


# ### Less Than Equal To `<=`

# In[23]:


x = 3
y = 5

print(x <= x)
print(x <= y)


# ## Logical Operators
# 
# Logical operators allow you to create logical statements between values or variables. 

# ### `and` Operator
# 
# Returns True if both statements are true

# In[24]:


x = 5

print(x > 3 and x < 10)
print(x > 3 and x > 10)
print(x < 3 and x > 10)


# ### `or` Operator
# 
# Returns True if one statements is true

# In[25]:


x = 5

print(x > 3 or x < 10)
print(x > 3 or x > 10)
print(x < 3 or x > 10)


# ### `not` Operator
# 
# Returns true is the result is false, returns false if the results is true

# In[26]:


print(not (True))


# In[27]:


print(not (False))


# In[28]:


x = 5

print(not (x > 3 or x < 10))
print(not (x > 3 or x > 10))
print(not (x < 3 or x > 10))


# ## Python Identity Operators
# 
# Identity operators allow you to determine if two variables are physically the same. This means both value and location in memory.

# ### `is` Operator
# 
# Returns true if an object is the same in memory

# In[29]:


x = 5
y = 5.

print(x is y)


# In[30]:


x = 5
y = x


print(x is y)


# ### `is not` Operator
# 
# Returns true if the object are different in memory

# In[31]:


x = 5
y = 5.

print(x is not y)


# In[32]:


x = 5
y = x


print(x is not y)

