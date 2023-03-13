#!/usr/bin/env python
# coding: utf-8

# # 📝 Inheritance
# 
# - Inheritance allows one class to inherit properties from another class.
# 

# - It is usually referred to as child and parent classes.
# 

# - It allows you to better represent real-world relationships.
# 

# - Code can become much more reusable.
# 

# - It is transitive meaning that if Class B inherits from Class A then subclasses of Class B would also inherit from Class A.
# 

# #### Inheritance Example
# 

# ```{admonition} Syntax
# Class BaseClass:
#     {Body}
# Class DerivedClass(BaseClass):
#     {Body}
# ```
# 

# ##### Step 1: Create a parent class with a method
# 
# - Create a parent class named `Person` that defines a `name` and `age`
# - Add a Class method that prints the name and title
# 

# In[ ]:


class Person:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.age)


# ##### Testing
# 

# In[ ]:


jedi = Person("Darth Vader", 56)
jedi.Display()


# #### Step 2: Creating a Child Class;
# 
# - Create a child class of `Person`, `Jedi` that has a method `Print` that prints `Jedi's use the force`
# 

# In[ ]:


class Jedi(Person):
    def Print(self):
        print("Jedi's use the force")


# ##### Testing
# 

# In[ ]:


# instantiate the parent class
jedi_info = Jedi("Darth Vader", 56)

# calls the parent class
jedi_info.Display()

# calls the child class
jedi_info.Print()


# ##### Step 3: Adding Inheritance
# 
# - Starting with the base Class `Person` we can add a method to `getName` that returns the `name`
# - We can add a method `isAlliance` that establishes if the person is part of the Rebel Alliance, the default should be `False`
# - We can add a inherited child class `Alliance` that changes `isAlliance` to `True`
# 

# In[ ]:


class Person:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Function that gets the name
    def getName(self):
        return self.name

    # Function that returns if the person is part of the alliance
    def isAlliance(self):
        return False


# Inherited child class
class Alliance(Person):

    # This will change the isAlliance class to True
    def isAlliance(self):
        return True


# ##### Test
# 

# In[ ]:


darth_vader = Person("Darth Vader", 56)
print(darth_vader.getName(), darth_vader.isAlliance())

luke_skywalker = Alliance("Luke Skywalker", 21)
print(luke_skywalker.getName(), luke_skywalker.isAlliance())

