#!/usr/bin/env python
# coding: utf-8

# # 📝Classes
# 

# - Classes provide a mechanism to bundle data and functionality together
# 

# - Classes allow you to create new objects that are instances of that type
# 

# - You can modify internal working or objects within a class to change its function
# 

# ## Class Syntax
# 

# The simplest form of a class looks like
# 

# ```python
# class ClassName:
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>
# ```
# 

# - When a class is defined it creates a new namespace, local variable in this namespace only exist here.
# 

# ## Class as an Object
# 
# ### Attributions
# 
# - Within a class you can define variables within the namespace
# - This is a very useful tool to create many objects of the same type with different values
# 

# In[ ]:


class MyClass:
    """A simple example class"""

    i = 12345

    def f():
        return "hello world"


# - Here we defined a `class` MyClass and assigned two attributes f and i.
# 

# In[ ]:


MyClass.i


# In[ ]:


MyClass.f()


# Within Python, there are some built in method - for example:
# 

# In[ ]:


MyClass.__doc__


# ## Instantiation
# 
# - Instantiation is the process of calling a class as a function to assign a new object of that class to a variable
# 

# In[ ]:


class MyClass:
    """A simple example class"""

    i = 12345

    def f(self):
        return "hello world"


# In[ ]:


x = MyClass()


# Once we instantiate a class we can call it
# 

# In[ ]:


x.f()


# Notice that we included an input `self`. When a class is instantiated, the first input to the function is always the object for the class itself. Convention is to call this `self`.
# 

# ## The `__init__` Function
# 
# When you instantiate a class, the `__init__` method is called. This allows you to define variables specific to the object you are creating.
# 

# In mathematics, number can be complex, which means that they have a real and an imaginary component. If you wanted to conduct mathematical operations on this different number, it would be useful to define a `class` `complex_number` that could serve as standard DataType.
# 

# In[ ]:


class Complex:
    def __init__(self, realpart, imagpart):

        self.r = realpart
        self.i = imagpart


# In[ ]:


a = Complex(2, 3)


# In[ ]:


a.r


# In[ ]:


a.i


# # Functions that Work on Class Objects
# 
# When you have a well-defined class, you can use them efficiently in functions. For example, let's say we wanted to build a function `add` that adds complex numbers. This is done by adding the real and imaginary components.
# 

# In[ ]:


def add(*args):
    r = 0
    i = 0
    for arg in args:
        r += arg.r
        i += arg.i
    return Complex(r, i)


# In[ ]:


a = Complex(2, 3)

b = Complex(5, 2)

new_complex = add(a, b, b, b)


# In[ ]:


print(new_complex.r, new_complex.i)


# That is quite a useful function. You defined a new DataType and an operator for that DataType. This is very similar to how Python is constructed on the backend.
# 

# ## Adding Methods to a Class
# 
# Within a class, you can add method. For example, we could add a method `add` that adds complex numbers within the object and updates itself.
# 

# In[ ]:


class Complex:
    def __init__(self, realpart, imagpart):

        self.r = realpart
        self.i = imagpart

    def add(self, *args):
        for arg in args:
            self.r += arg.r
            self.i += arg.i

    def __str__(self) -> str:
        return f"this object is a complex number with a real value of {self.r} and an imaginary value of {self.i}"


# In[ ]:


a = Complex(2, 3)

a.add(b)


# We used the magic method to define what the object does when we call it as a string
# 

# In[ ]:


a.__str__()


# In[ ]:


print(a)


# In[ ]:




