#!/usr/bin/env python
# coding: utf-8

# # Lab 1: Commenting Code 🧪🖥
# 
# As an engineer, it is important to not only be able to write code, but also to read and understand code written by others. One way to improve your understanding of someone else's code is by adding comments to the code.
# 
# Comments are lines of code that are not executed by the computer, but are included to explain what is happening in the code. They can be extremely helpful for anyone reading the code, including yourself, to understand (or remember) the logic and purpose behind each line of code. In Python, any line starting with `#` is a comment. For example, the following line of code has a comment above it explaining what the code does:
# 
# ```python
# # store the value 3 in a variable called x
# x = 3
# ```
# 
# In this lab assignment, you are given some code to read through, and your task will be to add comments to the code to explain what is happening. Don't worry if the code appears complicated and beyond your current understanding. This is intentional, challenge activities are the best way to learn. 
# 
# To help you should make use of the Python documentation (https://docs.python.org/3/) as you explore and learn the Python syntax. Most documentation for Python code is hosted online.
# 
# The code assigns weekly project groups from a spreadsheet of student names. The code has been split into sections with headers summarizing the code in each cell. You should comment every single line since every single line matters to the computer. Some comments have been provided to you to get you started.
# 
# By the end of this assignment, you should have a better understanding of how to read and understand code, as well as how to effectively use comments to explain your code. Good luck!

# ## Import Libraries

# In[1]:


# import the scientific computing library numpy and give it the nickname np
import numpy as np
import random
import csv


# ## Define Student class

# In[2]:


# create a python class called Student
class Student:

    # create a constructor for the Student class that has arguments: leader, partners, and name
    def __init__(self, leader, partners, name):
        # store the name in a data member called self.name
        self.name = name
        self.leader = leader
        self.partners = partners

    # create a method called _leader
    def _leader(self):
        # increment the value of self.leader by 1
        self.leader += 1


# ## Define Group class

# In[3]:


class Groups:
    def __init__(self, group_number, group_size, group_members, group_leader):
        self.group_number = group_number
        self.group_size = group_size
        self.group_member = group_members
        self.group_leader = group_leader


# ## Week class

# In[4]:


class Week:
    def __init__(self, week_number, groups):
        self.week_number = week_number
        self.groups = groups


# ## Load and parse the spreadsheet of filenames

# In[5]:


path = './baby-names-by-state.csv'
# open the file at the specified path for reading and give it the name f
with open(path, 'r') as f:
    # create a csv reader object to read the comma-separated file
    reader = csv.reader(f, delimiter=',')
    headers = next(reader)
    data = np.array(list(reader))

names_ = np.unique(data[:, 2])


# ## Assign the groups

# In[6]:


num_students = 177

num_of_weeks = 5

group_size = 3

# Sets the names for the students
# Names were taken from the list of most common names
names = random.choices(names_, k=num_students)

student_list = []

for name in names:
    student_list.append(Student(0, [], name))

num_groups = len(student_list)//group_size

groups_sizes = []

# If the number of students can be evenly split into groups
if len(student_list) % num_groups == 0:

    group_sizes = [group_size] * num_groups

elif len(student_list) % num_groups <= group_size * .8:
    group_sizes = [group_size] * (num_groups - (len(student_list) % num_groups)) + [
        group_size + 1] * (len(student_list) % num_groups)

week_list = []

for week in range(num_of_weeks):

    leader_number = [student.leader for student in student_list]

    leader_value = sorted(leader_number)[:len(group_sizes)]

    def select_leader(leader_options):
        return np.random.choice(leader_options)

    grouped_students = []
    group_list = []

    for i, _leader_value in enumerate(leader_value):

        leader_number = [student.leader for student in student_list]

        leader_options = np.argwhere(
            np.array(leader_number) == _leader_value).squeeze()

        leader_ = select_leader(leader_options)

        while leader_ in grouped_students:
            leader_ = select_leader(leader_options)

        group_list.append(Groups(i+1,
                                 group_sizes[i],
                                 [student_list[leader_]],
                                 [student_list[leader_]]))

        student_list[leader_]._leader()

        grouped_students.append(leader_)

    for i, group in enumerate(group_list):
        for j in range(group.group_size-1):
            remaining_students = set(
                np.arange(len(student_list)))-set(grouped_students)

            student_num_ = np.random.choice(list(remaining_students))

            group.group_member.append(student_list[student_num_])

            grouped_students.append(student_num_)

    week_list.append(Week(week + 1, group_list))


# ## Print out the groups

# In[7]:


for week in week_list:
    print(f'Week {week.week_number}\n')

    for group in week.groups:
        print(
            f'Group {group.group_number} - lead by {group.group_leader[0].name}')
        print([i.name for i in group.group_member])

    print('\n')

