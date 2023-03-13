#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Initialize Otter
import otter
grader = otter.Notebook("hw5-branching.ipynb")


# # 🏡📝 Homework 5
# 
# This assignment includes three problems on the topic of branching.
# 
# 

# **Question 1: Grade Calculator** 
# 
# Your task is to write a function accepts an integer score and returns a string of the letter grade that score corresponds to. The mapping of score ranges to letter grades is:
# 
# <center>
# 
# | Score | Letter Grade |
# | --- | --- |
# | 95-100 | A+ |
# | 90-94 | A |
# | 80-89 | B+ |
# | 70-79 | B |
# | 60-69 | C+ |
# | 50-59 | C |
# | 0-49 | F |
# 
# </center>
# 
# 
# 
# 
# (Important note: This is just an example, not the letter grade mapping for this course.)
# 
# 
# Write python code to do the following:
# 
# * Define a function called `letter_grade` which accepts one input argument, an integer score `s`
# * Implement your function so that it returns the proper letter grade for an input score
# * You may assume the input `s` is an integer, but if `s` is outside the bounds $[0, 100]$, your function should return the message: `"invalid score"` 
# 
# 
# Your code replaces the prompt:  `...`

# In[ ]:


...


# In[ ]:


grader.check("q1-grade-calculator")


# **Question 2: Leap Year** 
# 
# A year in the modern Gregorian Calendar consists of 365 days. In reality, the earth takes longer to rotate around the sun. To account for the difference in time, every 4 years, a leap year takes place. A leap year is when a year has 366 days: An extra day, February 29th. The requirements for a given year to be a leap year are:
# 
# 1) The year must be divisible by 4
# 2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400
# 
# Some examples:
# - 1600, 1712, and 2016 are all leap years
# - 2002 is not a leap year (not divisible by 4)
# - 1900 is not a leap year (1900 is a century year not divisible by 400)
# 
# Your task is to code a function that identifies whether or not a year is a leap year.
# 
# Write python code to do the following:
# 
# * Define a function called ``is_leap_year`` which accepts one input argument, an integer year `y`
# * Implement your function so that it returns `True` if the the year `y` is a leap year and otherwise returns `False`
# 
# 
# Your code replaces the prompt:  `...`
# 
# 

# In[ ]:


...


# In[ ]:


grader.check("q2-leap-year")


# **Question 3: Seasons** 
# 
# The date ranges for the seasons are as follows:
# 
# <center>
# 
# | Season | Date Range |
# | --- | --- |
# | `spring` | March 20 - June 20 |
# | `summer` | June 21 - September 21 |
# | `autumn` | September 22 - December 20 |
# | `winter` | December 21 - March 19 |
# 
# </center>
# 
# Your task is to write a function that takes in a date and returns the season that the date falls in.
# 
# Write python code to do the following:
# 
# * Define a function called `get_season` that takes as input arguments a string `m` and an integer `d`
# * The function should determine the season the date given by month `m` and day `d` 
#     * For example, if `m = "march"` and `d = 27`, the function should return "`spring`"
# * You must check that `m` and `d` form a valid date. If not, return "`invalid`"
# 
# You may assume the month `m` is in all lowercase
# 
# 
# Your code replaces the prompt:  `...`

# In[ ]:


...


# In[ ]:


grader.check("q3-seasons")


# 
