#!/usr/bin/env python
# coding: utf-8

# # 📝Week 7 - Lab Intro
# 
# In this lab introduction we will briefly review and discuss dictionaries, a data structure used in this week's lab.

# ## Dictionaries

# ### Creating an empty dicitonary
# 
# You can use curly braces or `dict()` to create an empty dicitonary

# In[ ]:


# one way to make an empty dicitonary
d1 = {}

# another way to make an empty dicitonary
d2 = dict()


# ### Filling the dictionary
# 
# You can fill a dictionary with the following syntax:
# 
# `dict_name[key] = value`

# In[ ]:


d = {}

d["A"] = 3
d["B"] = 4
d["C"] = 5

print(d)


# ### Creating a dictionary with starting items
# Dictionary items are given as `key:value` pairs separated by commas.

# In[ ]:


my_pets = {
    "dogs" : 1,
    "cats" : 2,
    "fish" : 5
}

print(my_pets)


# ### Overwriting values
# 
# Each key can only have one value, so if you asssign a value to a key that's already been used, it is overwritten.

# In[ ]:


my_pets = {
    "dogs" : 1,
    "cats" : 2,
    "fish" : 5
}

# if we got one more fish, what's another way we can write the following line?
my_pets["fish"] = 6

print(my_pets)


# While each key can only appear once, the same value can be used multiple times. For instance:

# In[ ]:


my_pets = {
    "dogs" : 2,
    "cats" : 2,
}

print(my_pets)


# #### What can be a dictionary key?
# 
# Let's see which types can be a dictionary key. We'll use the error messages to find which statements are valid.

# In[ ]:


import numpy as np

test_dict = {}

# string
test_dict["A"] = 3

# int
test_dict[5] = 3

# float
test_dict[3.7] = 3

# list
test_dict[[3,4,5]] = 3

# tuple
test_dict[(3,4,5)] = 3

# numpy array
test_dict[np.array([1,1,1])] = 3

# function
test_dict[len] = 3

# dictionary
test_dict[{"A":5}] = 3

print(test_dict)


# A dictionary key must be "hashable," meaning it is a type of object that cannot be changed after its creation. 
# 
# Thus it can be fed into a 'hash" function, which generates an index (an integer) specific to that object.

# #### What can be a dictionary value?

# Let's do the same to determine what objects can be values in a dictionary.

# In[ ]:


import numpy as np

test_dict = {}

# string
test_dict["A"] = "A"

# int
test_dict["B"] = 5

# float
test_dict["C"] = 3.7

# list
test_dict["D"] = [3,4,5]

# tuple
test_dict["E"] = (3,4,5)

# numpy array
test_dict["F"] = np.array([1,1,1])

# function
test_dict["G"] = len

print(test_dict)


# ### Counting with a dictionary

# Dictionaries are a natural choice of data structure when you when to count different things.
# 
# Consider the following example with counting suits in a hand of playing cards:

# In[ ]:


# cards are represented by a tuple: `(value, suit)`
hand_of_cards = [("ace", "spades"),("jack", "diamonds"),("queen", "spades"),("four", "spades"), ("jack", "hearts")]


# initialize a dictionary for counting the suits, all starting at 0
suit_counts = {"clubs" : 0,
                "diamonds" : 0,
                "hearts" : 0,
                "spades" : 0}

# loop through the hand of cards, unpacking the tuple into value and suit variables
for value, suit in hand_of_cards:
    # increment the value located at key=suit
    suit_counts[suit] += 1


# print the final dictionary of counts
print(suit_counts)

