#!/usr/bin/env python
# coding: utf-8

# # 📝 Dynamic Behavior in Python
# 
# Python includes a lot of flexibility and can adjust DataTypes and behaviors based on valid operations on inputs provided. 

# ## *args
# 
# Sometimes when you build functions you do not know how many inputs you will have. This can be handled usings *args.

# <div class="admonition note alert alert-info">
# <p class="first admonition-title" style="font-weight: bold;">Note</p> Any *variable can be used for *args, it is convention and good practice to use *args
#  </a>
# </div>

# In[1]:


def add(*args):
    print(sum(args), type(args))


add(2, 3)


# ## **kwargs
# 
# Sometimes you want to input an arbitrary number of key-value pairs. This can be done with the **kwargs input.

# <div class="admonition note alert alert-info">
# <p class="first admonition-title" style="font-weight: bold;">Note</p> Any **variable can be used for **kwargs, it is convention and good practice to use *kwargs
#  </a>
# </div>

# In[2]:


def add(**kwargs):
    print(kwargs)  # this is a dictionary
    print(sum(kwargs.values()))


add(two=2, three=3)


# ## *args and **kwargs
# 
# You can use predefined inputs, *args, and **kwargs together. Python will choose the right input. 

# In[3]:


def add(text, *args, **kwargs):
    print(text + f"kwargs is: {sum(kwargs.values())}")
    print(text + f"args is: {sum(args)}")


add("the sum is:", two=2, three=3)


# In[4]:


add("the sum is:", 2, 3)


# In[5]:


add("the sum is:", 2, 100, three=3, _1k=1000)


# <div class="admonition note alert alert-info">
# <p class="first admonition-title" style="font-weight: bold;">Note</p> *args and **kwargs are much more useful with iterators which you will learn about soon.
#  </a>
# </div>

# # Dynamic Typing
# 
# Within functions it is possible to input different DataTypes as inputs and as long a python can infer a valid operation and DataType it will automatically adjust

# In[6]:


def multiplier(x, y):
    print(f"multiplier ({x}, {y}) is {x * y}")
    print(type(x * y))


# In[7]:


multiplier(3, 2)


# In[8]:


multiplier(3.14, 2)


# In[9]:


multiplier("Drexel Dragons ", 3)

