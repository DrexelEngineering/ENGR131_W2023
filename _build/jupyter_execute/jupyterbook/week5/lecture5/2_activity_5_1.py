#!/usr/bin/env python
# coding: utf-8

# # 💻 Activity 5.1: Nuclear Plant Temperature Alert
# 
# We have just covered the relationship of a process value to a desired set point and discussed the importance of redundancy, especially in systems that have the potential to harm people.
# 

# Consider a nuclear reactor. A meltdown would be sufficiently catastrophic that the temperature of the cooling water around the nuclear fuel rods is monitored by four sensors. 
# 
# An alarm should go off if 
# 1. any of the two sensors report a temperature greater than 100 degrees Celsius, or 
# 2. any two of the sensor readings disagree by strictly 8 degrees. 
# 
# Write a function `coolingWaterAlarm(t1,t2,t3,t4)` where `t1`, `t2`, `t3`, and `t4` are the temperature readings for sensor 1, sensor 2, sensor 3, and sensor 4, respectively. 
# 
# The function should print 
# 
# 1. `Alarm! Temperatures differ.` if the first condition above is met,
# 2. `Alarm! Temperatures exceed 100 deg Celsius.` if the second condition above is met, or
# 3.  `Normal operation` if neither condition is met.

# In[ ]:


#write your function below



# In[1]:


import numpy as np


def coolingWaterAlarm(t1, t2, t3, t4):
    tlist = [t1, t2, t3, t4]
    # if (
    #     abs(t2 - t1) > 8
    #     or abs(t3 - t1) > 8
    #     or abs(t4 - t1) > 8
    #     or abs(t3 - t2) > 8
    #     or abs(t4 - t2) > 8
    #     or abs(t4 - t3) > 8
    # ):
    # option 2
    if max(tlist) - min(tlist) > 8:
        output = "Alarm! Temperatures differ."
    elif sorted(tlist, reverse=True)[1] > 100:
        output = "Alarm! Temperatures exceed 100 deg Celsius."
    else:
        output = "Normal operation"
    print(f"{output}")


# In[ ]:


# use this call to test your function
coolingWaterAlarm(93,95,96,101)


# In[ ]:


# use this call to test your function
coolingWaterAlarm(95,103,96,101)


# In[ ]:


# use this call to test your function
coolingWaterAlarm(90,95,96,101)

