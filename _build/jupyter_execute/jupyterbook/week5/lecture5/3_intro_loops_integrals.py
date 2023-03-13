#!/usr/bin/env python
# coding: utf-8

# # 📝 Introduction to Loops with Integrals

# ## Utility of loops
# 
# Branching causes specific blocks of code to be executed only under certain conditions. The conditions are articulated as logical expressions. 

# ## How do you write loops?
# 
# The simplest version of loop is a "for loop". 

# ```python
# for looping_variable in sequence:
#     code_block
# ```
# 

# More complex structures are possible with "while statements". 

# ```python
# while logical_expression:
#     # code_block is repeated until logical expression is false
#     code_block
# ```
# 

# Just like if-statements, for-loops can be nested. 
# 
# **EXAMPLE:** Let `x` be a two-dimensional array, `[[10, 20],[30 40]]`. Use a nested for-loop to sum all the elements in `x`. 

# In[1]:


import numpy as np

x = np.array([[10, 20], [30, 40]])
print(x)

n, m = x.shape
s = 0
for i in range(n):
    for j in range(m):
        s += x[i, j]

print(s)


# ## Using loops in integration
# 
# Many engineering applications require integration, which can be understood as calculating the area under a curve. For example, consider the following:

# * estimating the force of water against a bridge or dam
# 
# * determining the amount of time a reactor should operate for a given chemical to be produced
# 
# * processing audio or electrical signals into meaningful input 
# 
# * determining the force required to move an object a given distance

# For example, to deposit materials on graphene, one could observe the progress of experiments over time to find the amount of mass deposited to optimize the conditions for deposition.

# ![](https://i0.wp.com/www.atomiclimits.com/wp-content/uploads/2017/06/Chapter_1_Figure_5.png?w=1476&ssl=1)

# The Riemann integral is the simplest method of approximating the area under a curve. One simply 

# * divides the area under the curve into rectangles of equal width $h$ and height $f(x_i)$,
# 
# * calculates the area for each rectangle using $A_i = hf(x_i)$, and 
# 
# * sums the areas of each rectangle between some smaller value of $x$ called $a$ and a larger value of $x$ called $b$.

# Mathematically, this process is expressed as 
# 
# $$\int_{x_i}^{x_{i+1}} f(x) dx= hf(x_i) + O(h^2).$$
# 
# ![](https://i.ytimg.com/vi/NgLd16Dksrs/maxresdefault.jpg)

# In[ ]:




