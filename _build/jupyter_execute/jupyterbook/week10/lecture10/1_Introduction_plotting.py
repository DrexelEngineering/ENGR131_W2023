#!/usr/bin/env python
# coding: utf-8

# # 📝 Introduction to Plotting in Python
# 
# - Python would serve you well as your primary tool for visualizing quantitative data for most classes you will take as well as in your career.
# 
# - Matplotlib is the most common used Python package for 2-dimensional graphics.
# 

# ## Data visualization
# 
# - Graphics display information using a coordinate system, numbers, lines, symbols, words, shading, and color.
# 

# - Graphics are instruments for reasoning about quantitative information.
# 
# - Valuable graphics allow large collections of data to be turned into actionable information.
# 
# - For engineers, making **easy-to-interpret, honest graphical representations of information** is often the most effective way of communicating scientific information.
# 
# - **Graphics can be more informative than statistics!**
# 
# 

# ### What characterizes a valuable graphic?
# 

# - Presents data accurately, clearly, and efficiently
# 

# - Encourages the viewer to relate important pieces of information
# 

# ## Examples of data visualization
# Famous dot map of deaths from Cholera in central London in September 1854 by Dr. John Snow 
# 
# **What could someone learn from reading this graphic?**
# 
# ![title](figs/snow.png)
# 
# 

# ### Including Various Dimensions
# 
# - Most data have at least two dimensions, which are represented on an x-axis and y-axis.
# 
# - Color, size, and marker type are common ways to represent additional dimensions of data.
# 

# **What are the dimensions of data shown here and which feature on the figure is used to show each one?**

# <img src=https://raw.githubusercontent.com/DrexelEngineering/ENGR131_W2023/main/jupyterbook/week10/lecture10/median-annual-wages-in-2.png>
# 

# ## Principles of Graphical Excellence
# 
# - Presentation of data needs to consider _substance, statistics, and design_
# 

# - Complex ideas should be communicated with _clarity, precision, and efficiency_
# 

# - Graphics must not deceive the audience, intentionally or unintentionally.

# ### What is wrong with this figure?
# 
# <img src="figs/Army_Figure.png" width="1200">
# 

# ## Guiding Principles
# 

# ### Appropriate visualization for the data
# 
# - Avoid if possible since people are not good at determining angles.
# 
#   ![title](Figs/pie_chart_1.png)
# 

# - A bar chart or a line chart is much more informative
# 
#     ![title](Figs/bar_chart_1.png)
# 
# 

# ### Plots with multiple y-axes
# 
# - Multiple y-axes are possible when it is important to show the interrelationship of two variables with different absolute values.
# 
# - Be intentional and careful when choosing this strategy.
# 

# ![title](Figs/two_lines_1.png)
# 

# ![title](Figs/two_lines_2.png)
# 

# ### Make the y-value zero at the origin
# 
# - Most bar charts and figures with physical quantities are best represented with a value of zero at the origin.
# - If the reference point and all of the values are greater than zero, it may be acceptable to have a non-zero value at the origin.
# 

# ## How to plot in Python
# 
# Plotting is easy using matplotlib.

# In[1]:


import matplotlib.pyplot as plt

# some example data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# try to plot the data
try:
    plt.plot(x, y)
    plt.show()
except:
    print("Something went wrong with the plot!")


# You might have noticed we used `try` and `except` this is called exception handling.

# If a code in a try statement encounters an error it continues with the except statement. 
# * This is helpful in making code where it is not easy to define a branching statement for all cases.
# * This is also the basis of error handeling, which makes your code fail gracefully.

# In[2]:


import matplotlib.pyplot as plt

# some example data
x = [1, 2, 3, 4, plt]
y = [2, 4, 6, 8, 10]

# try to plot the data
try:
    plt.plot(x, y)
except:
    print("Something went wrong with the plot!")


# In[ ]:




