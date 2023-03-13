#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Initialize Otter
import otter
grader = otter.Notebook("hw8-strings.ipynb")


# # 🏡📝 Homework 8
# 
# This assignment includes three problems on the topic of strings.
# 
# 

# **Question 1: Remove non alpha characters** 
# 
# In this lab you will write a function which takes in a string and removes all of the non-alphabetic characters from it.
# 
# Write python code to do the following:
# 
# * Define a function called `remove_non_alpha` that takes an input string `s`
# * Loop through each character in the string, adding it to an output string if it is an alphabetic character.
# * Return the final string.
# 
# 
# Your code replaces the prompt:  `...`
# 

# In[ ]:


...


# In[ ]:


grader.check("q1-nonalpha")


# **Question 2: Palindrome Detector** 
# 
# A palindrome is a word or a phrase that is the same when read both forward and backward. Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). Write a program whose input is a word or phrase, and that outputs true if the input is a palindrome, otherwise false. In determining if a string is a palindrome, you should treat upper vs. lower case versions of characters as the same letter, and you may ignore all spaces. 
# 
# Write python code to do the following:
# 
# * Define a function called is_palindrome that takes in one input parameter `x`.
# * Convert the string `x` to be all lower case.
# * Remove all spaces from string `x`. (Hint: use the string.`replace` method)
# * Loop through the characters of `x` to determine if it is palindromic
# 
# Your code replaces the prompt:  `...`

# In[ ]:


...


# In[ ]:


grader.check("q2-palindrome")


# **Question 3: Count characters** 
# 
# Your task is to write a function that takes in a character and a string and retruns the count of how many times that character appears in the string.
# 
# Write python code to do the following:
# 
# * Define a function called ``count_characters`` which takes two arguments, a character `c`, and a string `s`
# * Your function should loop through the string and character by character, counting every time the character `c` is encountered
# * Return the total count, or `0` if the character `c` is not part of string `s`
# 
# 
# Your code replaces the prompt:  `...`
# 

# In[ ]:


...


# In[ ]:


grader.check("q3-countchars")

