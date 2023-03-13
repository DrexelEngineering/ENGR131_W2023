#!/usr/bin/env python
# coding: utf-8

# # 📝Creating Multiple Objects of a Class
# 
# - A very powerful utility of classes is that you can instantiate multiple instances of a class with different attributes.
# 

# - This allows you to build scaffolding that supports information, functions, and methods in ways that can be written once and reused.
# 

# ## Going back to Lab 1
# 

# As you learn more, you can start to appreciate things you have seen before in new ways. Let's return to the group randomization assignment we did in Lab 1.
# 

# 1. We start by importing some functions
# 

# In[ ]:


# import the scientific computing library numpy and give it the nickname np
import numpy as np
import random
import csv


# 2. Let's build a class `student` that contains the information about the students in the class.
# 

# In[ ]:


# create a python class called Student
class Student:

    # create a constructor for the Student class that has arguments: leader, partners, and name
    def __init__(self, name, number, leader=0, partners=None):

        # stores the name in a data member called self.name

        self.name = name
        self.leader = leader
        self.partners = partners
        self.number = number

    # create a method called _leader
    def _leader(self):

        # increment the value of self.leader by 1
        self.leader += 1


# 3. We build a class `Groups` that defines each group in the class.
# 

# In[ ]:


class Groups:
    def __init__(self, group_number, group_size, group_members, group_leader):
        self.group_number = group_number
        self.group_size = group_size
        self.group_member = group_members
        self.group_leader = group_leader


# 4. We load a list of Baby Names.
# 

# In[ ]:


path = "./baby-names-by-state.csv"

# open the file at the specified path for reading and give it the name f
with open(path, "r") as f:
    # create a csv reader object to read the comma-separated file
    reader = csv.reader(f, delimiter=",")
    headers = next(reader)
    data = np.array(list(reader))

names_ = np.unique(data[:, 2])


# 5. We can now build a list that contains all of the instantiated student objects.
# 

# In[ ]:


students = []

for i, name in enumerate(names_):
    students.append(Student(name, i))

