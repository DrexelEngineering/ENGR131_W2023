#!/usr/bin/env python
# coding: utf-8

# # 📝Week 6 - Lab Intro
# 
# In this lab introduction we will briefly discuss the topic of looping, which is the focus of the assigned homework.

# ## Looping

# ### `for` loops
# `for` loops let you run the same block of code for a predetermined number of iterations.
# 
# *syntax:* `for [variable name] in [iterable]`

# In[ ]:


for i in range(10):
    print(i)


# #### the `range` function

# The `range()` function creates an iterable over integers. It can have up to three arguments (start, stop, step).

# In[ ]:


# loop from 2 up to (not including) 20, stepping by 3
for i in range(2,20,3):
    print(i)


# with 2 arguments: (start, stop, 1)

# In[ ]:


# loop from 6 up to (not including) 10
for i in range(6,10):
    print(i)


# As before, with 1 argument: (0, stop, 1)

# In[ ]:


# loop from 0 up to (not including) 5
for i in range(5):
    print(i)


# #### looping over a list

# In[ ]:


days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for d in days:
    print(d)


# #### looping over a string

# In[ ]:


message = "Hello World!"

for letter in message:
    print(letter)


# #### looping over a dictionary

# A `for` loop over a dictionary iterates over the keys.

# In[ ]:


fruit_inventory = {"apple" : 6,
        "banana" : 2,
        "orange" : 4}

for f in fruit_inventory:
    print(f)


#  If we want the values as well, we can use `[dict_name].items()`.

# In[ ]:


fruit_inventory = {"apple" : 6,
                "banana" : 2,
                "orange" : 4}

for f in fruit_inventory.items():
    print(f)


# To separate each (key, value) tuple, we can provide to variables to the for loop. 

# In[ ]:


fruit_inventory = {"apple" : 6,
                "banana" : 2,
                "orange" : 4}

for fruit_name, quantity in fruit_inventory.items():
    print(f"There are {quantity} {fruit_name}s in stock.")


# #### the `enumerate` function
# 
# We can use the enumerate function to loop over an iterable with (index, object) pairs. 

# In[ ]:


days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for d in enumerate(days):
    print(d)


# We can use two variables to "unpack" the tuple.

# In[ ]:


days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for i, d in enumerate(days):
    print(f"{d} is day #{i+1}.")


# ### `while` loops
# `while` loops keep iterating while some condition is `True`.
# 
# *syntax:* `while [condition]`

# In[ ]:


i = 0
while i < 10:
    print(i)
    i += 1


# Notice that this is the same as the `for` loop we saw previously:

# In[ ]:


for i in range(10):
    print(i)


# Make sure the `while` loop condition will eventually become `False`. You don't want to loop forever!
# 
# **Run this at your peril:**

# In[ ]:


# loops forever

i = 0
while i < 10:
    print(i)


# If you already know how many times the loop needs to run, it is easier/cleaner to use a `for` loop.
# 
# Here's an example where `while` is required.

# In[ ]:


input_string = input("Please enter your favorite number:")
while not input_string.isnumeric():
    input_string = input("Not a number. Try again:")


print(f"{input_string} is your favorite number.")  


# We need a `while` loop (rather than a `for` loop) because we don't know how many times the user will mess up and enter a non-number.

# ### `break` and `continue`

# #### `break` statements
# The keyword `break` causes a loop to immediately terminate.

# In[ ]:


days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for d in days:
    if len(d) > 6:
        break
    print(d)


# #### `continue` statements
# 
# The keyword `continue` causes a loop to immediately terminate the current iteration, and move to the next one.

# In[ ]:


days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for d in days:
    if len(d) > 6:
        continue
    print(d)


# ### nested loops
# 
# Loops can be nested. The following example uses nested `for` loops to count in binary from 0 to 7.

# In[ ]:


for i in range(2):
    for j in range(2):
        for k in range(2):
            print(f"{i}{j}{k}")

