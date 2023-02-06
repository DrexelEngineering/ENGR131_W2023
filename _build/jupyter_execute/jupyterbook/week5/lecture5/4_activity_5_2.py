#!/usr/bin/env python
# coding: utf-8

# # Activity 5.2: Taking integrals with loops
# 

# Let's explore how two important choices impact the accuracy of this method for approximating integrals.
# 1. the width of the rectangle $h$, which is determined by the number of rectangles between $a$ and $b$
# 
# 2. the value of $x$ at which the function is evaluated (left, midpoint, or right)
# 
# ![](https://math.libretexts.org/@api/deki/files/6076/5.3.2.png?revision=1&size=bestfit&width=441&height=378)

# ## Interact with the code
# 
# 1. Add to the function `riemann` the correct expression for calculating the width of each rectangle using the number of rectangles passed into the function.
# 
# 2. Add the appropriate variable in the `range()` function in the `for` loop. 
# 
# 3. Why is the expression `i < (numRectangles-1)` appropriate for evaluating the height of the rectangle at the right side?

# In[ ]:


import numpy as np

def riemann(numRectangles,evalPoint): 
    # define the boundaries of the integral
    a = 0
    b = 5
    
    # define the curve
    x = np.linspace(a,b,numRectangles)
    f = np.sin(x/2)+1

    ### determine the width of the rectangle
    h = ...

    integral_R = 0.

    # integrate using the value of f at the right
    for i in range(...):
        if i < (numRectangles-1):
            integral_R += h * f[i+1]
    
    # print the integral, number of rectangles, and the chosen point for evaluation
    print(f'The integral is {integral_R} for {numRectangles} using the {evalPoint} point for evaluating the function.')


# Evaluate the function using 2, 5, and 11 rectangles between $a$ and $b$ and "right" as the evaluation point. 
# 
# Feel free to try other values, too, until you think you've approximated the integral reasonably well.
# 
# (Currently, the only calculation included in the function uses the right side of each rectangle as the value of the function.)

# In[ ]:


# call the function with two arguments 
# - one integer for the number of rectangles
# - one string for the "right" method

# 2 rectangles
riemann(...)

# 5 rectangles
riemann(...)

# 11 rectangles
riemann(...)

