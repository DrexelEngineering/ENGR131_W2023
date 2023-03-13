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


# In[1]:


import numpy as np

def roll():
    return np.random.randint(1,6, size=2).sum()


# On the initial come out roll, if you bet the pass line you win on a 7 or 11, and lose on a 2,3, or 12. 
# 
# 2. Implement a function `come_out_roll` for the pass line that rolls accepts a bet amount, returns the amount of money won or lost. Since we do not yet know if statement think of how to do this with Booleans as integers

# In[ ]:


...


# In[2]:


def come_out_roll(bet_amount):
    roll_ = roll()
    print(roll_)
    win = (roll_==7)*bet_amount*2 + (roll_==2)*bet_amount*-1 + (roll_==3)*bet_amount*-1 + (roll_==12)*bet_amount*-1
    return win


# Test your function here:

# In[ ]:


...


# In[3]:


come_out_roll(10)


# 3. Build a decorator that converts this number into a string that tells the player how much they won or lost

# In[ ]:


def announce(func):
    def wrapper(..., ...):
        ...


# In[4]:


def announce(func):
    def wrapper(*args, **kwargs):
        win = func(*args, **kwargs)
        out = int(win>0) * f'Congratulations you won {win}' + int(win<0) * f'Sorry you lost {win}' + int(win==0) * f'You did not win or lose'
        print(out)
    return wrapper


# In[ ]:


...
def come_out_roll(bet_amount):
    ...


# In[5]:


@announce
def come_out_roll(bet_amount):
    roll_ = roll()
    print(roll_)
    win = (roll_==7)*bet_amount*2 + (roll_==2)*bet_amount*-1 + (roll_==3)*bet_amount*-1 + (roll_==12)*bet_amount*-1
    return win


# In[ ]:


...


# In[6]:


come_out_roll(10)

