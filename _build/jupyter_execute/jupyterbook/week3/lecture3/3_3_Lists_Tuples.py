#!/usr/bin/env python
# coding: utf-8

# # 📝 Collections in Python

# ## Lists
# 
# Lists are defined using `[]`, items in a list are separated by `,`.

# Lists are used to store multiple items in a single variable.

# ### Lists are ordered

# In[1]:


list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 1]


# In[2]:


[1, 2, 3, 4] == [2, 3, 4, 1]


# **You can add a value to a list.**
# * This can be done with the built-in method `<obj>.append(<index>)`

# In[3]:


list1.append(5)


# In[4]:


list1


# **You can remove items from a list**
# * this can be done with the built-in method `<obj>.pop(<index>)`

# In[5]:


list1.pop(2)


# In[6]:


list1


# ### Lists Allow Duplications

# In[7]:


list1 = [1, 1, 1]


# In[8]:


list1


# ### Changing a value of a list

# <div class="admonition note alert alert-info">
# <p class="first admonition-title" style="font-weight: bold;">Note</p>
# Python supports indexing of ordered objects using `[{index}]`, it is important to note that the index starts at 0. </a>
# </div>

# **Replacing a value**

# In[9]:


list1[0] = "Drexel"


# In[10]:


list1


# **Inserting a value**

# In[11]:


list1.insert(1, "Dragons")


# In[12]:


list1


# ### Sorting Lists

# In[13]:


list1 = [5, 2, 3, 1]


# In[14]:


list1.sort()
list1


# In[15]:


list2 = ["Drexel", "Dragons"]
list2.sort()


# In[16]:


list2


# ### Lists can contain multiple data types

# In[17]:


list1 = ["Drexel", 1, 1.0]


# In[18]:


print(type(list1[0]))
print(type(list1[1]))
print(type(list1[2]))


# **You can even store list of list**

# In[19]:


list2 = [list1, list1]
list2


# or lists of lists of lists

# In[20]:


list3 = [list2, list2]
list3


# **You can get the length of a list using the method `len()`**

# In[21]:


print(len(list1))
print(len(list2))
print(len(list3))


# ## Tuple
# 
# A tuple is a collection that can store multiple ordered items that are **unchangeable**.

# <div class="admonition tip alert alert-success">
# <p class="first admonition-title" style="font-weight: bold;">Syntax</p>
# Tuples are made using ({obj}, {obj})
# </div>

# In[22]:


thistuple = ("Drexel", "Dragons", list2)


# In[23]:


print(thistuple)


# **Usually tuples are used to move objects, which are then unpacked to be used.**

# In[24]:


statement = ("Drexel", "Dragons", "Football", 0)

(University, Mascot, Sport, losses) = statement

print(f"school: {University}")
print(f"Mascot: {Mascot}")
print(f"Sport: {Sport}")
print(f"Lifetime Losses: {losses}")

