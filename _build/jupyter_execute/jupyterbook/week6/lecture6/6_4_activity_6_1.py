#!/usr/bin/env python
# coding: utf-8

# # 💻 Activity 6.1: Write the modulus operator using a while loop
# 
# We implemented the modulus operator using a for loop. Now, write it using a while loop.

# In[1]:


# add your code where the ... appears
def whileModulus(dividend, divisor):
    ...


# In[2]:


def whileModulus(dividend, divisor):
    remainder = dividend
    while remainder >= 0:
        remainder -= divisor
    return (remainder+divisor)


# In[3]:


print(whileModulus(5,3))
print(5%3)


# In[4]:


print(whileModulus(4,2))
print(4%2)


# In[5]:


print(whileModulus(100,21))
print(100%21)

