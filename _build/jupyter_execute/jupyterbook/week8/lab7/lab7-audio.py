#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Initialize Otter
import otter
grader = otter.Notebook("lab7-audio.ipynb")


# # 🧪🖥 Lab 7: Audio Synthesis with Numpy
# 
# This lab explores using loops to synthesize different types of audio waveform in python.
# 
# 

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import IPython.display as ipd


# **Generating a Sine Wave** 
# 
# A sine wave $s(t)$ with amplitude $A$ and frequency $f$ can be computed using the following equation:
# 
# $$ s(t) = A sin(2 \pi f t)$$
# 
# 
# 
# In python, we can compute an array of values of the sine function by making $t$ be an array of time values.
# 
# For instance, the following code sets `t` to be an array of $16000$ values lienaarly spaced from 0 to 1. (A few of these values are shown when we print `t` below.)
# 

# In[ ]:


# creates an array of 16000 time values from 0 to 1
t = np.linspace(0, 1, num=16000, endpoint=False) 

print(t)


# Now we can plug our `t` array in into our equation to get a sine wave `s`:

# In[ ]:


# amplitude of 1.0
A = 1.0 
# frequency of 440.0
f = 440.0

# compute sine wave from equation
s = A * np.sin(2 * np.pi * f * t) 


# Now if we print `s`, it might be difficult to tell that it's a sine wave...

# In[ ]:


print(s)


# So let's plot it!

# In[ ]:


# plot sinusoid s
plt.plot(s)
# show just the first 100 values
plt.xlim(0,100)


# We can listen to the sine wave audio with the code below. (The sampling rate 16000 needs to be provided to specify how quickly we want to play the audio samples.)

# In[ ]:


# we must provide 
ipd.Audio(s, rate=16000)


# **Task 1: Approximating a Square Wave with Sinusoids** 
# 
# A square wave is a waveform that alternates steadily between two fixed values. We can compute a square wave $q(t)$ with fundamental frequency $f$ using the following infinite sum of sinusoids: 
# 
# $$ q(t) = \sum_{k=0}^{\infty} \frac{sin(2 \pi (2k+1) f t)}{2k+1}$$
# 
# Usually it is a good option to use a `for` loop when implementing a mathematical sum in python. However, this sum goes to inifinity: we can't compute infinite loops. We can get an approximation of a square wave by summing just the first $K$ terms:
# 
# $$ q(t) \approx \sum_{k=0}^{K-1} \frac{sin(2 \pi (2k+1) f t)}{2k+1}$$
# 
# Write python code to do the following:
# 
# * Complete the function called ``square_wave`` which returns an approximate square wave based on input arguments (a fundamental frequency `f` and a number of terms `K`).
# * Loop over the desired number of terms `K`.
# * For each term, calculate the appropriate sinusoid and add it to the provided starting array `q`. 
# * For the input time value $t$ in the equation above, use the provided array of tiem values `t`. 
# * The function returns the approximate square wave q. 
# 
# Your code replaces the prompt:  `...`
# 
# 
# 

# In[ ]:


def square_wave(f,K):

    # initialize our square wave q to be all zeros
    q = np.zeros((16000,))

    # create an array of linearly spaced time values
    t = np.linspace(0, 1, num=16000, endpoint=False) 


    # loop over all desired values of k
    # add each sinusoid to q
    ...

    # return square wave q
    return q

# plot a square wave
plt.plot(square_wave(440,200))
# show just the first 100 values
plt.xlim(0,100)


# In[ ]:


grader.check("task1-square")


# Listen to a $200$-term square wave approximation with fundamental frequency $440$. In electronic music, square wave synthesizers are often used to provide a hollow, distorted sound.

# In[ ]:


ipd.Audio(square_wave(440,200), rate=16000)


# **Task 2: Sum of Harmonic Sinusoids** 
# 
# The square wave is just one waveform the can be constructed using a sum of sinusoids. In general, any periodic waveform $w(t)$ can be approximated using the following equation: 
# 
# $$ w(t) \approx \sum_{k=0}^{K-1}  A_k sin(2 \pi (k+1) f t)$$
# 
# Where $A_k$ is an amplitude value that is different for each term. Your task is to make a function that computes $w(t)$ given a fundamental frequency $f$ and a list of amplitude values $A_k$. The number of terms $K$ will be inferred by the length of the list of amplitudes.
# 
# Write python code to do the following:
# 
# * Define a function called ``waveform`` which accepts as input a fundamental frequency `f`, and a list of amplitudes `A`.
# * First, initialize an empty array `w` of $16000$ zeros, as in previous tasks.
# * Then create an array `t` of $16000$ linearly-spaced time values, as in previous tasks.
# * Loop through all values of $k$, adding on the appropriate sinusoid.
# * Return the final waveform `w`
# 
# 
# Your code replaces the prompt:  `...`
# 

# In[ ]:


...

# plot a square wave with the first 3 nonzero terms
plt.plot(waveform(440,[1,0,(1/3),0,(1/5)]))
# show just the first 100 values
plt.xlim(0,100);


# In[ ]:


grader.check("task2-sinesum")


# **Task 3: Musical Sequence** 
# 
# Your final task involves using the waveform function you made to generate sequences of musical notes. 
# 
# Music software often uses a protocol called MIDI (Musical Instrument Digital Interface) to format messages related to music. MIDI uses a numbering scheme for the notes on a piano, so that every note has a unique pitch value. Each pitch $p$ is an integer in $[0,127]$. The following equation shows how to compute the fundamental frequency $f$ for a note with MIDI pitch value $p$:
# 
# $$ f = 440 * 2^{(p - 69) / 12} $$
# 
# In this problem, you will complete a function called `music_sequence` which creates a waveform containing a sequence of musical notes. The input to the function will be a list of MIDI pitch values.
# 
# Write python code to do the following:
# 
# * Complete the function called ``music_sequence`` which accepts as input a list of MIDI pitch values `P`.
# * Loop through all the pitch values in list `P`
# * For each pitch $p$, compute its frequency $f$ using the equation above
# * Using the computed frequency $f$ and the provided amplitude list `A`, generate a waveform using the `waveform` function from the previous task 
# * Append each waveform to the sequence list, which has been initialized for you
# * The provided code concatenates the sequence of notes and returns the final waveform
# 
# 
# Your code replaces the prompt:  `...`
# 

# In[ ]:


def music_sequence(P):

    # initialize a empty list for our sequence of notes
    sequence = []
    # use this list of amplitudes A when generating waveforms
    # it gives the notes an organ-like sound
    A = [1, 0, 0, (1/4), 0, 0, 0, (1/8), 0, 0, 0, (1/12)]

    # loop over all pitches in P and compute each frequency
    # using the frequency and list A, generate a waveform
    # append the waveform to the sequence list
    ...

    return np.concatenate(sequence, axis=0)

# listen to the music sequence
ipd.Audio(music_sequence([60,62,64,65,67,69,71,72]), rate=16000)


# In[ ]:


grader.check("task3-musical-scale")

