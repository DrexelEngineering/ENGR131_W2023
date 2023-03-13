#!/usr/bin/env python
# coding: utf-8

# # 💻 Activity 4.2: Solving an Old School Punishment With a New Trick
# 
# In high school you are the class clown. Your teacher to punish you tells you to write "I will not text jay in spanish class." 100 times. You teacher thinks they are smart and removes all possibilities of copy and paste from your computer. But you are smarter than that! Write a script using dynamic programming concepts that can address your current and future mischievous plans. 
# 
# 1. "I will not hide 250 rubber ducks in math class."  (250 times)
# 2. "I will not cheat off Sarah and Tom in ENGR131 class." (101 times)

# Your function goes here

# In[ ]:


...


# In[1]:


def punishment(multiple, *args):
    action, noun, class_ = args
    print(f"I will not {action} {noun} in {class_} class. \n" * 100) 


# "I will not text jay in spanish class." 100 times

# In[ ]:


...


# In[2]:


punishment(100, 'text','jay',"spanish")


# "I will not hide 250 rubber ducks in math class."  (250 times)

# In[ ]:


...


# In[3]:


punishment(250, 'hide','250 rubber ducks',"Math")


# "I will not cheat off Sarah and Tom in ENGR131 class." (101 times)

# In[ ]:


...


# In[4]:


punishment(101, 'cheat off','Sarah and Tom',"ENGR131")

