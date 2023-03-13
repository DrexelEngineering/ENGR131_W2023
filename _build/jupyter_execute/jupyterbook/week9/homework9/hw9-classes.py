#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Initialize Otter
import otter
grader = otter.Notebook("hw9-classes.ipynb")


# # Homework 9
# 
# This assignment includes three problems on the topic of classes.
# 
# 

# **Question 1: Nutritional Information** 
# 
# Your task is to write a class called `FoodItem`. The class constructor should initialize a new food item given a name and amounts of fat, carbs, and protein (in grams). The class should also have a method called `get_calories` which returns the estimated amount of calories in a serving of the food item.
# 
# To estimate calories $x$ given the grams of fat $f$, carbs $c$, and protein $p$, you should use the following approximation:
# 
# $$x = 9f + 4c + 4p$$
# 
# 
# Write python code to do the following:
# 
# * Define a class called `FoodItem`.
# * Define the class constructor to accept as arguments a string `name` and floats `fat`, `carbs`, and `protein`. The values from these argument should be stored as data members, so that they can be used in other methods. 
# * Define a method within `FoodItem` called `get_calories`, which accepts no arguments (other than `self`) and returns the estimated calories, as a float.
# 
# Your code replaces the prompt:  `...`

# In[ ]:


...


# This creates a FoodItem object so you can test your class
snack = FoodItem("M&Ms", 10.0, 34.0, 2.0)
# This calls the get_calories method on the newly created FoodItem object
print(snack.get_calories())


# In[ ]:


grader.check("q1-nutrition")


# **Question 2: Area and Perimeter of a Circle** 
# 
# Your task is to write a class called `Circle`. The class constructor should take as input a radius that defaults to a value of `1.0`. The class should have methods called `area` and `perimeter` which return as floats the area and perimeter of the circle, respectively.
# 
# Be sure to reference `math.pi` in your calculations.
# 
# 
# Write python code to do the following:
# 
# * Define a class called `Circle`.
# * Define the class constructor to accept as argument a float `radius` with a default value of `1.0`. This value should be stored as a data member, so that it can be used in other methods. 
# * Define a method within `Circle` called `area`, which accepts no arguments (other than `self`) and returns the area, as a float.
# * Define a method within `Circle` called `perimeter`, which accepts no arguments (other than `self`) and returns the perimeter, as a float.
# 
# Your code replaces the prompt:  `...`
# 

# In[ ]:


...


# This creates a Circle object so you can test your class
c = Circle(8.0)
# These call the area and perimeter methods on the newly created Circle object
print(c.area())
print(c.perimeter())


# In[ ]:


grader.check("q2-area-perimeter-circle")


# **Question 3: 3D Point Class** 
# 
# Your task is to create a class called Point3D that implements a point in 3-D space. Objects of this class are constructed with three arguments `x`,`y`,and `z`, which all default to zero.
# 
# Inside the class you will implement a number of "magic" methods in python, the methods with names surrounded by double underscores. Specifically, you will implement the proper methods to allow addition, subtraction and equality checking between two Point3D instances. You will also implement the proper method to control how a Point3D object is printed.
# 
# Specifics regarding how these should be implemented follow.
# 
# Write python code to do the following:
# 
# * Define a class called `Point3D`.
# * Define the class constructor to accept as arguments 3 numbers `x`, `y`, and `z` which all default to `0`. These values should be stored as data members (called `x`, `y`, and `z`), so that they can be used in the other methods. 
# * Addition: define a method such that, given Point3D objects `a` and `b`, `a + b` returns a new Point3D object whose `x`, `y`, and `z` values are the sums of the `x`, `y` and `z` values of points `a` and `b`. (Hint: the built in function for addition is `__add__()`)
# * Subtraction: define a method such that, given Point3D objects `a` and `b`, `a - b` returns a float representing the Euclidean distance between points `a` and `b`.
# * Equality: define a method such that, given Point3D objects `a` and `b`, `a == b` returns True if and only if the `x`, `y` and `z` values of point `a` and `b` are equal.
# * Printing: define a method such that, given a Point3D object `a`, `print(a)` prints in the format `<a.x, b.y, c.z>`. (Hint: the built in `print` function will call the `__str__()` method on the input to convert the input into a string before printing.)

# After your class has been implemented, it should be able to be used as follows:
p1=Point3D(1,1,1)
p2=Point3D(2,2,2)
print(p1 + p2)
[output]: <3, 3, 3>

print(p1-p2)
[output]: 1.7320508075688772

p1==p2
[output]: False

p1+p1==p2
[output]: True

p1==p2+Point3D(-1,-1,-1)
[output]: True
# Your code replaces the prompt:  `...`

# In[ ]:


...


# You can manipulate these points (and make others!) to test your class 
p1 = Point3D(1,1,1)
p2 = Point3D(2,2,2)


# In[ ]:


grader.check("q3-point3d")

