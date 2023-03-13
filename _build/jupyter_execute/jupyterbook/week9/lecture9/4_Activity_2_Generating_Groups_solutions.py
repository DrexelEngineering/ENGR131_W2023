#!/usr/bin/env python
# coding: utf-8

# # 💻 Activity 9.2: Building a Group Assignment Tool
# 
# In this class we build a group assignment tool to assign students randomly to groups. Now it is your job to try to blend all the concepts you learned in this class to create this program. We will start with the classes we discussed in lecture.
# 
# Again, add code where there are `...`

# In[1]:


# import the scientific computing library numpy and give it the nickname np
import numpy as np
import random
import csv


# In[2]:


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


# In[3]:


class Groups:
    def __init__(self, group_number, group_size, group_members, group_leader):
        self.group_number = group_number
        self.group_size = group_size
        self.group_member = group_members
        self.group_leader = group_leader


# In[4]:


path = "./baby-names-by-state.csv"

# open the file at the specified path for reading and give it the name f
with open(path, "r") as f:
    # create a csv reader object to read the comma-separated file
    reader = csv.reader(f, delimiter=",")
    headers = next(reader)
    data = np.array(list(reader))

# grabs all of the unique names from the file
names_ = np.unique(data[:, 2])


# In[5]:


# Determine the number of students that you have
num_students = len(names_)

# Assign a parameter for the group size
# for this case make it 3
group_size = 3

# Use the random.choice method to select some number of students
names = random.choices(names_, k=num_students)

# Define an empty list for student
students = []

# Populate the list of students with a student object
# The student object should take the student name and number
for i, name in enumerate(names_):
    students.append(Student(name, i))

# determine the number of full groups that could exist given the number of students
num_groups = len(students) // group_size

# Make a list that will be used to store the size of each group
groups_sizes = []

# Write a branching statement that builds a list containing the size of each group
# We need to think about the different cases
# If the number of students is evenly divisible by the size of the groups then the list is just the size of groups replicated by the number of groups
# If the number of students is not evenly divisible by the size of the groups distribute the remainders
if len(students) % num_groups == 0:

    group_sizes = [group_size] * num_groups

else:
    group_sizes = [group_size] * (num_groups - (len(students) % num_groups)) + [
        group_size + 1
    ] * (len(students) % num_groups)

# write a function that selects a leader from a list of available options
def select_leader(leader_options):
    return np.random.choice(leader_options)


# make an empty list to store students already added to a group
grouped_students = []

# make an empty list that stores the groups of students
group_list = []


# Now you want to populate each group
# 1. You want to iterate through all of the group sizes
# 2. You want to select a leader from the list of students
# 3. You want to check if the selected leader is already in a group. If they are, you want to try again.
# 4. You want to use the object method to add a count to the leader object
# 5. You want to add the leader to the list of grouped students
# This will assign all of the group leaders.
for i, g in enumerate(group_sizes):

    leader_ = select_leader(students)

    while leader_ in grouped_students:
        leader_ = select_leader(students)

    group_list.append(Groups(i + 1, g, [leader_], [leader_]))

    leader_._leader()

    grouped_students.append(leader_)

# Now we want to populate the groups
# We again want to iterate through the group_list
# We then want to add that many number of students to the group member list of the group.group_member object
# a very useful hint is that if you subtract two set datastructures you get all of the objects that are only in the first list
# before you end the cycle of the loop you want to make sure you add the student you added to the group to the list of grouped students.
# This way you ensure that you do not add them again.
for i, group in enumerate(group_list):
    for j in range(group.group_size - 1):
        remaining_students = set(students) - set(grouped_students)

        student_num_ = np.random.choice(list(remaining_students))

        group.group_member.append(student_num_)

        grouped_students.append(student_num_)


# In[6]:


# This is a script that prints the students in group 10
# You can use this to check your results

print(f"The group leader is {group_list[10].group_leader[0].name}")

for i, student in enumerate(group_list[10].group_member):
    if i != 0:
        print(f"The group members {i} is: {student.name}")


# In[ ]:




