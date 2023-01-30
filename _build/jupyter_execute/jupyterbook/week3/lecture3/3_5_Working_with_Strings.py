#!/usr/bin/env python
# coding: utf-8

# # 📝 Working with Strings

# In[1]:


from friendly import *
from friendly.jupyter import friendly_tb


# A lot of times you want to relay information to a user or send new instructions to a program. One common method to perform these tasks in Python is to use strings. 

# ## Defining Strings 

# Recall that to represent a string you wrap it in quotes:
# * Single quotes `'` allows you to embed double quotes `"`
# * Double quotes `'` allows you to embed single quotes `'`
# * Triple quotes `"""` allows you to embed single and double quotes, and the string can span multiple lines 

# In[2]:


single_quote = 'Single quote allow you to embed "double" quotes in your string.'
double_quote = "Double quote allow you to embed 'single' quotes in your string."
triple_quote = """Triple quotes allows to embed "double quotes" as well as 'single quotes' in your string. 
And can also span across multiple lines."""


# Strings are immutable which means you cannot replace a value in a string. You need to create a new string.

# <div class="admonition note alert alert-info">
# <p class="first admonition-title" style="font-weight: bold;">Definition</p>
# Immutable object -  an object whose state cannot be modified after it is created
# </div>

# In[3]:


triple_quote = """This is triple quoted string using "single" quotes."""
triple_quote[35] = "'"


# ## Formatting within a string
# 
# You can add tabs to a string using `\t`

# In[3]:


string = "Drexel \t Engineering"

print(string)


# You can add a line break with `\n`

# In[4]:


string = "Drexel \nEngineering"

print(string)


# <div class="admonition note alert alert-info">
# <p class="first admonition-title" style="font-weight: bold;">Note</p>Did you notice the '\t', '\n' above? These are called escape characters. They start with a \ (backslash). 
# Internally, they are not interpreted as normal strings, but rather as special characters that represent something else. For example - '\t' represents a tab. There are many more escape characters.
#  </a>
# </div>

# ## Length of a String

# You can find the length of a string using the built-in `len()` function:

# In[5]:


len(triple_quote)


# ## String Slicing

# * Since strings are a sequence of characters, you can access it through slicing and indexing just like you would with Python lists or tuples. 
# * Strings are indexed with respect to each character in the string and the indexing begins at 0

# ![](images/String_Index.png)

# In[6]:


snack = "Chocolate Cookie."


# * The first index starts at 0

# In[7]:


print(snack[0])


# * The last index is the period at 16

# In[8]:


print(snack[16])


# * You can access the end of a string using [-1] index

# In[9]:


print(snack[-1])


# ## Extracting a Substring

# You can extract a substring using range slicing `[Start index (included): Stop index (excluded)]`

# In[10]:


print(snack[10:16])


# You can also use a combination of positive and negative slicing

# In[11]:


print(snack[10:-1])


# If you do not specify a start or end index it will use the entire array

# In[12]:


# Stop value not provided
print(snack[0:])

# Start value not provided (Stop value excluded according to syntax)
print(snack[:-1])

# This is also allowed
print(snack[:])


# ### Using a Stride
# 
# It is possible to use a 3rd parameter stride to specify how many characters you would like to move forward.

# In[13]:


mixed_string = "D0r0e0x0e0l0 0E0n0g0i0n0e0e0r0i0n0g"
print(mixed_string[::2])


# ### Reversing a String

# Strides can be used to reverse a string

# In[14]:


ordered_string = "ABCDEFG"
print(ordered_string[::-1])


# ## Concatenation of String
# 
# There are many times where you might want to join or concatenate strings. In python this can be done using the simple addition operator. 

# In[15]:


string1 = "Drexel"
string2 = "Engineering"

alma_mater = string1 + " " + string2
print(alma_mater)


# This will only work if all the datatypes are strings

# In[17]:


string1 = "Drexel"
string2 = "Engineering"
string3 = "Class of"
year = 2027

alma_mater = string1 + " " + string2 + " " + string3 + " " + year
print(alma_mater)


# In[16]:


string1 = "Drexel"
string2 = "Engineering"
string3 = "Class of"
year = 2027

alma_mater = string1 + " " + string2 + " " + string3 + " " + str(year)
print(alma_mater)


# ## Repeating Strings
# 
# The multiply operator allows you to repeat strings

# In[17]:


single_word = "hip "
line1 = single_word * 2 + "hurray! "
print(line1 * 3)


# ## Built-in String Methods

# Python provides many built-in methods or helper functions to manipulate strings. 

# ### Capitalize a String

# In[18]:


string = "drexel engineering"

print(string.capitalize())


# ### Checks if lower case

# In[19]:


string = "drexel engineering"

print(string.islower())


# ### Finds Substring
# 
# Returns the lowest index in the string where the substring is found.

# In[20]:


print(string.find("eng"))


# ### Count Occurrence
# 
# Counts how many times a substring occurs.

# In[21]:


string = "drexel engineering " * 4

print("initial string: " + string)

print(string.count("eng"))


# ## Replace Values
# 
# `str.replace(substring, new)`: replaces all occurrences of the substring in string with new. You can also define a third argument max, which replaces at most max occurrences of substring in the string. 

# In[22]:


string1 = "hip hip hurray! hip hip hurray! hip hip hurray!"
string2 = string1.replace("hip", "Hip")
print(string1)
print(string2)

print("\nIDs")
print(id(string1))
print(id(string2))


# You can see that the IDs for the string change. This is because they are immutable. 

# ## Splitting Strings
# 
# `str.split(sep="")`: splits the string according to the delimiter (space if not provided) and returns a list of substrings.

# In[23]:


string2.split(sep=" ")


# ## Formatting Strings
# 
# Sometimes you might want to substitute a variable into a string. 
# 
# ### Python Version 3.6 Formatter

# In[24]:


print(
    "{0} scored {1} points for the Drexel Dragons!".format("Coletrane Washington", 24)
)  # Accessing values by position


# In[25]:


print(
    "{player_name} scored {points} points for the Drexel Dragons!".format(
        player_name="Coletrane Washington", points=24
    )
)


# ### Python Version >3.6 F-strings
# 
# f-string is a string literal that is prefixed with `f` or `F`. You can define identifiers to be used in your string within curly braces { }.
# 
# We recommend using F-strings because their beautiful practicality and simplicity.

# In[26]:


player_name = "Coletrane Washington"
points = 24

print(f"{player_name} scored {points} points for the Drexel Dragons!")

