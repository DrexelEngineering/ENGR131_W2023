#!/usr/bin/env python
# coding: utf-8

# # 📝Week 9 - Lab Intro
# 
# In this lab introduction we will briefly review and discuss classes. We will also go over some of the math involved in triangulation, which will be useful for this week's lab.

# ## Classes

# ### Creating a class
# 
# You can use the keyword `class` to create a class. 

# In[ ]:


class MyClass:
    # contents of the class go indented here
    ...


# Classes can contain various attributes, including variables and functions.

# In[ ]:


class MyClass:
    
    myVar = 9

    def myFunc():
        print("Hello World")


# We can access these by doing the following:

# In[ ]:


MyClass.myFunc()
MyClass.myVar


# ### Creating objects from classes
# 
# You can create objects belonging to a class. First, we must discuss the `__init__` method.
# 
# #### The `__init__` method
# 
# The `__init__` method is a function that is used to handle the creation of new objects. The first input argument `self` is used to refer to the object being created. We can use `self.<variable name>` to create a variable specific to each object. 

# In[ ]:


class Student:

    # the first input argument to init refers to the object being created
    # by convention it is always called "self"
    def __init__(self, fname, lname):
        # self.fname is a variable 
        self.fname = fname
        # self.lname is a variable 
        self.lname = lname


# To create a new object of class `Student`, we can do the following.

# In[ ]:


# The two strings are passed as the second and third input arguments to the __init__ method
s1 = Student("John", "Foo")


# We can create a different object belonging to the same class

# In[ ]:


s2 = Student("Jane", "Bar")


# Each `Student` object has its own first and last name variables.

# In[ ]:


print(s1.fname)
print(s1.lname)

print(s2.fname)
print(s2.lname)


# #### Adding methods
# 
# A method is defined just like a function where the first argument is `self`, referring to the current object. (Just like with `__init__`, the first argument of all methods is called `self` by convention.)
# 
# Below we define a method called `print_full_name` which prints the student's full name.

# In[ ]:


class Student:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_full_name(self):
        print(f"{self.fname} {self.lname}")


# When calling a method, the object itself is always passed in as the first argument. This is why there is nothing in the parentheses of the method calls below.

# In[ ]:


s1 = Student("John", "Foo")
s2 = Student("Jane", "Bar")

s1.print_full_name()
s2.print_full_name()


# ## Triangulation
# 
# We will now discuss the introduction to today's lab.
