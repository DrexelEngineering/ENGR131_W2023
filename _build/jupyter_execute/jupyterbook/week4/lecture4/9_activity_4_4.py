#!/usr/bin/env python
# coding: utf-8

# # 💻 Activity 4.4: Using Functions to Build the Game of Craps

# In the game of craps there are many bets that you can place and actions that you can take. We will use functions to implement some of the basic components of one of the most simple best, the pass line. 
# 
# In craps, 2 dice are rolled and wins and losses are determined by sum of the dice

# 1. Write a function `roll` that rolls 2 dice, and takes the sum.
# 
# Throughout the code the ... indicate where you should add your code.

# In[ ]:


import numpy as np

...


# On the initial come out roll, if you bet the pass line you win on a 7 or 11, and lose on a 2,3, or 12. 
# 
# 2. Implement a function `come_out_roll` for the pass line that rolls accepts a bet amount, returns the amount of money won or lost. Since we do not yet know if statement think of how to do this with Booleans as integers

# In[ ]:


...


# Test your function here:

# In[ ]:


...


# 3. Build a decorator that converts this number into a string that tells the player how much they won or lost

# In[ ]:


def announce(func):
    def wrapper(..., ...):
        ...


# In[ ]:


...
def come_out_roll(bet_amount):
    ...


# In[ ]:


...

