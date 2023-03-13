#!/usr/bin/env python
# coding: utf-8

# # 📝 Interrupting Loops

# ## Keywords for control inside loops
# 
# `break`: immediately stops the execution of the nearest loop
# 
# `continue`: skips the remainder of the code block and starts the next iteration

# ```python
# for looping_variable in sequence:
#     if logical_expression:
#         continue
#     code_block
#     if logical_expression:
#         break
# ```
# 

# ![](images/breakContinue.jpeg)

# ## Examples of `break` and `continue`

# Refresh on the implementation of these keywords in the following examples before using them in an activity.

# In[1]:


# iterate over numbers up to five but do not print 2
for i in range(5):
    
    if i == 2:
        continue
        
    print(i)


# In[2]:


# use a break to prevent an infinite loop
n = 0
while n > -1:
    n += 1
    if n > 1000:
        break
print(n)

