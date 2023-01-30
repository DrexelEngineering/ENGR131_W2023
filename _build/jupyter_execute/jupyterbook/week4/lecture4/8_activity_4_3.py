#!/usr/bin/env python
# coding: utf-8

# # 💻 Activity 4.3: Analyzing Text
# 
# A common tasks for a computer program is to analyze text for structural characteristics. This can be used to determine readability. We have provided you with a text document from a news article. Build a set of functions, and use the `map` function to count 
# 1. The number of words 
# 2. The average word length
# 3. The average number of words per sentence
# 4. As a bonus plot a histogram of the word length. Use the matplotlib function `hist` 

# In[1]:


import requests

response = requests.get('https://raw.githubusercontent.com/DrexelEngineering/ENGR131_W2023/main/jupyterbook/week4/lecture4/assets/article.txt')
article = response.text


# Print the article to read it

# In[ ]:


...


# Write a function that counts the number of strings split by a substring.
# 
# Note: for map to work you need to set a default string to split by

# In[ ]:


...


# Write a function that counts the length of a string

# In[ ]:


...


# Write your function that does all of the computation and then prints the results

# In[ ]:


...


# Code to make a histogram of the word length

# In[ ]:


...

