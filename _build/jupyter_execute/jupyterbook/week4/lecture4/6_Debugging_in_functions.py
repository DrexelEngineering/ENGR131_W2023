#!/usr/bin/env python
# coding: utf-8

# # 📝 Debugging in Python
# 
# When you write complex code with functions you are more likely to encounter hidden bugs

# Debuggers are effective tools to identify problems by stepping through code one step at a time.

# Consider the code:

# In[1]:


x = 20


def my_function(value):
    y = value
    z = y + 3
    print(z)


my_function(7)


# Assume we wanted to figure out why z is not returning the value we expect. You might want to see what the value y is.

# Since Y is a local variable you do not have direct access. You need to add a breakpoint and use a debugger reveal the inner workings of your code.

# ## Using the Debugger in JupyterHub

# 1. Click the bug on the right panel.
# 
# ![](images/Debugger_1.png)

# 2. Click the bug inside your notebook
# 
# ![](images/Debugger_2.png)

# 3. Add a breakpoint - This is where you want your code to stop
# 
# ![](images/breakpoints.png)

# 4. You can step through the program and reveal the variable as they are assigned
# 
# ![](images/Step_in.png)

# It is best to use the debugger only when necessary because it slows down the computation on your kernel and uses a lot of memory. 
