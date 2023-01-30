#!/usr/bin/env python
# coding: utf-8

# # 📝 Return Output using Functions
# 
# The value in functions come from their ability to perform operations on an input and return a new output. 

# ## Explicit Return statement
# 
# Aside: Why the number 42? 
# 

# 
# The number 42 is especially significant to fans of science fiction novelist Douglas Adams’ “The Hitchhiker’s Guide to the Galaxy,” because that number is the answer given by a supercomputer to “the Ultimate Question of Life, the Universe, and Everything.”   

# In[1]:


def return_42():
    return 42  # An explicit return statement


# In[2]:


return_42()


# **You can modify an explicit return statement**

# In[3]:


return_42() * 2


# In[4]:


return_42() - 2


# ## Functions with Inputs and returns

# In[5]:


def mean(sample):
    return sum(sample) / len(sample)


# In[6]:


mean([1, 2, 3, 4])


# ## Implicit Return Statements

# In[7]:


def add_one(x):
    results = x + 1


# In[8]:


value = add_one(5)


# In[9]:


value


# In[10]:


print(value)


# **Why did this return None?**

# ```{toggle}
# No return statement was provided thus an implicit return of `None` was inferred.
# ```

# ## Returning multiple values
# 
# You can have a Python function return multiple values

# In[11]:


import numpy as np


def statistics(sample):
    
    mean = np.mean(sample)
    median = np.median(sample)
    
    # find unique values in array along with their counts
    vals, counts = np.unique(sample, return_counts=True)

    # find mode
    mode = np.argwhere(counts == np.max(counts))
    return mean, median, mode


# In[12]:


mean, median, mode = statistics([0, 1, 2, 3, 3, 4, 5])


# In[13]:


print(mean)
print(median)
print(mode)


# ## Functions calling Functions

# In[14]:


def adder(number, value):
    return number + value


def multiplier(number, factor):
    return number * factor


# In[15]:


multiplier(adder(10, 1), 10)


# ## Functions by Closure
# 
# Because functions are object you can return a function that is modified by some input

# In[16]:


def by_factor(factor):
    def multiply(number):
        return factor * number

    return multiply


# Let's break this down:
# 1. You start by calling by_factor with an input of factor.

# 2. factor is locally defined so when you run multiply it uses the value for factor

# 3. return multiply returns the function with the factor implemented

# 4. This function can be used by inputting a number

# In[17]:


double = by_factor(2)


# In[18]:


double(3)


# In[19]:


double(12)


# In[20]:


triple = by_factor(3)


# In[21]:


triple(3)


# In[22]:


triple(12)


# ## Advanced Topic (not on exam - maybe bonus): Decorators 

# Decorators are tools that take one function as an input and extend its capabilities. 

# In[23]:


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)


# In[24]:


say_whee()


# ### Beautiful Python
# 
# Python has a lot of ways to simplify syntax. This might be confusing at first but makes for really nice and simple code

# In[25]:


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


# In[26]:


say_whee()


# ## Creating decorator files
# 
# You can create Python files, import them, and use them as decorators

# In[27]:


get_ipython().run_cell_magic('writefile', 'decorators.py', '\ndef do_twice(func):\n    def wrapper_do_twice():\n        func()\n        func()\n    return wrapper_do_twice\n')


# In[28]:


from decorators import do_twice


@do_twice
def say_whee():
    print("Whee!")


# In[29]:


say_whee()


# ## Decorators with Arguments
# 

# In[30]:


from decorators import do_twice


@do_twice
def greet(name):
    print(f"Hello {name}, I am a Drexel Dragon")


# In[13]:


greet("Jay")


# The problem is that the inner function wrapper_do_twice() does not take any arguments, but name="World" was passed to it.

# The solution is to use *args and **kwargs in the inner wrapper function. Then it will accept an arbitrary number of positional and keyword arguments.

# In[31]:


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


# In[32]:


@do_twice
def greet(name):
    print(f"Hello {name}, I am a Drexel Dragon")


# In[33]:


greet("Jay")

