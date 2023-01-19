#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Initialize Otter
import otter
grader = otter.Notebook("hw3-types.ipynb")


# # 🏡📝 Homework 3 - Using Different Types of Variables
# 
# This assignment includes three quesitons on the topic of data types.
# 
# 

# **Question 1: Creating a Password** 
# 
# In this problem you will implement a function that generates a password for a user based on their favorite color, pet's name and an integer number.
# 
# If their favorite color is yellow, their pet is called Daisy, and their favorite number is 6, the suggested password should be: `"yellow_Daisy_6"`.
# 
# Write python code to do the following:
# 
# * Inside the provided `create_password` function, combine the variables `fav_color`,`pet_name`, and `number` to make a password in the proper format specified above.  
# * Store the the final string in a variable called `password`.
# 
# Your code replaces the prompt:  `...`

# In[ ]:


# This line creates a function called create_password which has 3 arguments: fav_color, pet_name, and number
def create_password(fav_color, pet_name, number):
    ...
    # This line outputs from the function the password that you generated
    return password

# this line runs the function and prints its output
print(create_password("yellow", "Daisy", 6))


# In[ ]:


grader.check("q1-password")


# **Question 2: Caffeine Levels** 
# 
# A half-life is the amount of time it takes for a substance or entity to fall to half its original value. Caffeine has a half-life of about 6 hours in humans. The amount of caffeine left after $h$ hours, $C_h$, is approximated using the following equation:
# 
# $$C_h = C_0 \left( \frac{1}{2} \right) ^{ h/6 }$$
# 
# Where $C_0$ is the initial amount of caffeine. 
# 
# You will write code that generates a brief report of the caffeine level for a given intial amount of caffeine (in mg) after a given amount amount of time (in hours). If the initial caffeine amount is 100 mg, and the given time passed is 12 hours, the report should be:
# 
# `"After 12.00 hours: 25.00 mg"`
# 
# Notice that both values should be reported with two digits after the decimal point. You should use a string formatting expression to do this.
# 
# Example: if you have a variable `x = 5`, we can get the string `"5.00"` with the following expression:
# `f"{x:.2f}"`
# 
# Write python code to do the following:
# 
# * Inside the provided `caffeine_levels` function, calculate the final caffeine level based on the starting amount `amt` and the hours passed `hours`.  
# * Generate the report string and store it in a variable called `report`.
# 
# Your code replaces the prompt: `...`

# In[ ]:


# This line creates a function called caffeine_levels which has 2 arguments: amt and hours
def caffeine_levels(amt, hours):
    ...
    # this line outputs the report from the function
    return report

# this line runs the function and prints its output
print(caffeine_levels(100, 12))


# In[ ]:


caffeine_levels(100, 12)


# In[ ]:


grader.check("q2-caffeine")


# **Question 3: Phone Number Parsing** 
# 
# This problem involves parsing a phone number. Parsing means to evaluate a collection of symbols. Parsing is an important task in many computer applications.
# 
# You will write a program that takes a string containing a formatted phone number and parses it into a single integer. The format we will use for phone numbers is `"XXX-XXX-XXXX"` where `X` is an integer in $[0,9]$.
# 
# For example, a given phone number string `"123-456-7890"` should result in the integer `1234567890`.
# 
# Hint: use slicing to extract part of a string. If `S` = `"123-456-7890"`, we can use `S[0:3]` to slice just the first 3 characters of the string, producing `"123"`.
# 
# 
# Write python code to do the following:
# 
# * Inside the provided `parse_phone_number` function, parse the formatted phone number string `S` to produce an integer 
# * Store the resulting integer in a variable called `parsed`.
# 
# Your code replaces the prompt: `...`

# In[ ]:


# This line creates a function called parse_phone_number which has 1 argument: S
def parse_phone_number(S):
    ...
    # this line outputs the parsed number from the function
    return parsed

# this line runs the function and prints its output
print(parse_phone_number("123-456-7890"))


# In[ ]:


grader.check("q3-phone-parsing")

