#!/usr/bin/env python
# coding: utf-8

# # Accessing Items in a List
# 

# ## Consider a Circuit with Resistors in Series
# 
# Let's use a circuit with 9 volts of energy and three different resistors in series. 
# 
# ![image](https://www.allaboutcircuits.com/uploads/thumbnails/Figure_1._Series_circuit_with_a_battery_and_three_resistors__.jpg)
# 
# Let's use nested lists to store information about the circuit.

# In[1]:


# create each list individually before nesting
r1 = [3, "series", 1, 2]
r2 = [10, "series", 2, 3]
r3 = [5, "series", 3, 4]

# make a nested list of the resistors in the circuit
circuitSeries = [r1, r2, r3]


# Ohm's Law shows that the voltage (E) is equal to current (I) multiplied by resistance (R).
# 
# $E = IR$

# Let's apply Ohm's Law to find the current going through each resistor and append it to the nested list.

# In[2]:


# voltage through the circuit
V = 9

# current through first resistor
circuitSeries[0].append(V / circuitSeries[0][0])

print(circuitSeries[0])


# In[3]:


# total resistance and current
totalResistance = 0

for resistor in circuitSeries:
    totalResistance += resistor[0]

print(totalResistance)

