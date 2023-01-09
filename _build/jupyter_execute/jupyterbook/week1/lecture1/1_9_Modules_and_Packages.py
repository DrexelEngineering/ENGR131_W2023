#!/usr/bin/env python
# coding: utf-8

# # 📝Modules and Packages

# In Python tools are built around modules that perform operations

# Modularity allows the isolation of code to simplify programming

# ## Built-in Functions

# Python contains many built in functions

# ### Print Function

# In[1]:


print("Drexel Engineering")


# ### Finding a DataType

# In[2]:


type("Drexel Engineering")


# You can find more [built-in functions](https://docs.python.org/3/library/functions.html)

# ## Built-in Modules

# The base package of python contains built-in modules. These have to be imported before they can be used. 

# You import modules using 
# ```python
# import <Module Name>
# ```

# ### Random
# 
# We can use random to sample a random integer. This would make a 6-sided die. 

# In[3]:


import random


# In[4]:


dice = random.randint(1,6)
print(dice)


# You can view everything included in the [standard library here](https://docs.python.org/3/library/)

# ## External Packages

# There are many additional packages. Anyone in the world can make a package. Most packages are distributed using the [Python Package Index (PyPI)](https://pypi.org/).

# You can install packages using package managers:
# 
# `pip install <package name>`
# 
# or 
# 
# `conda install <package name>`

# ### Importing Matplotlib

# A common plotting package in Python is matplotlib, we can import and use matplotlib.

# <div class="admonition note alert alert-info">
# <p class="first admonition-title" style="font-weight: bold;">Note</p>
# Usually when you download python distributions they will contain many of the common packages. We have installed all the packages you need for the course on the JupyterHub.
# </div>

# <div class="admonition tip alert alert-success">
# <p class="first admonition-title" style="font-weight: bold;">Syntax</p>
# There are many ways to import packages
# 
# <body>
#     <pre><code id="python_code">import {package name}
# 
# from {package name} import {module}
# 
# from {package name} import {module} as {name}</code></pre>
#     <script type="text/javascript">
#         window.onload = function(){
#             var codeElement = document.getElementById('python_code');
#             // Add code mirror class for coloring (default is the theme)
#             codeElement.classList.add( 'cm-s-default' );
#             var code = codeElement.innerText;
# 
#             codeElement.innerHTML = "";
# 
#             CodeMirror.runMode(
#               code,
#               'python',
#               codeElement
#             );
#         };
#     </script>
# </body>    
#     
# </div>

# In[5]:


import matplotlib.pyplot as plt


# In[6]:


plt.plot([0,1,2,3,4,5],'-sk')


# ## Submodules

# Many modules contain submodules. These can be accessed by calling `<module>.<submodule>`

# <div class="admonition tip alert alert-warning">
# <p class="first admonition-title" style="font-weight: bold;">Tip</p>
# If you type a module name. you can use `tab` to discover the available submodules
# </div>

# In[ ]:


plt.


# ## Making Your Own Modules

# You can make your own modules by building a function

# <div class="admonition tip alert alert-success">
# <p class="first admonition-title" style="font-weight: bold;">Syntax</p>
# 
# <body>
#     <pre><code id="python_code">
#     def module_name(input):
#         a = 'line 1'
#         b = input
#         return a, b
#     </code></pre>
#     <script type="text/javascript">
#         window.onload = function(){
#             var codeElement = document.getElementById('python_code');
#             // Add code mirror class for coloring (default is the theme)
#             codeElement.classList.add( 'cm-s-default' );
#             var code = codeElement.innerText;
# 
#             codeElement.innerHTML = "";
# 
#             CodeMirror.runMode(
#               code,
#               'python',
#               codeElement
#             );
#         };
#     </script>
# </body>     
#     
# </div>

# In[7]:


def Drexel(college):
    return "Drexel " + college


# In[8]:


print(Drexel("engineering"))


# In[9]:


print(Drexel("Arts and Sciences"))


# ## Loading Modules from Files
# 
# You can load modules from files

# This is a script that writes a file

# In[10]:


get_ipython().run_cell_magic('writefile', 'drexel.py', '\ndef Drexel(name):\n    return "I, " + name + " am a Drexel Dragon"\n')


# In[11]:


import drexel as Drexel


# In[12]:


Drexel.Drexel("Jay")


# ### Reloading Modules
# 
# Once you load a module if it changes you need to reload it.

# Changing the module

# In[13]:


get_ipython().run_cell_magic('writefile', 'drexel.py', '\ndef Drexel(name):\n    return "I, " + name + " am a Drexel Dragon Engineer!!"\n')


# Using `importlib.reload` to reload the module. 

# In[14]:


import importlib
importlib.reload(Drexel)


# In[15]:


Drexel.Drexel("Jay")


# ## Existing Python Packages

# In[16]:


from IPython.display import IFrame
IFrame('https://wiki.python.org/moin/UsefulModules', width=800, height=1200)

