#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Initialize Otter
import otter
grader = otter.Notebook("lab4-RPS.ipynb")


# # 🧪🖥 Lab 4: Rock, Paper, Scissors Game
# 
# In this lab you will use branching to complete a playable game of rock paper scissors.
# 
# 

# In[ ]:


import random


# ## History of Rock, Paper, Scissors
# 
# Rock paper scissors (also known by other orderings of the three items, with "rock" sometimes being called "stone," or as Rochambeau, roshambo, or ro-sham-bo) is a hand game originating from China, usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock" (a closed fist), "paper" (a flat hand), and "scissors" (a fist with the index finger and middle finger extended, forming a V). "Scissors" is identical to the two-fingered V sign (also indicating "victory" or "peace") except that it is pointed horizontally instead of being held upright in the air.
# 
# A simultaneous, zero-sum game, each round has three possible outcomes: a tie, a win or a loss. A player who decides to play rock will beat another player who has chosen scissors ("rock crushes scissors" or "breaks scissors" or sometimes "blunts scissors"), but will lose to one who has played paper ("paper covers rock"); a play of paper will lose to a play of scissors ("scissors cuts paper"). If both players choose the same shape, the game is tied and is usually immediately replayed to break the tie. The game spread from China while developing different variants in signs over time.
# 

# **Task 1: Check for valid input** 
# 
# In your game of Rock, Paper, Scissors, it will be the player vs. the computer. The player will make their selection each round by typing either `"rock"`, `"paper"`, or `"scissors"`. The first task is to write a function that checks to make sure that the input entered by the player is valid.
# 
# Write python code to do the following:
# 
# * Complete the function called `valid_input` which takes as input a string `player_choice`.
# * The function should return `True` if `player_choice` equals `"rock"`, `"paper"`, or `"scissors"`.
# * Otherwise the function should return `False`. 
# 
# Your code replaces the prompt:  `...`

# In[ ]:


def valid_input(player_choice):
    ...

# use this to check your results
valid_input("paper")


# In[ ]:


grader.check("task1-input")


# **Task 2: Get Round Result Message** 
# 
# In each round, we want to display a result message that explains the outcome. Your next task is to write a function to determine the message that should displayed based on the choices of the player and computer. The table below shows the message to display if the player and computer choose different options. 
# 
# <center>
# 
# | `player_choice` | `computer_choice` | `message` |
# | --- | --- | --- |
# | `"rock"` | `"paper"` | `"You lose! Paper covers rock."` |
# | `"rock"` | `"scissors"` | `"You win! Rock crushes scissors."` |
# | `"paper"` | `"rock"` | `"You win! Paper covers rock."` |
# | `"paper"` | `"scissors"` | `"You lose! Scissors cuts paper."` |
# | `"scissors"` | `"rock"` | `"You lose! Rock crushes scissors."` |
# | `"scissors"` | `"paper"` | `"You win! Scissors cuts paper."` |
# 
# </center>
# 
# If the player and the computer make the same choice, the the displayed message should be:
# `"It's a tie!"` 
# 
# Write python code to do the following:
# 
# * Complete the function called `round_message` which takes in two strings, `player_choice` and `computer_choice`.
# * If the player and computer choose different options, the function should return a string containing the appropriate message based on the table above.
# * If the player and computer choose the same, then the tie message above should be returned.
# 
# Your code replaces the prompt:  `...`

# In[ ]:


def round_message(player_choice, computer_choice):
    ...

# use this to check your results
round_message("paper", "scissors")


# In[ ]:


grader.check("task2-round-message")


# **Task 3: Get Final Message** 
# 
# The game will be played in rounds until one player has reached a score of 2. When the game ends, a final message is displayed indicating whether the player won or lost. Your final task is to write the function that determines this final message based on the score.
# 
# Write python code to do the following:
# 
# * Complete the function called `final_message` which takes in two integers, `player_score` and `computer_score`.
# * If the `player_score` is greater than `computer_score`, return the string: `"You won the game!"`
# * If the `player_score` is less than `computer_score`, return the string: `"You lost the game!"` 
# * You don't need to worry about handling a tie, since the game will only end when someone has won.
# 
# Your code replaces the prompt:  `...`

# In[ ]:


def final_message(player_score, computer_score):
    ...

# use this to check your results
final_message(2,0)


# In[ ]:


grader.check("task3-final-message")


# ## Play the game!
# Once you've completed the three tasks above, run the code below to play the game. Read through the commented code carefully and try to follow the logic of the implementation.

# In[ ]:


# imports randomint package to select a random integer
from random import randint

# a list of choices the compute can pick from
choices = ["rock", "paper", "scissors"]

# initialize the score to 0/0
player_score = 0
computer_score = 0

# initialize the round number to 1
round = 1

# keep playing while nobody has a score == 2
while player_score < 2 and computer_score < 2:

    # print the round number
    print(f"Round {round}\n-------")

    # loop forever! (until we break out)
    while True:
        # get input from the player
        player_choice = input("Your choice:")
        # if the input is valid, break out of the while loop
        if valid_input(player_choice):
            break
        # otherwise warn the player of invalid input and have them try again
        else:
            print("Invalid input. Must be \"rock\", \"paper\" or \"scissors\". Try again.")
    
    # have a computer make a random selection from the choices
    computer_choice = choices[randint(0,2)]

    # print out the player and computer choices
    print(f"Player choice: {player_choice}")
    print(f"Computer choice: {computer_choice}")

    # get and store the round result message
    message = round_message(player_choice, computer_choice)

    # print the message
    print(message)

    # use the round result message to tell who won
    # split the message at the spaces to get a list of words
    # The second word (at index 1) is "win!" or "lose!" indicating the result
    if message.split()[1] == "win!":
        # add 1 to the player score
        player_score += 1
    elif message.split()[1] == "lose!":
        # add 1 to the computer score
        computer_score += 1

    # increment the round number
    round += 1
    # print an empty line
    print()

# get and print the final message
print(final_message(player_score, computer_score))
# print the score
print(f"Final score | You : {player_score} | Computer : {computer_score} |")

