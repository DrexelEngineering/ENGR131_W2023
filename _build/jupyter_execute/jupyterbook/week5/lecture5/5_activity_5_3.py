#!/usr/bin/env python
# coding: utf-8

# # 💻 Activity 5.3: Advancing integral evaluations by combining loops and branches

# We wanted to explore how two important choices impact the accuracy of this method for approximating integrals.
# 
# ✅ 1. the width of the rectangle $h$, which is determined by the number of rectangles between $a$ and $b$
# 
# Now, let's explore
# 
# 2. the value of $x$ at which the function is evaluated (left, midpoint, or right)
# 
# ![](https://math.libretexts.org/@api/deki/files/6076/5.3.2.png?revision=1&size=bestfit&width=441&height=378)

# ## Interact with the code
# 
# 1. Add the branching structure *inside* the current function to cause different calculations to occur if the `evalPoint` variable is `"right", "mid", or "left"`.
# 
# 2. Include an extra case in which the user receives a helpful message if the string for `evalPoint` is not one of the three options.

# In[ ]:


import numpy as np

def reimann(numRectangles,evalPoint): 
    # define the boundaries of the integral
    a = 0
    b = 5
    
    # define the curve
    x = np.linspace(a,b,numRectangles)
    f = np.sin(x/2)+1

    ### determine the width of the rectangle
    h = ...

    integral_R = 0.

    # add branching structure for evalPoint to calculate the integral in three different ways

    # integrate using the value of f at the right
    for i in range(...):
        if i < (numRectangles-1):
            integral_R += h * f[i+1]
   
    
    # print the integral, number of rectangles, and the chosen point for evaluation
    print(f'The integral is {integral_R} for {numRectangles} using the {evalPoint} point for evaluating the function.')


# In[1]:


import numpy as np

def reimann(numRectangles,evalPoint): 
    # define the boundaries of the integral
    a = 0
    b = 5
    
    # define the curve
    x = np.linspace(a,b,numRectangles)
    f = np.sin(x/2)+1

    ### determine the width of the rectangle
    h = (b - a) / (numRectangles - 1)

    integral_R = 0.

    # add branching structure for evalPoint to calculate the integral in three different ways
    if evalPoint == "right":
        
        # integrate using the value of f at the right
        for i in range(numRectangles):
            if i < (numRectangles-1):
                integral_R += h * f[i+1]
                
    elif evalPoint == "left":
        pass
    elif evalPoint == "mid":
        pass
    else: 
        print("The evaluation point method is not 'right', 'left', or 'mid'. Please try again.")

    # print the integral, number of rectangles, and the chosen point for evaluation
    print(f'The integral is {integral_R} for {numRectangles} using the {evalPoint} point for evaluating the function.')


# Consider how the calculation at the left side of the rectangle or the midpoint would differ from the right. 
# 
# 1. Copy the `for` loop from the right-side calculation into each branch and make the few necessary changes to calculate `integral_R` using these two different approaches.

# In[ ]:


import numpy as np

def reimann(numRectangles,evalPoint): 
    # define the boundaries of the integral
    a = 0
    b = 5
    
    # define the curve
    x = np.linspace(a,b,numRectangles)
    f = np.sin(x/2)+1

    ### determine the width of the rectangle
    h = ...

    integral_R = 0.
    j = 1

    # add branching structure for evalPoint to calculate the integral in three different ways
    
    # print the integral, number of rectangles, and the chosen point for evaluation
    print(f'The integral is {integral_R} for {numRectangles} using the {evalPoint} point for evaluating the function.')


# In[2]:


import numpy as np

def reimann(numRectangles,evalPoint): 
    # define the boundaries of the integral
    a = 0
    b = 5
    
    # define the curve
    x = np.linspace(a,b,numRectangles)
    f = np.sin(x/2)+1

    ### determine the width of the rectangle
    h = (b - a) / (numRectangles - 1)

    integral_R = 0.
    j = 1

    # add branching structure for evalPoint to calculate the integral in three different ways
    if evalPoint == "right":
        # integrate using the value of f at the right
        for i in range(numRectangles):
            if i < (numRectangles-1):
                j+= 1
                integral_R += h * f[i+1]
    elif evalPoint == "left":
        # integrate using the value of f at the right
        for i in range(numRectangles):
            if i > (0):
                j+= 1
                integral_R += h * f[i]
    elif evalPoint == "mid":
        # integrate using the value of f at the right
        for i in range(numRectangles):
            if i < (numRectangles-1):
                j += 1
                integral_R += h * (f[i]+f[i+1])/2
    else: 
        print("The evaluation point method is not 'right', 'left', or 'mid'. Please try again.")
    
    # print the integral, number of rectangles, and the chosen point for evaluation
    print(j)
    print(f'The integral is {integral_R} for {numRectangles} using the {evalPoint} point for evaluating the function.')


# Explore how both the number of rectangles and the point at which the function is evaluated influence the resulting integral. 
# 
# 1. Is a higher or lower number of rectangles better?
# 
# 2. Is the "left", "right", or "mid" point best?

# In[ ]:


# call the function with two arguments 
# - one integer for the number of rectangles
# - one string for the "right" method

# 2 rectangles, right
reimann()
# 2 rectangles, left
reimann()
# 2 rectangles, mid
reimann()

# 5 rectangles, right
reimann()
# 5 rectangles, left
reimann()
# 5 rectangles, mid
reimann()


# 11 rectangles, right
reimann()
# 11 rectangles, left
reimann()
# 11 rectangles, right
reimann()


# In[3]:


# call the function with two arguments 
# - one integer for the number of rectangles
# - one string for the "right" method

# 2 rectangles, right
reimann(2,"right")
# 2 rectangles, left
reimann(2,"left")
# 2 rectangles, mid
reimann(2,"mid")

# 5 rectangles, right
reimann(5,"right")
# 5 rectangles, left
reimann(5,"left")
# 5 rectangles, mid
reimann(5,"mid")


# 11 rectangles, right
reimann(11,"right")
# 11 rectangles, left
reimann(11,"left")
# 11 rectangles, right
reimann(11,"mid")

# 22 rectangles, right
reimann(22,"right")
# 22 rectangles, left
reimann(22,"left")
# 22 rectangles, right
reimann(22,"mid")


