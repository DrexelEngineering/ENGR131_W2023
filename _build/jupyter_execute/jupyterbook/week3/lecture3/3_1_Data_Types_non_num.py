#!/usr/bin/env python
# coding: utf-8

# # 📝Data Types

# * Every object that you store in python has a data type that describes how it is interpreted and behaves.

# ## Boolean

# The most simple data type is a Boolean which has one of two possible values:
# 1. True
# 2. False

# ### Boolean Type
# 
# Booleans are described in python by the words: `True` or `False`

# In[1]:


True


# <div class="admonition note alert alert-info">
# <p class="first admonition-title" style="font-weight: bold;">Note</p>
# Computers work with binary logic, which means that everything is defined by a series of 1's or 0's. The data type determines how the bits are interpreted.
# </div>

# <div class="admonition note alert alert-secondary">
# <p class="first admonition-title" style="font-weight: bold;">Definition</p>
# Bit - the most basic unit of computing representing a logical state of a `1` or `0`<br>
# Byte - 8 bits grouped together
# </div>

# **Question:** How many bits are required to store a boolean value? 

# ```{toggle}
# Technically, a boolean value could be stored in a single bit; however, boolean values are commonly stored as 4 bits because of hardware architectures. 
# ```

# <div class="admonition note alert alert-secondary">
# <p class="first admonition-title" style="font-weight: bold;">Syntax</p>
# <tt class="docutils literal">type(obj)</tt> - returns the data type of an object
# </div>

# In[2]:


type(True)


# In[3]:


type(False)


# In[4]:


type(true)


# **Question:** Why did this not work?  

# ```{toggle}
# The value `true` is not actually defined. Python is case sensitive. 
# ```

# ### Booleans as Numbers
# 
# Python can consider booleans as numbers.

# <div class="admonition tip alert alert-success">
# <p class="first admonition-title" style="font-weight: bold;">Syntax</p>
# <tt class="docutils literal"> == - is an operator for is equal to 
# </div>

# In[5]:


True == 1


# In[6]:


True == 0


# In[8]:


False == 0


# Since Booleans can be interpreted as numbers, it is possible to use operators arithmetically.

# <div class="admonition tip alert alert-success">
# <p class="first admonition-title" style="font-weight: bold;">Syntax</p>
# <tt class="docutils literal"> + <tt> - Addition operator<br> 
# <tt class="docutils literal"> - <tt> - Subtraction operator<br>
# <tt class="docutils literal"> * <tt> - Multiplication operator<br>
# <tt class="docutils literal"> / <tt> - Division operator<br> 
# </div>

# In[9]:


True + (False / True)


# ## Strings
# 
# Strings are arrays of bytes representing Unicode characters.
# 
# * each character is 2 bytes or 16 bits wide

# <div class="admonition tip alert alert-success">
# <p class="first admonition-title" style="font-weight: bold;">Syntax</p>
# Strings are defined by surrounding characters with <tt class="docutils literal"> "<tt> or <tt class="docutils literal">'<tt> marks
# </div>

# String with "

# In[10]:


"Drexel Engineering"


# String with '

# In[11]:


"Drexel Engineering"


# Are these the same?

# In[12]:


"Drexel Engineering" == "Drexel Engineering"


# Use the `type` function to confirm the datatype of an object or variable.

# In[13]:


type("Drexel Engineering")


# Strings can be numbers.

# In[14]:


type("123")


# Strings can be combinations of characters, numbers, and even emojis.

# In[15]:


type("Drexel 🐉 112")

