#!/usr/bin/env python
# coding: utf-8

# # 📝Functions as Objects

# Let's build a function to draw a drexel dragon.

# In[1]:


def drexel_dragons():
    print(
        """         

           /\_/\   _   ()_()  wWw  wW    Ww wWw  W  W        _   ()_()            \/       .-.   \\\  ///  oo_    
          / o o \   /||_ (O o)  (O)_(O)\  /(O)(O)_(O)(O)      /||_ (O o)    /)     (OO)    c(O_O)c ((O)(O)) /  _)-< 
     /\   \~(*)~/     /o_) |^_\  / __)`. \/ .' / __) ||         /o_) |^_\  (o)(O) ,'.--.)  ,'.---.`, | \ ||  \__ `.  
     //\\  /     \   / |(\ |(_))/ (     \  /  / (    | \       / |(\ |(_))  //\\ / /|_|_\ / /|_|_|\ \||\\||     `. | 
     //  \\(       )  | | ))|  /(  _)    /  \ (  _)   |  `.     | | ))|  /  |(__)|| \_.--. | \_____/ ||| \ |     _| | 
     //    \/\~*.*~/   | |// )|\\ \ \_  .' /\ `.\ \_  (.-.__)    | |// )|\\  /,-. |'.   \) \'. `---' .`||  ||  ,-'   | 
     //__/\_/   \      \__/ (/  \) \__)(_.'  `._)\__)  `-'       \__/ (/  \)-'   ''  `-.(_.'  `-...-' (_/  \_)(_..--'  """
    )


# Let's assign `drexel_dragons` to a variable `Penn`

# In[2]:


Penn = drexel_dragons


# **Why did this not run?**

# ```{toggle}
# We just assigned this to a variable that is an object of the function `drexel_dragons`
# ```

# We can discover what the object is by printing the type

# In[3]:


print(type(Penn))


# Or running it by calling the function

# In[4]:


Penn()


# ## Reassigning Functions
# 
# We can assign functions to a different variable

# In[5]:


drexel = drexel_dragons


# In[6]:


drexel is Penn


# In[7]:


drexel == Penn


# ## Functions in Data Structures
# 
# Data Structures are objects that store other objects: List, Tuples, Dictionaries, Sets

# Since functions are objects they can be stored in data structures

# In[8]:


[Penn, drexel]


# ## Functions calling Functions
# 
# Functions can be called by other functions. A good example of this is the function `map`

# `map()` function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# In[9]:


import numpy as np
import matplotlib.pyplot as plt


def sig(x):
    return 1 / (1 + np.exp(-x))


# In[10]:


x = np.random.uniform(-5, 5, 100)
plt.plot(x, np.array(list(map(sig, x))), "s")


# ## Function Scope
# 
# A variable is only available from inside the region which is was created

# ### Local Scope
# 
# A variable created inside a function belongs to the *local scope* of that function, and can only be used inside that function

# A variable created inside a function is available inside that function:
# 
# 

# In[11]:


def myfunc():
    x = 300
    print(x)


myfunc()


# ### Global Scope
# 
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# 

# 
# Global variables are available from within any scope, global and local.

# A variable created outside of a function is global and can be used by anyone:
# 

# In[12]:


x = 300


def myfunc():
    print(x)


myfunc()

print(x)


# ### Common Mistakes
# 
# You cannot access a locally defined variable outside a function, as it does not exist

# In[ ]:


x = 300


def my_function():
    print(x)
    y = 200
    print(y)


y

