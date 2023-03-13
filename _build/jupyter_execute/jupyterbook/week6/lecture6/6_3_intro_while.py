#!/usr/bin/env python
# coding: utf-8

# # 📝 Introduction to `while` Loops

# ## Structure

# While loops are executed until the logical expression evaluates to false.

# ```python
# while logical_expression:
#     # code_block is repeated until logical expression is false
#     code_block
# ```
# 

# ## Which loop to use? 

# Therefore, `while` loops are appropriate when the number of times the code block needs to be executed is indefinite. 
# 
# `for` loops are appropriate when the number of times the code block needs to be executed is definite or well understood.

# When using while loops, ensure that the loop does not run *infinitely*, which it will if the logical expression never becomes false.

# Which one(s) of these loops will run infinitely? 
# 
# Try to evaluate it without executing the code.

# In[ ]:


# Option A
x = 1
while x >= 0:
    x /= 0.1


# In[ ]:


# Option B
x = 1
while x >= 0:
    x -= 0.1


# In[ ]:


# Option C
x = -4
while x < 0:
    if x % 2 == 0:
        x -= 1
    else: 
        x += 1


# ### Interrupt infinite loops
# 
# If you accidentally execute an infinite loop, interrupt the execution by clicking the ◼️ beside the ▶ at the top of the JupyterLab screen.
