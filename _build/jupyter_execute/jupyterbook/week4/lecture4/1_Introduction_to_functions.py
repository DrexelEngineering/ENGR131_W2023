#!/usr/bin/env python
# coding: utf-8

# # 📝 Introduction to Functions

# ## What are Functions?
# 
# ![](https://raw.githubusercontent.com/jagar2/Fall_2022_MEM_T680Data_Analysis_and_Machine_Learning/main/jupyterbook/Topic_4/figs/function_calls.gif)
# 

# Functions are a convenient way to divide your code into useful blocks
# * order our code 

# * make it more readable

# * reuse it and save some time. 

# * way to define interfaces so programmers can share their code.

# ## How do you write functions?

# ```python
# def name_of_function(input_argument1, input_argument2):
#     Line_1_of_function = all_lines_in_function_must_be_tab_indented
#     Line_2_of_function = all_lines_in_function_must_be_tab_indented
# ```
# 

# ## The most simple function

# In[1]:


def my_function():
    print("I am a Drexel Dragon")


# **When you ran this code why did it not print the output?**

# ```{toggle}
# It did not print because the code just defined the function my_function. You need to call the function for it to run.  
# ```

# In[2]:


my_function


# **Why did this not print the result?**

# ```{toggle}
# We just typed the object for the function and it returned the object to the function. You need to call the function using `()` for it to run
# ```

# In[3]:


my_function()


# ## Functions with Arguments

# In[4]:


def my_function(name, major):
    print(f"I, {name} am a Drexel Dragon, and I am majoring in {major}")


# In[5]:


my_function("Jay", "Mechanical Engineering")

