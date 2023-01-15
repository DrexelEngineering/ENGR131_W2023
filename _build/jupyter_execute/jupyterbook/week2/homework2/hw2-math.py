#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Initialize Otter
import otter
grader = otter.Notebook("hw2-math.ipynb")


# #  🏡📝 Homework 2 - Using Python to Solve Math Problems
# 
# This assignment will explore using python's capabilities for mathematical calculations.
# 
# 

# **Question 1: Interest rate calculation** 
# 
# Let $r$ be a bank's interest rate in percent per year. An inital amount of money $P$, also called a principal, will mature to an amount of 
# 
# $$ P\left(1 + \frac{r}{100}\right)^{n} $$
# 
# after $n$ years have passed.
# 
# Write python code to do the following:
# 
# * Define variables: `P = 1000`, `r = 0.95`, and `n = 5`
# * Calculate the interest rate based on the equation above
# * Store the final value in a variable called `v`
# 
# 
# Note: Your code should be indented under what's called the function definition: `def question_1():`. This helps the autograder run all the code you write by calling a single name. (Functions will be taught in future weeks.). 
# 
# Note: Python cares about **Tabs** make sure the spacing is correct. If you get an `Indention Error` it likely means your spacing is not correct. 
# 
# Your solution should look like this: 
# 
# ```python
# def question ():
#     line1 = line1_code # line 1 of code
#     line2 = line2_code # line 2 of code
# 
#     return x, y, z # variables to return seperated by commas
# ```
# 
# Your code replaces the prompt:  `...`

# In[ ]:


# define a function called question_1 to be used for grading
def question_1():

    ...

    # The following line outputs these values from the function so that they can be accessed by the grader
    return P, r, n, v


# In[ ]:


grader.check("q1-interest")


# **Question 2: Musical note frequencies** 
# 
# On a piano, each key has a fundamental frequency $f$. Each higher key (black or white) has a fundamental frequency of 
# 
# $$ f * 2^{(\frac{n}{12})} $$ 
# 
# where $n$ is the distance away from the starting key. The key $A_4$, near the center of the piano keyboard, has a fundamental frequency of 440 Hz. Your task is to calculate the fundamental frequency of $D_5$, which is 5 keys higher. 
# 
# Write python code to do the following:
# 
# * Define variables: `f = 440` and `n = 5`
# * Calculate the interest rate based on the equation above
# * Store the frequency of $D_5$ in a variable called `d`
# 
# Again, your code should be indented under the function definition: `def question_2():`.
# 
# Your code replaces the prompt: `...`

# In[ ]:


# define a function called question_2 to be used for grading
def question_2():

    ...

    # output these values from the function so that they can be accessed by the grader
    return f, n, d


# In[ ]:


grader.check("q2-music")


# **Question 3: Using Python as a calculator** 
# 
# We have seen how Python can be used to evaluate mathematical expressions. This problem provides practice incorporating various mathematical functions and constants.  
# 
# 
# Write python code to do the following:
# 
# * Define variables: `a = 3`, `b = -6`, `c = 4`, and `x = 2`
# * For each of the quantities $E_0$ through $E_7$, construct a one-line Python expression that computes the value and assigns it to a variable. (You should perform your computations using the variable names $a$, $b$, and $c$ instead of their numerical values). In Python, we will use variable names `E0` through `E7` to store the values $E_0$ through $E_7$. Definitions of the variables `E0` through `E7` have been started for you in the template.
# 
# $\text{i.  } E_0 = \sqrt{a^2+b^2+c^2}$
# 
# $\text{ii.  } E_1 = \ln(3x-a)$
# 
# $\text{iii.  } E_2 = \log_{10} \left(3 \left|x\right|+\frac{c}{5} \right)$
# 
# $\text{iv.  } E_3 = \left( ax+\frac{ab}{c} \right)^{1/3}$
# 
# $\text{v.  } E_4 = \frac{x^2+1}{(ax-1)\left|b-e^x\right|}$
# 
# $\text{vi.  }  E_5 = \left( cos \left( \frac{\sqrt{a}}{3}\pi \right) \right)^2+\cos \left( \frac{\sqrt{a}}{3}\pi \right)^2$
# 
# $\text{vii.  }  E_6 = \arccos(\cos(x))$
#     
# $\text{viii.  }  E_7 = \frac{a+2c}{\sin \left( \frac{b+2c}{\sqrt{a^2+b^2+c^2}} \right) }$
# 
# 
# You should use the `NumPy` library for the required mathematical functions. You can discover the necessary functions using the [Numpy Documentation](https://numpy.org/doc/stable/reference/)
# 
# We have used the standard `NumPy` convention `import numpy as np`, thus, for example the `cos` function is used by typing `np.cos(<value>)`
# 
# Again, your code should be indented under the function definition: `def question_3():`.
# 
# Your code replaces the prompt:  `...`

# In[ ]:


# import the np library to be used
import numpy as np

# define a function called question_3 to be used for grading
def question_3():

    a = ...
    b = ...
    c = ...
    x = ...

    E0 = ...
    E1 = ...
    E2 = ...
    E3 = ...
    E4 = ...
    E5 = ...
    E6 = ...
    E7 = ...

    # output these values from the function so that they can be accessed by the grader
    return a, b, c, x, E0, E1, E2, E3, E4, E5, E6, E7


# In[ ]:


grader.check("q3-calculator")

