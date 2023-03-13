#!/usr/bin/env python
# coding: utf-8

# # 💻 Activity: Practice with Variables and Operators
# 
# ## 1.2.1 Using Variables to Make a Price List
# 
# You are working for your favorite grocer and they want you to calculate the price of goods at checkout. Here is a list of prices:
# 
# | Item | Price per pound |
# |---|---|
# | Apples | \$1.50 |
# | Oranges | \$2.00 |
# | Bananas | \$0.75 |
# | Carrots | \$1.25 |
# | Beef | \$5.00 |
# | Salmon | \$8.00 |
# | Shrimp | \$9.00 |
# 
# <br>
# 
# | Item | Quantity | Price |
# |---|---|---|
# | Bread | 1 loaf | \$3.00 |
# | Milk | 1 gallon | \$3.50 |
# | Eggs | 1 dozen | \$3.00 |
# | Cheese | 1 lb | \$5.00 |
# | Yogurt | 6 pack | \$4.50 |
# 
# 
# 
# Purchases:
# 
# | Item | Quantity |
# |---|---|
# | Apples | 3 lbs |
# | Oranges | 2 lbs |
# | Bananas | 1 lb |
# | Carrots | 0.5 lb |
# | Bread | 1 loaf |
# | Milk | 1 gallon |
# | Eggs | 1 dozen |
# | Cheese | 1 lb |
# | Yogurt | 6 pack |
# 
# A. Write a python script to calculate your bill.
# B. Write a print statement the prints the total cost of your bill.

# In[1]:


# your solution goes here


# In[2]:


# Declare and assign values to variables for the cost of each item
Apples = 1.50
Oranges = 2.00
Bananas = 0.75
Carrots = 1.25
Beef = 5.00
Salmon = 8.00
Shrimp = 9.00
Bread = 3.00
Milk = 3.50
Eggs = 3.00
Cheese = 5.00
Yogurt = 4.50

bill = 0
bill += Apples * 3
bill += Oranges * 2
bill += Bananas * 1
bill += Carrots * 0.5
bill += Milk
bill += Eggs
bill += Cheese
bill += Yogurt

# Print the total cost
print(f"The total cost of the groceries is ${bill:.2f}.")


# ## 1.2.2 Planning for Paving a Driveway
# 
# You are tasked with ordering asphalt to pave a driveway that is 12 feet wide, and 28 feet long. You want the end pavement to be 3 inches thick. When water is added to mix the asphalt it expands by 20\% in volume, after pouring the asphalt reduces in volume by 31 percent. How much asphalt mix will you need to purchase. If it costs $1.03/cubic ft., what is the cost? You should include a safety factor (an excess) of 10\% for material lost during processing. 

# In[3]:


# Your solution goes here


# In[4]:


# width of the driveway in feet
width = 12

# length of the driveway in feet
length = 28

# thickness of the pavement in inches
thickness = 3

# safety factor to account for material lost during processing
safety_factor = 1.1

# expansion factor due to adding water
expansion_factor = 1.2

# shrinkage factor due to the asphalt setting
shrinkage_factor = 0.69

# cost in dollars
cost = 1.03

# Convert the thickness from inches to feet
thickness_in_feet = thickness / 12

# Calculate the area of the driveway in square feet
area = width * length

# Calculate the volume of the asphalt needed in cubic feet when set
volume_needed_set = area * thickness_in_feet * safety_factor

# Calculates the volume needed to pour
volume_poured = volume_needed_set / shrinkage_factor

# Calculates the volume needed to purchase
volume_purchased = volume_poured / expansion_factor

# Print the total amount of asphalt needed
print(
    f"You will need to purchase {volume_purchased:.2f} cubic feet of asphalt mix, equating to a price of {cost*volume_purchased:.2f} "
)


# After you do the calculation your boss runs back to you and says he found a product that expands by 30 percent on mixing and shrinks by 12 percent on setting. The problem is it cost $1.40/cubic ft.. Which product should you go with?

# In[5]:


# Your solution goes here


# In[6]:


# width of the driveway in feet
width = 12

# length of the driveway in feet
length = 28

# thickness of the pavement in inches
thickness = 3

# safety factor to account for material lost during processing
safety_factor = 1.1

# expansion factor due to adding water
expansion_factor = 1.3

# shrinkage factor due to the asphalt setting
shrinkage_factor = 0.88

# cost in dollars
cost = 1.40

# Convert the thickness from inches to feet
thickness_in_feet = thickness / 12

# Calculate the area of the driveway in square feet
area = width * length

# Calculate the volume of the asphalt needed in cubic feet when set
volume_needed_set = area * thickness_in_feet * safety_factor

# Calculates the volume needed to pour
volume_poured = volume_needed_set / shrinkage_factor

# Calculates the volume needed to purchase
volume_purchased = volume_poured / expansion_factor

# Print the total amount of asphalt needed
print(
    f"You will need to purchase {volume_purchased:.2f} cubic feet of asphalt mix, equating to a price of {cost*volume_purchased:.2f} "
)

