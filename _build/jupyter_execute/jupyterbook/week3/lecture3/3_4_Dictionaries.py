#!/usr/bin/env python
# coding: utf-8

# # 📝 Dictionaries

# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered and changeable. Dictionaries do not allow duplicates.

# Dictionaries are written with curly brackets, and have keys that correspond to values:
# 

# In[1]:


thisdict = {
    "Student": "Jay",
    "University": "Drexel",
    "College": "Engineering",
    "class": 2024,
}

print(thisdict)


# ## Dictionary Items

# Dictionary items are ordered, changeable, and does not allow duplicates.
# 

# Dictionary items are presented in key:value pairs and can be referred to by using the key name.
# 

# In[2]:


thisdict = {
    "Student": "Jay",
    "University": "Drexel",
    "College": "Engineering",
    "class": 2024,
}

print(thisdict["class"])


# ## Ordered Dictionary

# The meaning of "ordered" is that the items in a dictionary have a defined order, and that order will not change.
# 

# This allows you to iterate through a dictionary in a set order. This concept will become important especially when using loops. 

# ## Changeable

# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# 

# In[3]:


thisdict["class"] = 2025

print(thisdict["class"])


# In[4]:


thisdict["major"] = "Undeclared Engineering"

print(thisdict)


# ## Duplicates are Not Allowed
# 

# Dictionary keys must be unique. Dictionaries cannot have two items with the same key:

# In[5]:


thisdict = {
    "Student": "Jay",
    "University": "Drexel",
    "College": "Engineering",
    "class": 2024,
    "class": "Engr131",
}

print(thisdict)


# If code is written in this way, the dictionary will have the last entry to the key after the code is executed.

# ## Dictionary Length

# In[6]:


print(len(thisdict))


# ## Dictionary Item Types

# Items in dictionaries can be of any type

# In[7]:


thisdict = {
    "Student": "Jay",
    "University": "Drexel",
    "College": "Engineering",
    "class": 2024,
    "colors": ["blue", "gold"],
    "graduated": False,
}

print(thisdict)


# ## Type of a Dictionary

# Python dictionaries are viewed as the type `dictionary`.

# In[8]:


print(type(thisdict))


# ## Dictionary Constructor
# 
# A dictionary is defined or built with code such as the following.

# In[9]:


thisdict = dict(
    Student="Jay",
    University="Drexel",
    College="Engineering",
    Class=2024,
    colors=["blue", "gold"],
    graduated=False,
)


# In[10]:


print(thisdict)


# ## Accessing Items From Dictionary

# ### Getting a Value
# 
# The value associated with the key is accessed by putting the key in `[]` immediately following the dictionary name.

# In[11]:


print(thisdict["Class"])


# In[12]:


x = thisdict.get("Class")

print(x)


# ### Getting Keys
# 
# Returns all the keys in a dictionary. The keys are returned in order.

# In[13]:


x = thisdict.keys()

print(x)


# ### Get Values
# 
# Returns all of the values in a dictionary. The values are returned in order

# In[14]:


x = thisdict.values()

print(x)


# ### Get Items
# 
# This returns the key:value pairs. The results are returned in order.

# In[15]:


x = thisdict.items()

print(x)


# ## Modifying a Dictionary

# ### Updating Values

# #### By Assignment

# In[16]:


print(thisdict["Class"])

thisdict["Class"] = 2025

print(thisdict["Class"])


# #### Using the Update Method

# In[17]:


thisdict.update({"Class": 2024})

print(thisdict)


# ### Removing Items

# Removing by key value

# In[18]:


thisdict = dict(
    Student="Jay",
    University="Drexel",
    College="Engineering",
    Class=2024,
    colors=["blue", "gold"],
    graduated=False,
)

thisdict.pop("Class")

print(thisdict)


# Removing the last item

# In[19]:


thisdict.popitem()
print(thisdict)


# ## Copying a Dictionary

# You might think that you can copy a dictionary using assignment.

# In[20]:


thisdict_copy = thisdict


# Actually, when you assign a dictionary to a new variable, it will occupy the same spot in memory. 

# In[21]:


thisdict_copy is thisdict


# In[22]:


# This will clear the dictionary
thisdict_copy.clear()

print(thisdict)


# The original dictionary has been deleted.

# ### `.copy()` method
# 
# This method makes a copy in a different location in memory. It is necessary to make a copy in a different location in memory in order to modify each copy independently.

# In[23]:


thisdict = dict(
    Student="Jay",
    University="Drexel",
    College="Engineering",
    Class=2024,
    colors=["blue", "gold"],
    graduated=False,
)

thisdict_copy = thisdict.copy()


# In[24]:


thisdict_copy is thisdict


# The objects are not the same.

# In[25]:


thisdict_copy == thisdict


# The values are the same.

# ### `.clear()` method
# 
# This method removes the key:value pairs from the dictionary to which it is applied.

# In[26]:


# This will clear the dictionary
thisdict_copy.clear()

print("thisdict_copy is now cleared:")
print(thisdict_copy)

print("thisdict was unchanged:")
print(thisdict)


# ## Nested Dictionaries

# Using a single dictionary constructor, one can have nested dictionaries in one dictionary. 

# In[27]:


mystudents = {
    "Student1": {"name": "Quinn", "year": 2024},
    "Student2": {"name": "River", "year": 2022},
    "Student3": {"name": "Jay", "year": 2023},
}

print(mystudents)


# Alternatively, if those dictionaries are separately assigned, they can then be combined.

# In[28]:


student1 = {"Student": {"name": "Quinn", "year": 2024}}

student2 = {"Student": {"name": "River", "year": 2022}}

student3 = {"Student": {"name": "Jay", "year": 2023}}

mystudents = {"Student1": student1, "Student2": student2, "Student3": student3}

print(mystudents)

