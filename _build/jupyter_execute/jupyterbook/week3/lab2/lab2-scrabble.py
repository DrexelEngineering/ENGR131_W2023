#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Initialize Otter
import otter
grader = otter.Notebook("lab2-scrabble.ipynb")


# # 🧪🖥 Lab 2: Scrabble Score Calculator
# 
# In this lab you will use the map and reduce functions to calculate scores in the game Scrabble.
# 
# 

# ## Intro to Scrabble
# 
# Scrabble is a board game in which players lay tiles containing letters to spell words. Each letter has an associated point value based on the rarity of the letter. For instance, the very common letter `E` is worth only one point, while the much rarer `Q` is worth 10 points. The letter scores are shown in the table below:
# 
# <center>
# 
# | Score | Letters |
# | --- | --- |
# | 1 point | A, E, I, O, U, L, N, S, T, R |
# | 2 points | D, G |
# | 3 points | B, C, M, P |
# | 4 points | F, H, V, W, Y |
# | 5 points | K |
# | 8 points | J, X |
# | 10 points | Q, Z |
# 
# </center>
# 
# 
# 

# **Task 1: Letter score** 
# 
# Your first task is to complete a function which takes in a letter and outputs the score for that letter. A dictionary can be used to store the information from the scoring table above.   
# 
# Write python code to do the following:
# 
# * Inside the provided `letter_score` function, use the provided scores dictionary `S` to determine the score for the provided letter called `letter`.
# * Store the score in a variable called `score`.
# 
# Note: you may assume that the input letter will always be uppercase.
# 
# Your code replaces the prompt:  `...`

# In[ ]:


# this line creates a function called letter_score with one argument: letter
def letter_score(letter):
    # create the scoring dictionary of letter scores
    S = {
        "A" : 1,
        "B" : 3,
        "C" : 3,
        "D" : 2,
        "E" : 1,
        "F" : 4,
        "G" : 2,
        "H" : 4,
        "I" : 1,
        "J" : 8,
        "K" : 5,
        "L" : 1,
        "M" : 3,
        "N" : 1,
        "O" : 1,
        "P" : 3,
        "Q" : 10,
        "R" : 1,
        "S" : 1,
        "T" : 1,
        "U" : 1,
        "V" : 4,
        "W" : 4,
        "X" : 8,
        "Y" : 4,
        "Z" : 10,
    }
    ...
    # this line outputs the score from the function
    return score

# this runs the letter score function with input "Q" and prints its output
print(letter_score("Q"))


# In[ ]:


grader.check("task1-letter-score")


# **Task 2: Letter scores** 
# 
# Now that you have a function that computes the score for a letter, you can use Python's built-in `map` function to apply it to each letter in a word to get a list of letter scores. 
# 
# First you will need to convert the string `word` into a list of the individual letters. This can be achieved with `list(word)`. 
# 
# Next, use the `map` function to apply the `letter_score` function to each letter in the list. Recall how the `map` function is used: If you have a function `f` and a list `L = [a,b,c]`, you can do `map(f,L)` which results in the mapped list `[f(a), f(b), f(c)]`. 
# 
# Write python code to do the following:
# 
# * Inside the provided `letter_scores` function, first convert the argument string `word` into a list.
# * Map the `letter_score` function onto the list to get a list of letter scores. 
# * Store the final list of letter scores in a variable called `score_list`.
# 
# Your code replaces the prompt:  `...`

# In[ ]:


# this line creates a function called letter_scores with one argument: word
def letter_scores(word):
    ...
    # this line outputs the score list from the function
    return list(score_list)

# this runs the letter_scores function with input "EXAMPLE" and prints out the resulting list of letter scores
print(letter_scores("EXAMPLE"))


# In[ ]:


grader.check("task2-letter-scores")


# **Task 3: Word score** 
# 
# The last thing you need to do is sum the list of indivudal letters scores to get the total point value for the entire word.
# 
# To do this you should use the `sum` function. This adds all the elements of a list and returns the sum.
# 
# Write python code to do the following:
# 
# * Inside the provided `word_score` function, first call the `letter_scores` function on the input `word` to get the list of individual letter scores.
# * Next use the `sum` function on the list and `return` the final sum. 
# 
# Your code replaces the prompt:  `...`

# In[ ]:


def word_score(word):
    ...

# use this to check your results
word_score("ZEBRA")


# In[ ]:


grader.check("task3-word-score")

