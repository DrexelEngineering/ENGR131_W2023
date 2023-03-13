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

# In[2]:


...


# In[2]:


print(article)


# Write a function that counts the number of strings split by a substring.
# 
# Note: for map to work you need to set a default string to split by

# In[4]:


...


# In[3]:


def counter(article, split=" "):
    return len(article.split(split))


# Write a function that counts the length of a string

# In[6]:


...


# In[4]:


def string_len(word):
    return len(word)


# Write your function that does all of the computation and then prints the results

# In[8]:


...


# In[5]:


<<<<<<< Updated upstream
import numpy as np
=======
>>>>>>> Stashed changes
word_counts = counter(article, " ")
sentence_counts = counter(article, ". ")
word_lengths = np.array(list(map(string_len, article.split(" "))))
average_word_length = word_lengths.sum() / word_counts

sentence_list = article.split(". ")
word_in_sentence = np.array(list(map(counter, sentence_list)))
average_sentence_length = word_in_sentence.sum() / len(sentence_list)

print(f"Word count = {word_counts}")
print(f"Average Word Length = {average_word_length:0.2f}")
print(f"Average Sentence Length = {average_sentence_length:0.2f}")


# Code to make a histogram of the word length

# In[10]:


...


<<<<<<< Updated upstream
# In[6]:
=======
# In[ ]:
>>>>>>> Stashed changes


import matplotlib.pyplot as plt

plt.hist(word_lengths, 10)

<<<<<<< Updated upstream

# In[ ]:




=======
>>>>>>> Stashed changes
