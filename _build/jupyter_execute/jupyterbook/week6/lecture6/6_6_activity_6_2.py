#!/usr/bin/env python
# coding: utf-8

# # 💻 Activity 6.2: Apply the break or continue keywords

# ## Revisit for loop implementation of modulus operator
# 
# The implementation of the modulus operator would be more clean with the break or continue statement. 

# Recall: the modulus operator provides the remainder left after dividing one number by another.

# How would you use a `break` or `continue` to make the code for the modulus operator using a `for` loop to make the code more concise?
# 
# 1. Copy your correct code to the cell below. 
# 
# 2. Add `break` or `continue` to make the function more concise.

# In[1]:


# add your code where the ... appears
def forModulus(dividend, divisor):
    ...


# In[2]:


# add your code where the ... appears
def forModulus(dividend, divisor):
    remainder = dividend
    for i in range(dividend):
        if ((remainder-divisor) < 0):
            break
        remainder -= divisor
    return remainder


# In[3]:


print(forModulus(5,3))
print(5%3)


# In[4]:


print(forModulus(4,2))
print(4%2)


# The notes for Session 6 benefitted from the availability of [Python Programming and Numerical Methods: A Guide for Engineers and Scientists](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html) through the MIT License.
