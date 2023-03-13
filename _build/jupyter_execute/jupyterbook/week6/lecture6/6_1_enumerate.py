#!/usr/bin/env python
# coding: utf-8

# # 📝 Introduction of Enumerate

# A skill necessary for programming is reading documentation to learn how to use functions. 
# 
# For example, consider `enumerate`.

# ## Built-in Function
# 
# `enumerate(iterable, start=0)`
# 
# Return an enumerate object. `iterable` must be a sequence, an iterator, or some other object which supports iteration. The `__next__()` method of the iterator returned by `enumerate()` returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over `iterable`.
# 
# ```python
# 
# >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# >>> list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
# >>> list(enumerate(seasons, start=1))
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
# ```
# 

# ## Practice with `enumerate`
# 
# The Eagles wide receivers have Batman nicknames. Let's use `enumerate` to match the wide receiver with the correct nickname.

# In[1]:


wideReceivers = ['A. J. Brown', 'DeVonta Smith', 'Quez Watkins']
nicknames = ['Swole Batman', 'Skinny Batman', 'Fast Batman']

print(list(enumerate(wideReceivers)))


# In[2]:


for count, realName in enumerate(wideReceivers):
    print(f'{realName} is also known as {nicknames[count]}.')

