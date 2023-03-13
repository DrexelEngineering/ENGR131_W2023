#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Initialize Otter
import otter
grader = otter.Notebook("hw6-loops.ipynb")


# # 🏡📝 Homework 6
# 
# This assignment includes three problems on the topic of loops.
# 
# 

# **Question 1: Fibonacci Sequence** 
# 
# Fibonacci was born sometime around 1170 in the Kingdom of Pisa in what is now Italy. The sequences we now refer to as Fibonacci sequences first appeared in his treatise *Liber Abaci* from 1202 as a model of how rabbit populations grow.
# 
# A Fibonacci sequence is a list of integers in which the $n\text{th}$ entry $x_n$ is computed from:
# 
# $$ x_n = x_{n-1} + x_{n-2} $$
# 
# To initiate a Fibbonaci sequence, one must provide values for $x_0$ and $x_1$. 
# 
# For example, if $x_0 = 0$ and $x_1 = 1$, the first 10 terms of the sequence are:
# 
# $$ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 $$
# 
# Your task is to implement a function that takes in two starting values and a length and returns the resulting Fibonacci sequence.
# 
# 
# Write python code to do the following:
# 
# * Define a function called `fibonacci` which accepts 3 input arguments: two starting values `x0` and `x1`, and a sequence length `L`
# * Your function should return a list containing the first `L` fibonacci numbers starting with `x0` and `x1`
# * You may assume the value `L >= 2`
# 
# Your code replaces the prompt:  `...`

# In[ ]:


...


# In[ ]:


grader.check("q1-fibonacci")


# **Question 2: Brute-Force Equation Solver** 
# 
# Numerous engineering and scientific applications require finding solutions to a set of equations. For example, the following system of equations:
# 
# $$ 8x + 7y = 38 $$  
# $$3x - 5y = -1 $$ 
# 
# have a solution: $ x = 3$, $y = 2$. 
# 
# You will implement a function that acts as a simple equation solver. For systems of equations of the form:
# 
# $$ ax + by = c $$  
# $$ dx + ey = f $$ 
# 
# You will use the following brute-force algorithm to find an integer solution for x and y in the range $[-10, 10]$ (if such a solution exists):
# 
For every value of x from -10 to 10 (inclusive)
   For every value of y from -10 to 10 (inclusive)
      Check if the current x and y satisfy both equations. If so, return the solution, and finish.
If no solution was found, return the string "no solution found".
# Notes:
# - You may assume that if a solution exists, there is only one solution. Your function should return the first solution found using the algorithm outlined above
# - Elegant mathematical techniques exist to solve such linear equations. However, for other kinds of equations or situations, brute-force approaches can be handy.
# 
# Write python code to do the following:
# 
# * Define a function called ``eq_solver`` which accepts 6 input arguments, `a`, `b`, `c`, `d`, `e`, and `f` the coefficients for two equations
# * Your function should return a tuple of integers, containing solution values for ($x$,$y$)
# * If no solution was found, your function should return a string: `"no solution found"`
# 
# 
# Your code replaces the prompt:  `...`

# In[ ]:


...


# In[ ]:


grader.check("q2-equation-solver")


# **Question 3: Convert to Binary** 
# 
# A natural number's binary representation tell which powers of $2$ sum to produce the number. 
# 
# For instance: 
# $6$ in binary is $110$, since: $$ 6 = (1)2^2 + (1)2^1 + (0)2^0 $$
# 
# ($110$ are the coefficients of the descending powers of $2$.)
# 
# Your task is to write a function that takes in a positive integer and returns a string containing its binary representation. The following algorithm can be used to generate a natural number's binary representation:
As long as x is greater than 0
   Add x modulo 2 as the leftmost bit
   Assign x with x divided by 2 (integer division)
# Reminders:
# - "x modulo 2", written in python as `x % 2`, returns the remainder when dividing by two, either 0 or 1
# - Integer division written in python as, `x // 2`, truncates any remainder. 
#     - For example `5 // 2 = 2` since the remainder is truncated
# - Use `str()` to convert a number to a string
# 
# Write python code to do the following:
# 
# * Define a function called `to_binary` that takes an input positive integer `x`
# * Using the algorithm described in pseudocode above, compute the binary representation of `x`
# * Return the binary as a string of `"1"`s and `"0"`s
# 
# 
# Your code replaces the prompt:  `...`

# In[ ]:


...


# In[ ]:


grader.check("q3-binary")

