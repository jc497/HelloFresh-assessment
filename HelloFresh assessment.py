#!/usr/bin/env python
# coding: utf-8

# In[206]:


import pandas as pd
import json
import re


# Q2

# In[179]:


df = pd.read_json('recipes.json', lines = True)
search_term = 'chilies'
pattern = re.compile(r'\b{}\w*\b'.format(search_term), re.IGNORECASE)
df_extracted = df[df['ingredients'].str.contains(pattern)]
df_extracted


# Q3

# In[201]:


#remove PT in both columns
df_extracted['cookTime'] = df_extracted['cookTime'].str.replace('PT', '')
df_extracted['prepTime'] = df_extracted['prepTime'].str.replace('PT', '')

# divide hours and minutes for cookTime and prepTime
df_extracted['cookTime_H'] = df_extracted['cookTime'].str.extract(r'(\d+)H', expand=False).fillna(0).astype(int)
df_extracted['cookTime_M'] = df_extracted['cookTime'].str.extract(r'(\d+)M', expand=False).fillna(0).astype(int)
df_extracted['prepTime_M'] = df_extracted['prepTime'].str.extract(r'(\d+)M', expand=False).fillna(0).astype(int)

# add the totalTime to the dataframe
df_extracted['totalTime'] = df_extracted['cookTime_H']*60 + df_extracted['cookTime_M'] + df_extracted['prepTime_M']

# add the 'difficulty' field to the dataframe
def difficulty_level(totalTime):
    if totalTime > 60:
        return 'Hard'
    if totalTime <= 60 and totalTime > 30:
        return 'Medium'
    if totalTime < 30 and totalTime > 0:
        return 'Easy'
    else:
        return 'Unknown'

df_extracted['difficulty'] = df_extracted['totalTime'].apply(difficulty_level)


# Q4

# In[204]:


df_extracted.to_csv('result.csv', index=False)

