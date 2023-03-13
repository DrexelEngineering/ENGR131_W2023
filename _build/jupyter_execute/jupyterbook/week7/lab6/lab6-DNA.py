#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Initialize Otter
import otter
grader = otter.Notebook("lab6-DNA.ipynb")


# # 🧪🖥 Lab 6: DNA Analysis
# 
# This lab conducts DNA analysis with strings and dictionaries.
# 
# 

# In[ ]:


# Imports


# **Introduction** 
# 
# In simple terms, your genetic code is a long string of characters drawn from a four-character alphabet `ACGT`, where each letter signifies a particular nucleic acid. Your skills using Python to manipulate strings can be used to perform analyses of genetic code. In this lab, you will write three functions that process a sample string of nucleic acid symbols in three particular ways.

# **Task 1: Base Counts** 
# 
# It can be important to count the number of times each nucleic acid occurs in a string of DNA. You will write a function which takes in a string of DNA and counts the number of times each base (`A`,`C`,`G`, or `T`) occurs. The function returns a dictionary where each key is a letter and its value is the number of times it occurs in the sequence. 
# 
# Write python code to do the following:
# 
# * Complete a function called `base_counts` which takes in a DNA string `s` of unknown length. 
# * First, initialize a dictionary with keys `"A"`,`"C"`,`"G"`, and `"T"`, each having a value of `0`.
# * Loop through the characters in string `s` and count each base by updating its value in the dictionary.
# * Finally, return the resulting dictionary of base counts.
# * Note: you may assume the string contains only the characters (`A`,`C`,`G`, and `T`).
# * Note: If any base does not occur in the string, that base should still be included in the dictionary, with a value of 0. 
# 
# Your code replaces the prompt:  `...`

# In[ ]:


def base_counts(s):
    ...

# use this to check your results
base_counts("AATTC")


# In[ ]:


grader.check("task1-base-counts")


# **Task 2: Pair Counts** 
# 
# In this next task you will count how many times pairs of bases occur in a string. Since there are 4 unique letters in the genetic code, there are 16 possible unique two-letter pairs. You will count pairs using a dictionary where the keys are two-character pairs (`"AA"`, `"AC"`, `"AG"`, etc.) and the values are the number of times each pair is observed. Note that every letter (except the very first and very last) is in two pairs: one where it is the first letter and the other where it is the second letter.
# 
# Write python code to do the following:
# 
# * Complete a function called `pair_counts` which again takes in a DNA string `s` of unknown length. 
# * First, initialize a dictionary with keys (`"AA"`, `"AC"`, `"AG"`, etc.), each having a value of `0`.
# * Loop through each pair in string `s` and count each by updating its value in the dictionary.
# * Finally, return the resulting dictionary of pair counts.
# * Note: you may assume the string contains only the characters (`A`,`C`,`G`, and `T`).
# * Note: As before, if any pair does not occur in the string, that pair should still be included in the dictionary, with a value of 0.
# 
# Hint: To loop through pairs in a string, consider looping over the index values of the first base in each pair. If `i` is the index of the first base, then `s[i:i+2]` slices the pair.
# 
# Your code replaces the prompt:  `...`
# 

# In[ ]:


def pair_counts(s):
    ...

# use this to check your results
pair_counts("AATTC")


# In[ ]:


grader.check("task2-pair-counts")


# **Task 3: Number of Stops**  
# 
# Triplets of DNA bases are called codons. Certain codons signal a stopping message and are called "stop codons." The following three-letter sequences are stop codons: `"TAG"`, `"TGA"`, `"TAA"`. Your final task is to count the number of times a stop codon occurs in a DNA string. 
# 
# Write python code to do the following:
# 
# * Complete a function called `num_stops` which takes in a DNA string `s` of unknown length. 
# * Initialize the count by setting a variable to zero. (You don't need a dictionary since you are only making one count.)
# * Loop through each triplet in string `s` and increment the count whenever a stop codon is encountered.
# * Finally, return the integer number of stops.
# * Note: you may assume the string contains only the characters (`A`,`C`,`G`, and `T`).
# 
# Hint: You can loop through triplets in a string just like pairs, by looping over the index values the first base in each triplet. If `i` is the index of the first base, then `s[i:i+3]` slices the triplet.
# 
# Your code replaces the prompt:  `...`
# 

# In[ ]:


def num_stops(s):
    ...

# use this to check your results
ex_string = "ATTTGAAATATGAATGTTAAGATGA"
print(f"{num_stops(ex_string)} stops detected in {ex_string}.")


# In[ ]:


grader.check("task3-num-stops")

