#!/usr/bin/env python
# coding: utf-8

# # Accessing Items in a List
# 

# ## Consider a Circuit with Resistors in Parallel
# 
# Let's use a circuit with 9 volts of energy and three different resistors in parallel. 
# 
# ![image](https://www.allaboutcircuits.com/uploads/thumbnails/Figure_1._Parallel_circuit_with_a_battery_and_three_resistors_.jpg)
# 
# Let's use nested lists to store information about the circuit.

# In[14]:


# create each list individually before nesting
r1 = ...
r2 = ...
r3 = ...

# make a nested list of the resistors in the circuit
circuitParallel = [r1, r2, r3]


# Ohm's Law is still applicable but to each of the parallel loops.
# 
# Ohm's Law shows that the voltage (E) is equal to current (I) multiplied by resistance (R).
# 
# $E = IR$
# 
# Apply Ohm's Law to determine the current through each resistor.

# In[ ]:


# voltage through the circuit
E = 9

# current through first resistor
...

# current through the second resistor
...

# current through the third resistor
...


# For a parallel circuit, the total current is the sum of the current across all of the resistors. 
# 
# In the  next cell, sum the current across the resistors *using a `for` loop to access the items in `circuitParallel`*.
# 

# In[ ]:


# sum the current across the resistors

for ... in ...: 
    ...

print(totalCurrent)


# Now, you can confidently use nested lists and can access each item in a list using a `for` loop.

# 
