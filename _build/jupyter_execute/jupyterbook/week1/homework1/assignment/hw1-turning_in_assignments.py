#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Initialize Otter
import otter
grader = otter.Notebook("hw1-turning_in_assignments.ipynb")


# # Homework 1 🏡📝 - Using Jupyter and Turning in Assignments
# 
# In this class we will be using Jupyter Notebooks for completing homeworks. This homework assignment will make sure you are comfortable using these tools. 
# 
# Jupyter notebooks are Java-Script Object Notation files that allow you to create documents to move and transport code and documentation that can be run interactively. The postfix for the file is `.ipynb`, you can think of this like a word document for python. 
# 
# In this homework assignment we want you to demonstrate your proficiency using this system. We will provide you some code that allows you to create your own personalized T-shirt logo. 
# 
# Instructions: 
# 1. Open the notebook from the course website using the Jupyterhub. You can do this by clicking on the rocket ship and selecting jupyterhub.
# 2. Copy and paste the provided code. 
# 
# ```python
# import numpy as np
# from PIL import Image, ImageDraw, ImageFont
# import skimage
# from skimage.transform import rescale, resize, downscale_local_mean
# #import matplotlib.pyplot as plt
# 
# class your_branded_shirt(): 
#     
#     def __init__(self, validation = False):
#         
#         # identifies the location of the drexel dragon file
#         image_filename = "https://raw.githubusercontent.com/DrexelEngineering/ENGR131_W2023/main/jupyterbook/assets/drexel-dragon-all_blue.png"
# 
#         # loads the drexel dragon file into a numpy array
#         self.image = skimage.io.imread(image_filename)
#                 
#         self.font = ("./arial.TTF")
#         
#         self.validation = validation
#         
# 
#     def color_random(self):
#         
#         # selects a random int between 0,255 with size of 3 for RGB.
#     color = np.random.choice(range(255), size=3).astype("uint8")
#         
#         # makes sure the color is not too blue to conceal the drexel logo
#         if color[2] > 150:
#             color[2] = 150
# 
#         # returns the color    
#         return color
# 
# 
#     def rgb_to_hex(self, rgb):
#         # function to convert RGB to hex
#         return "%02x%02x%02x" % rgb
# 
# 
#     def image_canvas(self, text, size):
# 
#         # Create font
#         pil_font = ImageFont.truetype(self.font, size=size, encoding="unic")
# 
#         # gets size of the text
#         _, _, text_width, text_height = pil_font.getbbox(text)
# 
#         # creates a canvas based on the size of the text
#         return np.zeros((text_height, text_width + len(text) // 2, 3), dtype="uint8")
# 
# 
#     def text_phantom(self, text, size):
# 
#         # Create font
#         pil_font = ImageFont.truetype(self.font, size=size, encoding="unic")
#         _, _, text_width, text_height = pil_font.getbbox(text)
# 
#         # create a blank canvas with extra space between lines
#         canvas = Image.new("RGB", [text_width, text_height], (255, 255, 255))
# 
#         # draw the text onto the canvas
#         draw = ImageDraw.Draw(canvas)
# 
#         offset = (0, 0)
# 
#         # Calls the function to choose a random color
#         color_ = self.color_random()
# 
#         # converts the color from RGB to hex
#         color = "#" + self.rgb_to_hex((color_[0], color_[1], color_[2]))
#         
#         # draws the text
#         draw.text(offset, text, font=pil_font, fill=color)
# 
#         # Convert the canvas into an array with values in [0, 1]
#         return 255 - np.asarray(canvas)
# 
# 
#     def multicolor_image(self, text, height):
#         
#         # creates the canvas
#         out = self.image_canvas(text, height)
#         
#         # sets an initial position
#         pos = 0
# 
#         # for loop that goes around each letter in the text
#         for i in text:
#             letter = self.text_phantom(i, height)
# 
#             #Add the letter to the image
#             out[0 : letter.shape[0], pos : pos + letter.shape[1], :] = letter
#             
#             # adjusts the position so the letters do not overlap
#             pos += letter.shape[1]
# 
#         return out
# 
# 
#     def build_image(self, name):
#     
#         # creates a 256,256,3 image where 3 represents RGB
#         bkgr = np.zeros((256, 265, 3), dtype="uint8")
# 
#         # Sets the background to be a random color
#         bkgr[:, :, :] = self.color_random()
# 
#         # Resizes the image to fit within the frame
#         image_resized = resize(self.image, (106, 150), anti_aliasing=True)
# 
#         # places the drexel dragon image in the correct location
#         bkgr[3:109, (256 - 150) // 2 : (256 - 150) // 2 + 150][
#             image_resized[:, :, :-1].sum(axis=2) < 2
#         ] = (image_resized[:, :, :-1] * 255).astype("uint8")[
#             image_resized[:, :, :-1].sum(axis=2) < 2
#         ]
# 
#         # writes the word congratulations as multicolored text
#         out = self.multicolor_image("Congratulations!", 33)
# 
#         # adds the word congratulations to the image under the dragon
#         bkgr[
#             126 : 126 + out.shape[0],
#             (256 - out.shape[1]) // 2 : (256 - out.shape[1]) // 2 + out.shape[1],
#         ][out.sum(axis=2) > 0.1] = out.astype("uint8")[out.sum(axis=2) > 0.1]
# 
#         # moves the starting y position down a line
#         y = 126 + out.shape[0]
# 
#         # You type your comment here for what this line of code does. 
#         out = self.multicolor_image(name, 33)
# 
#         # Adds your name to the image
#         bkgr[
#             y + 10 : y + 10 + out.shape[0],
#             (256 - out.shape[1]) // 2 : (256 - out.shape[1]) // 2 + out.shape[1],
#         ][out.sum(axis=2) > 0.1] = out.astype("uint8")[out.sum(axis=2) > 0.1]
#         
#         if self.validation:
#             image = bkgr
#         else:
#             # makes the image
#             image = plt.imshow(bkgr)
#             
#             # saves the image
#             plt.savefig(f'{name}_image.png')
#         
#         # returns the plot 
#         return image
# 
# ```
# 
# 3. As you can see we have used `#` to add comments to the code. This is an important part of your assignments and grade. Comments show us that you not only completed the assignments but understand the code. 
# 4. The following code has 3 problems which need to be fixed so that it can run. We would like you to get comfortable reading error messages and using the `friendly.jupyter` to help you discover your errors. There are small errors or corrections that need to be made on lines 5, 25, and 130. 
# 
# Hint: you can simply view the line numbers by pressing `shift + l` when in a cell. You can toggle between typing and edit mode using the `esc` key.
# 
# 5. You need to instantiate the the class by typing `shirt =  your_branded_shirt()`
# 
# 6. We would like you to call the `shirt.build_image` function to produce your image. You do this by typing `shirt.build_image("Your Name")` into a new cell after running the copied code. You replace \<Your Name\> with your actual name. Make sure your name is in `"` as this defines a string of characters in python. 
# 
# Hint: cells can be run by pressing `shift` + `enter`
# 
# 7. We would like you to download the `.ipynb` file and your image from the jupyter hub. Please upload these files to bblearn for grading. 
# 
# Because of the size of the class we are using autograding technologies to assist with grading. Thus ensuring that your files match the naming convention is critical to receiving credit. 
# 

# Run the following code by pressing `shift + enter`, this is a module that helps explain errors to you.

# In[ ]:


from friendly.jupyter import *


# **Question 1: Make Your Branded Shirt**
# 
# 

# In[2]:


# Paste your code here

...


# In[3]:


# Your command to run build image goes here

...


# In[4]:


grader.check("q1-Make Your Branded Shirt")

