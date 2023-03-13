#!/usr/bin/env python
# coding: utf-8

# # 💻 Activity 3.2: Profanity & Word Count Detector
# 
# ## Task 1: Detect & Replace Profanity
# The growth of public forums has required automated filters to remove profanity and other inappropriate content from the web. We have provided you with two emails from a newsgroup dataset. We would like you to find and remove the profanity using string tools. 
# 
# Since the articles selected do not have profane content we will assume the word "philosopher" is profane.

# In[1]:


from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(subset='train', categories = ['sci.med'])
Article_1 = newsgroups_train.data[0]
Article_2 = newsgroups_train.data[1]


# In[2]:


print(Article_1)


# In[3]:


print(Article_2)


# 1. Determine if there is a profane word in the article?

# In[4]:


# Article 1



# In[4]:


"philosopher" in Article_1


# In[6]:


# Article 2



# In[5]:


"philosopher" in Article_2


# 2. Replace the profane word with `****`

# In[8]:


# Replace 



# In[6]:


Article_1 = Article_1.replace("philosopher", '****')


# In[10]:


# check both articles visually
print(Article_1)
print(Article_2)


# ## Task 2: Evaluate Word Limit
# 
# Some forums may like to impose a word limit on posts.
# 
# Use what you have learned about methods that operate on strings to 
# 1. count the number of words, and 
# 2. determine if the number of words in each article is greater than the word limit of 200.

# In[11]:


...


# In[7]:


print(f"Article 1 has {len(Article_1.split(' '))} words")
print(f"Article 2 has {len(Article_2.split(' '))} words")


# In[ ]:




