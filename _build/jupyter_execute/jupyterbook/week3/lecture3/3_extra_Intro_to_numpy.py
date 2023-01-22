#!/usr/bin/env python
# coding: utf-8

# # 📝 Introduction to NumPy

# NumPy is 
# * a package used to accelerate mathematical operations.

# * is specifically tailored towards matrix multiplication.

# * the first package we will be using in this course.

# * used on the backend in almost every python package that does math.

# * so efficient because it is written in C, but it is easy to use like Python.

# ## Importing NumPy
# 
# To use NumPy you need to import it. The convention for importing NumPy is:
# 
# `import numpy as np`

# <div class="admonition note alert alert-info">
# <p class="first admonition-title" style="font-weight: bold;">Note</p>
# Not all packages are installed with Python. You can download a distribution that contains common packages (e.g., Anaconda), or you can use the JupyterHub where we have installed the needed packages for you. If you need to install a package you can find most packages on the Python Package Index (PyPI). Usually packages can be installed by running `pip install <package_name>` from the terminal.
# </div>

# ## What is the difference between a Python list and a NumPy array?
# 

# 
# NumPy gives you an enormous range of fast and efficient ways of creating arrays and manipulating numerical data inside them. 
# 

# * Python list can contain different data types within a single list, all of the elements in a NumPy array should be homogeneous (of the same data type). 
# 

# * Mathematical operations that are meant to be performed on arrays would be extremely inefficient if the arrays weren’t homogeneous.

# ## What is an Array? 
# 
# An array is a central data structure of the NumPy library. An array is a grid of values and it contains information about the raw data, how to locate an element, and how to interpret an element. It has a grid of elements that can be indexed in [various ways](https://numpy.org/doc/stable/user/quickstart.html#quickstart-indexing-slicing-and-iterating). The elements are all of the same type, referred to as the array dtype.
# 

# ### Initializing Arrays

# In[1]:


# importing numpy
import numpy as np


# In[2]:


a = np.array([1, 2, 3, 4, 5, 6])


# or

# In[3]:


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


# ### Accessing an element
# 
# We can access the elements in the array using square brackets. 
# 

# * In NumPy starts at 0. That means that if you want to access the first element in your array, you’ll be accessing element `0`.

# In[4]:


print(a[0])


# ## Array Types
# 
# You might occasionally hear an array referred to as a “ndarray,” which is shorthand for “N-dimensional array.” An N-dimensional array is simply an array with any number of dimensions. 
# 
# * 1D, or one-dimensional array - Vector - magnitude and direction
# * 2D, or two-dimensional array - Image, stress, strain
# * 3D, or three-dimensional array - piezoelectricity
# * 4D or beyond tensor - elasticity, magnetism

# ### Attributes of an Array
# 
# * An array is usually a fixed-size container of items of the same type and size. 
# * The number of dimensions and items in an array is defined by its shape. 
# * The shape of an array is a tuple of non-negative integers that specify the sizes of each dimension.

# In[5]:


a = np.array([[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]])


# You can view the shape of a NumPy array using the built in method `.shape`

# In[6]:


a.shape


# Your array has 2 axes. The first axis has a length of 2 and the second axis has a length of 3.

# #### Modifying Arrays
# 
# * The contents of an array can be accessed and modified by indexing or slicing the array they are mutable. 
# * Unlike the typical container objects, different arrays can share the same data, so changes made on one array might be visible in another.

# In[7]:


a[1, 2] = 100
print(a)


# ## Creating Basic Arrays
# 
# To create an NumPy array, you can use the function `np.array()`

# ![](images/np_array.png)

# In[8]:


a = np.array([1, 2, 3])


# ### Preallocating a NumPy Array
# 
# Sometimes it is useful to preallocate an array in memory
# * This can be done using the `np.zeros` or `np.ones` methods

# In[9]:


print(np.zeros(2))


# In[10]:


print(np.ones(2))


# #### An Empty array
# 
# When you use zeroes or ones you need to rewrite all the states in memory which takes time.
# 

# 
# An empty array is filled with random values from the current memory state in the ram. This is way more efficient if initializing large arrays

# In[11]:


get_ipython().run_cell_magic('time', '', 'del(a)\na = np.empty((100,100,1000))\n')


# #### An ordered array
# 
# You can build an ordered array starting from 0 using `np.arrange()` method

# In[12]:


np.arange(4)


# There are many options within the `np.arrange()` method. `np.arrange([start(inclusive), stop(exclusive), step size])`

# In[13]:


np.arange(2, 10, 2)


# If you want to discover the syntax for a method you can search the docstring on the package website, or you can use `??` within Jupyter

# In[14]:


get_ipython().run_line_magic('pinfo2', ' np.arange')


# You can create a linear spaced vector using the `np.linspace()` method, where `np.linspace(start[inclusive], stop[inclusive], number_of_steps)` 

# In[15]:


np.linspace(0, 11, num=5)


# ## Adding, Removing, and Sorting Elements

# Sorting an element is simple with `np.sort()`. You can specify the axis, kind, and order when you call the function.
# 
# If you start with this array:

# In[16]:


arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])


# You can quickly sort the numbers in ascending order with:

# In[17]:


np.sort(arr)


# Other Sort Options: 
# 
# * [argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort), which is an indirect sort along a specified axis,
# 
# * [lexsort](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort), which is an indirect stable sort on multiple keys,
# 
# * [searchsorted](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted), which will find elements in a sorted array, and
# 
# * [partition](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#numpy.partition), which is a partial sort.

# ### Concatenating Arrays
# 
# If you start with these arrays:

# In[18]:


a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])


# You can concatenate them with `np.concatenate()`

# In[19]:


np.concatenate((a, b))


# Or

# In[20]:


x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
np.concatenate((x, y), axis=0)


# ## Determining the shape and size of an array?

# `ndarray.ndim` will tell you the number of axes, or dimensions, of the array.
# 
# `ndarray.size` will tell you the total number of elements of the array. This is the product of the elements of the array’s shape.
# 
# `ndarray.shape` will display a tuple of integers that indicate the number of elements stored along each dimension of the array. If, for example, you have a 2-D array with 2 rows and 3 columns, the shape of your array is (2, 3).

# In[21]:


array_example = np.array(
    [
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
    ]
)


# To find the number of dimensions of the array, run:

# In[22]:


array_example.ndim


# To find the total number of elements in the array, run:

# In[23]:


array_example.size


# And to find the shape of your array, run:

# In[24]:


array_example.shape


# ## Reshaping an Array
# 
# Using `arr.reshape()` will give a new shape to an array without changing the data. Just remember that when you use the reshape method, the array you want to produce needs to have the same number of elements as the original array. If you start with an array with 12 elements, you’ll need to make sure that your new array also has a total of 12 elements.

# In[25]:


a = np.arange(6)
print(a)


# In[26]:


b = a.reshape(3, 2)
print(b)


# ## Adding and Removing an Axis

# You can use `np.newaxis` and `np.expand_dims` to increase the dimensions of your existing array.
# 
# Using `np.newaxis` will increase the dimensions of your array by one dimension when used once. This means that a 1D array will become a 2D array, a 2D array will become a 3D array, and so on.
# 
# For example, if you start with this array:

# In[27]:


a = np.array([1, 2, 3, 4, 5, 6])
a.shape


# You can use `np.newaxis` to add a new axis:
# 
# 

# In[28]:


a2 = a[np.newaxis, :]
a2.shape


# You can remove an axis using `np.squeeze`

# In[29]:


a2.squeeze()


# ## Indexing and Slicing
# You can index and slice NumPy arrays in the same ways you can slice Python lists.

# In[30]:


data = np.array([1, 2, 3])


# In[31]:


data[1]


# In[32]:


data[0:2]


# In[33]:


data[1:]


# In[34]:


data[-2:]


# You can visualize it this way:
# 
# ![](images/np_indexing.png)

# If you want to select values from your array that fulfill certain conditions, it’s straightforward with NumPy.
# 

# In[35]:


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


# You can easily print all of the values in the array that are less than 5.
# 
# 

# In[36]:


print(a[a < 5])


# Or numbers that are divisible by 2

# In[37]:


divisible_by_2 = a[a % 2 == 0]
print(divisible_by_2)


# Or you can select elements that satisfy two conditions using the `&` (and) and `|` (or) operators:

# In[38]:


c = a[(a > 2) & (a < 11)]
print(c)


# You can also make use of the logical operators & and | in order to return boolean values that specify whether or not the values in an array fulfill a certain condition. This can be useful with arrays that contain names or other categorical values.

# In[39]:


five_up = (a > 5) | (a == 5)
print(five_up)


# You can also find the index that satisfy a condition using `np.argwhere`

# In[40]:


ind = np.argwhere((a > 2) & (a < 11))
print(ind)


# Or you can find a boolean and use it for indexing

# In[41]:


ind = np.where((a > 2) & (a < 11))
print(a[ind])


# ## How to create arrays from existing data?

# Let’s say you have this array:

# In[42]:


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# You can create a new array from a section of your array any time by specifying where you want to slice your array

# In[43]:


arr1 = a[3:8]
arr1


# Here, you grabbed a section of your array from index position 3 through index position 8.

# You can also stack two existing arrays, both vertically and horizontally. Let’s say you have two arrays, `a1` and `a2`:

# In[44]:


a1 = np.array([[1, 1], [2, 2]])

a2 = np.array([[3, 3], [4, 4]])


# You can stack them vertically with `vstack`:

# In[45]:


np.vstack((a1, a2))


# Or stack them horizontally with `hstack`:

# In[46]:


np.hstack((a1, a2))


# [Learn more about stacking and splitting arrays here](https://numpy.org/doc/stable/user/quickstart.html#quickstart-stacking-arrays)

# ## Copies and Views
# 
# When operating and manipulating arrays, their data is sometimes copied into a new array and sometimes not. This is often a source of confusion for beginners. There are three cases:

# ### No Copy at All
# 
# Simple assignments make no copy of objects or their data.

# In[47]:


a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
b = a
b is a


# Python passes mutable objects as references, so function calls make no copy.

# In[48]:


def f(x):
    print(id(x))


f(a)
f(b)


# See, they really are the same, this is useful if you want to save memory

# ### View or Shallow Copy
# 
# Different array objects can share the same data. The `view` method creates a new array object that looks at the same data.

# In[49]:


c = a.view()
c is a


# In[50]:


c.base is a  # c is a view of the data owned by a


# In[51]:


c = c.reshape((2, 6))  # a's shape doesn't change


# In[52]:


a.shape


# In[53]:


c[0, 4] = 1234  # a's data changes


# In[54]:


a


# Note that operations on the object can be applied without effecting the original object. If a value is changed it does effect the original object.

# ### Deep Copy
# The copy method makes a complete copy of the array and its data
# 
# This will consume the same amount of memory as the original object

# In[55]:


d = a.copy()  # a new array object with new data is created


# In[56]:


d is a


# In[57]:


d.base is a  # d doesn't share anything with a


# In[58]:


d[0, 0] = 9999


# In[59]:


a


# ## Basic array operations
# 
# Once you’ve created your arrays, you can start to work with them. Let’s say, for example, that you’ve created two arrays, one called “data” and one called “ones”
# 
# ![](figs/np_array_dataones.png)

# You can add the arrays together with the plus sign.
# 
# ![](figs/np_data_plus_ones.png)

# In[60]:


data = np.array([1, 2])
ones = np.ones(2, dtype=int)
data + ones


# You can do all operations on arrays
# 
# ![](figs/np_sub_mult_divide.png)

# In[61]:


data - ones


# In[62]:


data * data


# In[63]:


data / data


# Basic operations are simple with NumPy. If you want to find the sum of the elements in an array, you’d use `sum()`. This works for 1D arrays, 2D arrays, and arrays in higher dimensions.

# In[64]:


a = np.array([1, 2, 3, 4])
a.sum()


# To add the rows or the columns in a 2D array, you would specify the axis.
# 
# If you start with this array:

# In[65]:


b = np.array([[1, 1], [2, 2]])
b.sum(axis=0)


# or

# In[66]:


b = np.array([[1, 1], [2, 2]])
b.sum(axis=1)


# [Learn More about basic operations here](https://numpy.org/doc/stable/user/quickstart.html#quickstart-basic-operations)

# Besides `sum` there are a plethora of built in calculations. You can discover more [here](https://numpy.org/doc/stable/reference/arrays.ndarray.html#calculation)

# ## Broadcasting
# 
# There are times when you might want to carry out an operation between an array and a single number (also called an operation between a vector and a scalar) or between arrays of two different sizes. For example, your array (we’ll call it “data”) might contain information about distance in miles but you want to convert the information to kilometers. You can perform this operation with:

# In[67]:


data = np.array([1.0, 2.0])
data * 1.6


# ![](figs/np_multiply_broadcasting.png)
# 
# NumPy understands that the multiplication should happen with each cell.  
# * Broadcasting is a mechanism that allows NumPy to perform operations on arrays of different shapes. 
# * The dimensions of your array must be compatible, for example, when the dimensions of both arrays are equal or when one of them is 1. 
# * If the dimensions are not compatible, you will get a ValueError.
# 
# [Learn more about broadcasting here.](https://numpy.org/doc/stable/user/basics.broadcasting.html#basics-broadcasting)

# ## Finding Unique Items and Counts

# You can find the unique elements in an array easily with `np.unique`
# 

# 
# For example, if you start with this array:
# 

# In[68]:


a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])


# you can use `np.unique` to print the unique values in your array:
# 

# In[69]:


unique_values = np.unique(a)
print(unique_values)


# To get the indices of unique values in a NumPy array (an array of first index positions of unique values in the array), just pass the return_index argument in `np.unique()` as well as your array.

# In[70]:


unique_values, indices_list = np.unique(a, return_index=True)
print(indices_list)


# There are many more options which can be read in the doc string

# ## Transposing and Reshaping
# 
# It’s common to need to transpose your matrices. NumPy arrays have the property T that allows you to transpose a matrix.
# 
# ![](figs/np_transposing_reshaping.png)

# In[71]:


data = np.array([[1, 2], [3, 4], [5, 6]])
data.T


# You may also need to switch the dimensions of a matrix. This can happen when, for example, you have a model that expects a certain input shape that is different from your dataset. This is where the `reshape` method can be useful. You simply need to pass in the new dimensions that you want for the matrix.
# 
# ![](figs/np_reshape.png)

# In[72]:


data.reshape(2, 3)


# In[73]:


data.reshape(3, 2)


# To learn more about transposing and reshaping arrays, see [transpose](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose) and [reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape).
