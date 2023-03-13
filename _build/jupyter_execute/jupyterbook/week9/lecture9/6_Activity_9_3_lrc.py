#!/usr/bin/env python
# coding: utf-8

# # 💻 Activity 9.3: Building the game LCR
# 
# Left-Center-Right (also known as LCR) is a simple dice game that can be played with any number of players, making it a great option for parties or family gatherings. The game requires three six-sided dice and a handful of chips or other small items to use as currency. Here are the rules:
# 
# - Each player starts with three chips.
# - The game begins with each player rolling the three dice.
# - The result of the roll determines what action each player must take:
#   - If a player rolls an "L," they must pass one chip to the player on their left.
#   - If a player rolls an "R," they must pass one chip to the player on their right.
#   - If a player rolls a "C," they must put one chip into the center pot.
#   - If a player rolls a number, they keep their chips for that round.
# - The game continues with each player rolling the dice and following the corresponding action until only one player has any chips left.
# - The player with chips remaining is the winner and collects all the chips from the center pot.
# - If a player runs out of chips, they are out of the game. 
# - If a player has only one chip left, they only roll one dice.
# - Players can agree to increase the number of chips each player starts with or add other variations to the game to make it more interesting.
# 
# That's it! LCR is a quick and easy game to learn, but it can be surprisingly addictive and competitive.
# 
# You will build this game using classes an inheritance. Again, we will be practicing your ability to problem solve in code. 
# 

# In[ ]:


import random


# Import the random module.
# Define a new class called Dice.
# Within the Dice class, define an __init__ method that initializes the class with a list of sides. 
# By default, the list contains the strings "L", "R", and "C".
# Within the Dice class, define a roll method that returns a random element from the list of sides.
# To create a new Dice object, create a new instance of the class.
# To roll the die, call the roll method on your Dice object.
# If you want to create a Dice object with custom sides, pass a list of strings representing the sides when you create the object.
...


# Define a new class called Player.
# The Player class should inherit from the Dice class.
# Within the Player class, define an __init__ method that initializes the class with a name, position, chips, CPU, and dice value. 
# chips should be set to 3 by default, and CPU should be set to True by default. 
# If a dice object is passed, the sides of the Player object's dice should be set to the sides of the passed dice object.
# Within the Player class, define a take_chip method that subtracts one chip from the player's chips value and returns 1.
# Within the Player class, define a give_chip method that adds one chip to the player's chips value and returns 1.
class Player(...):
    def __init__(...):
        super().__init__()
        if dice is not None:
            self.sides = dice.sides
        ...

    def take_chip(self):
        ...

    def give_chip(self):
        ...


# Define a list of players instantiated from the `Player` class above
# Make it so the 0th player is a human and a cheater by having biased dice
players = ...


# initialize center_pot as 0
...


# Create a while loop that runs as long as the length of the players list is greater than 1.
# Within the while loop, use a for loop to iterate through each player in the players list.
# Print out the current state of the game, including the number of chips each player has and the number of chips in the center pot.
# Wait for the user to press the Enter key to continue.
# Roll the dice for the current player a number of times equal to the player's current number of chips.
# Print out the result of each roll.
# For each roll:
# If the roll is an "L," the current player should take a chip and give it to the player to their left. Print a message indicating the chip transfer.
# If the roll is an "R," the current player should take a chip and give it to the player to their right. Print a message indicating the chip transfer.
# If the roll is a "C," the current player should put a chip in the center pot. Print a message indicating the chip transfer.
# If the roll is a number, do nothing.
# If the current player has no chips remaining, remove them from the players list. You can use the list method `.remove`
# Update each player's position attribute to reflect their new position in the players list, and who they pass to. 
# This helps correct if someone was removed from the game.
# hint, the player to the right can be determined using `players[(player.position + 1) % len(players)]`
while ...:

    for ...:

        print("Current State:")

        for ...:

            print(f"{players[i].name}: {players[i].chips}")


        print(f"Center Pot: {center_pot}\n")

        input("Press Enter to continue...")

        rolls = [player.roll() for _ in range(player.chips)]
        print(f"{player.name} rolls: {' '.join(rolls)}")
        
        for roll in rolls:
            if roll == "L":
                ...
                ...
                print(
                    "{player.name} passes a chip to {players[player.position - 1].name} on the left"
                    )
                
            elif roll == "R":
                player.take_chip()
                players[(player.position + 1) % len(players)].give_chip()
                print(
                    f"{player.name} passes a chip to {players[(player.position + 1) % len(players)].name} on the right"
                    )
            elif roll == "C":
                ...
                center_pot += 1
                print(f"{player.name} puts a chip in the center pot")
            else:
                print("Does Nothing")

        if ...:
            ...

        for ... in ...:
            player.position = ...


# print the winner
print("The winner is", players[0].name)


# In[ ]:




