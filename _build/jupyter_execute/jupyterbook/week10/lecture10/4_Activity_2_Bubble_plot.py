#!/usr/bin/env python
# coding: utf-8

# # 💻 Activity 9.2: Making a Updated Bubble Plot of Engineering Jobs
# 
# In this activity, we will make a bubble plot of more recent Bureau of Labor Statistics data for projected engineering jobs. 
# 
# Again, add code where there are `...`

# In[1]:


# import the scientific computing packages with their conventional nicknames
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# ## 0. Read data
# 
# The Bureau of Labor Statistics makes projections about the growth of jobs in given areas. These data need to be read into this Jupyter Notebook to plot them.
# 
# Dataframes are the structure that pandas uses, which is helpful for columns and rows of different kinds of data.

# In[ ]:


# read the employment projection data 
path = "./data/employment-projections.csv"

# open the file at the specified path for reading and give it the name f
with open(path, "r") as f:
    # create a pandas dataframe from the comma-separated file
    df = pd.read_csv(f, delimiter=",")

# shows the first 5 lines of the pandas dataframe
df.head()


# ## 1. Make a simple plot
# 
# The next step is to make a simple bubble plot, which is just a scatter plot with the markers sized by another dimension of the data.
# 
# Like the one we saw earlier in class, we want to see the employment percent change, 2021-2031, on the x-axis, the median annual wage, 2021, on the y-axis, and the number of jobs in 2021 influencing the size of the marker. 
# 
# - To select any set of these values from the dataframe, just use `df` to refer to the dataframe and the string of the column title inside `[]` to choose which one. 
# 
# - Secondly, choose a colormap that is built into `matplotlib` as the argument `cmap='...'`.
# 
# - You can choose a different alpha (between 0.0 and 1.0) to see if you prefer a more transparent set of bubbles.

# In[ ]:


# Create bubble plot of the median annual wage against the percent change in employment with the markers sized by employment in 2021
fig, ax = plt.subplots(figsize=(10, 6))

# use the title of the appropriate column in the output above to replace the ...
employment2021size = (df['...']*2).tolist()

# use the title of the appropriate columns in the output above to replace the ...'s
bubble = ax.scatter(df['...'], df['...'], s=employment2021size, c=range(len(df)), cmap='...', alpha=0.9)

plt.show()


# ## 2. Add axes labels and a title
# 
# The next step is to add informative labels and a title. 
# 
# - Copy your code from up above to replace the commented, incomplete code.
# 
# - Fill in the four `...` to label the axes and make an appropriate title.

# In[ ]:


# Set axes labels and title

# copy your completed code from the task 1
#fig, ax = plt.subplots(figsize=(10, 6))
#
#employment2021size = (df['...']*2).tolist()
#
#bubble = ax.scatter(df['...'], df['...'], s=employment2021size, c=range(len(df)), cmap='...', alpha=0.9)

ax.set_xlabel('...')
ax.set_...('...')
ax.set_title('...')

plt.show()


# ## 3. Label the points and interpret
# The final step is to label each of the bubbles. 
# 
# - Copy your code from up above to replace the commented, incomplete code.
# 
# - Fill in the four `...` to label the axes and make an appropriate title.

# In[ ]:


# Set axis labels and title

# copy your completed code from the task 1
#fig, ax = plt.subplots(figsize=(10, 6))
#
#employment2021size = (df['...']*2).tolist()
#
#bubble = ax.scatter(df['...'], df['...'], s=employment2021size, c=range(len(df)), cmap='...', alpha=0.9)
#
#ax.set_xlabel('...')
#ax.set_...('...')
#ax.set_title('...')

# Add labels to bubbles
for i, row in df.iterrows():
    # first ... should be the string referring to the x-axis data
    # second ... should be the string referring to the y-axis data 
    # third ... shold be the string referring to the type of engineer 
    # feel free to choose different locations for the labels by changing right to left or bottom to top
    ax.text(row['...'], row['...'], row['...'], ha='right', va='bottom')

plt.show()


# ### What kind of engineering does this suggest would be likely to have more jobs when you graduate than now? 
