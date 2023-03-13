#!/usr/bin/env python
# coding: utf-8

# # 💻 Activity 9.1: Building a Sensor Class
# 
# In manufacturing, you might be required to build software for a sensor. We will build a sensor with a name, a current value, a warning threshold, and alarm threshold. The sensor should return a string when the warning or alarm threshold is reached.
# 
# We will provide you with guidance on how to build this class. As you progress with coding, it is expected that you are able to write functional code with objectives but without specific instructions. Please add code where the `...` are located
# 

# In[ ]:


# Define the sensor class


    # write a warning announcement `Warning: sensor reading is high!`
    warning_announcement = ...

    # build the init function: this should instantiate the variables name, value, warning_threshold, alarm threshold,
    # and alarm announcement
    def ...:
        ...

    # build a method check value that will check if the value should cause a warning or an alarm.
    # for the alarm announcement, the alarm should print the current value with the alarm announcements
    # if the alarm does not go off, you should check if the sensor is above the warning threshold
    # if this is true, you should print the warning message
    # if there is no alarm, you should print the value
    def check_value(...):
        ...


# In[ ]:


import time

# Instantiate a temperature sensor
# the current temperature should be 20, the warning temperature should be 30, and the max temperature should be 40
# the alarm text should read ALARM: Temperature is too high!
...

# Make a loop that slowly increases the temperature from 20-50
# For each iteration, print the current temperature value
# Call the function that checks if the sensor has a warning
for ...:

    ...

    # This delays the loop so it does not go too fast
    time.sleep(1)


# In[ ]:




