#!/usr/bin/env python
# coding: utf-8

# # Review of For Loops

# ## Structure
# 
# A "for loop" uses iteration over a sequence.

# ```python
# for looping_variable in sequence:
#     code_block
# ```
# 

# ## Recap: code modulus function

# Recall: the modulus operator provides the remainder left after dividing one number by another.

# How would you use a `for` loop to calculate the result of the modulus operator (without using this operator)?
# 
# 1. First, think about the method you would use. 
# 
# 2. Test that process with 5 (= dividend) divided by 3 (= divisor) and 4 (= dividend) divided by 2 (= divisor).

# In[ ]:


# add your code where the ... appears
def forModulus(dividend, divisor):
    numDiff = ...
    remainder = ...
    for i in range(...):
        ...
    return remainder


# In[ ]:


print(forModulus(5,3))
print(5%3)


# In[ ]:


print(forModulus(4,2))
print(4%2)


# The notes for Session 5 benefitted from the availability of [Python Programming and Numerical Methods: A Guide for Engineers and Scientists](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html) through the MIT License.
