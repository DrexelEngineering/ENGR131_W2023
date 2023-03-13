#!/usr/bin/env python
# coding: utf-8

# # 💻 Activity 3: Determining the Superbowl Proposition Winner
# 
# We made a Superbowl proposition game for ENGR131 now it is time to determine the winner. The submission are in an excel file your tasks is to calculate the winner. We have provided you a list with the correct outcomes from the superbowl. 

# ## Step 1: Load the File
# 
# The file is named "Super Bowl Propositions.xls" load the file into a Pandas DataFrame. 
# 
# Save it as a variable df

# In[1]:


get_ipython().system('pip install openpyxl')


# In[2]:


# import pandas
import pandas as pd

# use the pd.read_excel to load the excel file
...


# In[3]:


# import pandas
import pandas as pd

# use the pd.read_excel to load the excel file
df = pd.read_excel('Super Bowl Propositions.xlsx')


# Use `df.head()` to look at the first few lines of the DataFrame

# In[4]:


...


# In[5]:


df.head()


# Now we want to get the strings for each of the questions

# In[6]:


# We want to extract the question names
# To do this we want all the column heading that have a ? in the string

# We can start by creating a empty list called questions
...

# now we want to loop around all of the row heading
# You can build a loop that loops around each column name
# The column name can be obtained from df.columns
# save each heading in a temporary variable column
for ... in ...:
    
    # Now we want to check if the variable column is a questions
    # To do this we want to use an if statement that sees if a "?" is in the string
    if ... in ...:
        
        # if this is true we want to add the heading to the list
        # this can be done using the list method .append(obj)
        # the obj is the local variable in the list
        ...

# if you want to check this you can print the columns        
...    


# In[ ]:


# We want to extract the question names
# To do this we want all the column heading that have a ? in the string

# We can start by creating a empty list called questions
questions = []

# now we want to loop around all of the row heading
# You can build a loop that loops around each column name
# The column name can be obtained from df.columns
# save each heading in a temporary variable column
for column in df.columns:
    
    # Now we want to check if the variable column is a questions
    # To do this we want to use an if statement that sees if a "?" is in the string
    if "?" in column:
        
        # if this is true we want to add the heading to the list
        # this can be done using the list method .append(obj)
        # the obj is the local variable in the list
        questions.append(column)

# if you want to check this you can print the columns        
print(questions)    


# Now we want to calculate the score. We have provided comments to help you complete this task.

# In[5]:


Correct_Answers = ['Under 2 minutes 2 seconds (worth 1 point)', #1
 'Tails (worth 1 point)', #2
 'Yes (worth 1 point)', #3
 'Yes (worth 1 point)', #4
 'Run (worth 2 points)', #5
 'Yes (worth 2 points)', #6
 'Eagles (worth 2 points)', #7
 'Chiefs (worth 2 points)', #8
 'Jalen Hurts (worth 2 points)', #9
 'Chiefs (worth 2 points)', #10
 'Touchdown (worth 1 point)', #11
 'Over 24.5 (worth 2 points)', #12
 'Eagles (worth 2 points)', #13
 'No (worth 2 points)', #14
 'No (worth 2 points)', #15
 'Eagles (worth 2 points)', #16
 'Over 9.5 (worth 2 points)', #17
 'Other (worth 2 points)', #18
 'Under 2.5 (worth 1 point)', #19
 'Under 281.5 (worth 2 points)', #20
 'Over 241.5 (worth 2 points)', #21
 'Over 78.5 (worth 2 points', #22
 'Over 72.5 (worth 2 points)', #23
 'Over 6.5 (worth 2 points)', #24
 'Fourth Quarter (worth 2 points)', #25
 'Third Quarter (worth 2 points)', #26
 'Yes (worth 2 points)', #27
 'Eagles (worth 2 points)', #28
 '3 (worth 2 points)', #29
 'No (worth 3 points)', #30
 'No (worth 1 point)', #31
 'Odd (worth 1 point)', #32
 'Purple (worth 6 points)', #33
 'Odd (worth 2 points)', #34
 'Over 50.5 (worth 3 points)', #35
 'Patrick Mahomes (worth 1 point)', #36
 'xxx'] #37

points = [1, #1 'Under 2 minutes 2 seconds (worth 1 point)'
 1, #2 'Tails (worth 1 point)'
 1, #3  Yes (worth 1 point)
 1, #4 Yes (worth 1 point)
 2, #5 Run (worth 2 points)
 2, #6 Yes (worth 2 points)
 2, #7 Eagles (worth 2 points)
 2, #8 Chiefs (worth 2 points)
 2, #9 Jalen Hurts (worth 2 points)
 2, # 10 Chiefs (worth 2 points)
 1, # 11 Touchdown (worth 1 point)
 2, #12 Over 24.5 (worth 2 points)
 2, #13 Eagles (worth 2 points)
 2, #14 No (worth 2 points)
 2, #15 No (worth 2 points)
 2, #16 Eagles (worth 2 points)
 2, #17 Over 9.5 (worth 2 points)
 2, #18 Other (worth 2 points)
 1, #19 Under 2.5 (worth 1 point)
 2, #20 Under 281.5 (worth 2 points)
 2, #21 Over 241.5 (worth 2 points)
 2, #22 Over 78.5 (worth 2 points
 2, #23 Over 72.5 (worth 2 points)
 2, #24 Over 6.5 (worth 2 points)
 2, #25 Fourth Quarter (worth 2 points)
 2, #26 Third Quarter (worth 2 points)
 2, #27 Yes (worth 2 points)
 2, #28 Eagles (worth 2 points)
 2, #29 3 (worth 2 points)
 3, #30 No (worth 3 points)
 1, #31 No (worth 1 point)
 1, #32 Odd (worth 1 point)
 6, #33 Purple (worth 6 points)
 2, #34 Odd (worth 2 points)
 3, #35 Over 50.5 (worth 3 points)
 1, # Patrick Mahomes (worth 1 point)
 250]


# In[6]:


# make a list to keep the scores


# create a loop that goes through each row
# to turn the df into a row iterator use the .iterrows() method
# You can select just the questions by indexing the dataframe with the list
# example: df[questions].iterrows()
# note iterrows returns a tuple with the first value being the index and the second being the row
for ..., ... in ...:
    
    # initiate a score for the person
    ...
    
    # Since we have the heading for all of the questions we can loop around the list
    # The correct answers are order
    # we also have an ordered list that shows how much each question is worth
    # make a loop around the questions that uses enumerate
    # enumerate will let you get the index number and the contents
    for ..., ... in ...:
        
        # check if the the person got the correct answer
        if ... == ...:
            
            # add the number of points they earned for the correct response
            ...
            
    # append the score to the list of scores
    ...
    
# add the score to the original dataframe using df['scores'] = scores
 
            


# In[ ]:


# make a list to keep the scores
scores = []

# create a loop that goes through each row
# to turn the df into a row iterator use the .iterrows() method
# You can select just the questions by indexing the dataframe with the list
# example: df[questions].iterrows()
# note iterrows returns a tuple with the first value being the index and the second being the row
for ind, row in df[questions].iterrows():
    
    # initiate a score for the person
    score = 0
    
    # Since we have the heading for all of the questions we can loop around the list
    # The correct answers are order
    # we also have an ordered list that shows how much each question is worth
    # make a loop around the questions that uses enumerate
    # enumerate will let you get the index number and the contents
    for i, question in enumerate(row):
        
        # check if the the person got the correct answer
        if question == Correct_Answers[i]:
            
            # add the number of points they earned for the correct response
            score += points[i]
            
    # append the score to the list of scores
    scores.append(score)
    
# add the score to the original dataframe using df['scores'] = scores
df['scores'] = scores    
            


# Now we can find the winner.

# In[35]:


# use df['scores'] and convert to numpy using .to_numpy() method
# use the .argsort() method to find the sorted index
# then flip the array using [::-1] 
...

# Use df.iloc[ind[0]] to get the row of winner.
# Then index the dataframe to get the winners name
...


# In[ ]:


# use df['scores'] and convert to numpy using .to_numpy() method
# use the .argsort() method to find the sorted index
# then flip the array using [::-1] 
ind = df['scores'].to_numpy().argsort()[::-1]

# Use df.iloc[ind[0]] to get the row of winner.
# Then index the dataframe to get the winners name
df.iloc[ind[0]]['Name']

