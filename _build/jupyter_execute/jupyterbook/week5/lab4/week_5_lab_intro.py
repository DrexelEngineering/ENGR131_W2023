#!/usr/bin/env python
# coding: utf-8

# # 📝Week 5 - Lab Intro
# 
# In this lab introduction we will briefly discuss the topic of branching, which is the focus of today's lab and the assigned homework.

# ## Branching

# #### `if` statements
# `if` statements let you run certain code only if some condition is met. The code inside the `if` statement is indented.

# In[ ]:


score = 50

if score > 80:
    print(f"{score} is a good score.")
print("End of score report.")


# #### `else` statements
# You can use the keyword `else` if you want code to run only if the previous condition was *not* met. You cannot provide `else` with a condition.

# In[ ]:


score = 50

if score > 80:
    print(f"{score} is a good score.")
else:
    print(f"{score} is a bad score.")

print("End of score report.")


# #### Multiple `if` statements
# You can have multiple `if` statements in a row. It's possible more than one are true.

# In[ ]:


score = 90

if score > 80:
    print(f"{score} is a good score.")
if score > 70:
    print(f"{score} is a decent score.")

print("End of score report.")


# If you have multiple `if` statements, the else only applies to the last `if` statement.

# In[ ]:


score = 75

if score > 70:
    print(f"{score} is a decent score.")
if score > 80:
    print(f"{score} is a good score.")
else:
    print(f"{score} is a bad score.")

print("End of score report.")


# The examples so far show that using multiple `if` statements in a row isn't always what you want. Sometimes multiple `if`s are useful, when you want to check for multiple conditions and any or all of them can be true. Here's an example.  

# In[ ]:


number = 12

if number % 2 == 0:
    print(f"{number} is divisible by 2.")
if number % 3 == 0:
    print(f"{number} is divisible by 3.")
if number % 4 == 0:
    print(f"{number} is divisible by 4.")
if number % 5 == 0:
    print(f"{number} is divisible by 5.")
if number % 6 == 0:
    print(f"{number} is divisible by 6.")


# #### `elif` statements
# The `elif` keyword is used to mean "else if". They are useful when you have multiple conditions you want to check for, but you only ever want one condtion to be true at a time.
# 
# When you want to have multiple mutually exclusive conditions, your best choice is to use the `if` - `elif` - `else` structure. It always starts with an `if`, ends with an `else`, and the remaining statements in between are all `elif` statements. For example:
# 

# In[ ]:


score = 93

if score > 90:
    print(f"{score} is an excellent score.")
elif score > 80:
    print(f"{score} is an good score.")
elif score > 70:
    print(f"{score} is a decent score.")
else:
    print(f"{score} is a bad score.")

print("End of score report.") 


# #### Nested conditions
# 
# It is possible to have nested conditions, for example an `if` statement inside an `if` block. For example:

# In[ ]:


score = 55

if score >= 0:
    if score <= 100:
        print(f"{score} is a valid percentage.") 


# This is equivalent to:

# In[ ]:


score = 55

if score >= 0 and score <= 100:
    print(f"{score} is a valid percentage.")


# Here's an example where nesting is useful. The outermost statements check whether the score is a valid percentage. If it is, then the inner statements are used to further determine the quality of the score.

# In[ ]:


score = int(input())

if score >= 0 and score <= 100:
    if score > 90:
        print(f"{score} is an excellent score.")
    elif score > 80:
        print(f"{score} is an good score.")
    elif score > 70:
        print(f"{score} is a decent score.")
    else:
        print(f"{score} is a bad score.")

else:
    print("Invalid percentage.")

