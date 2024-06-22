#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


# In[8]:


df = pd.read_excel(r"D:\Users\juli_\Desktop\wages_by_education.xlsx")


# In[9]:


df= df.sample(frac=1)


# In[10]:


df


# In[22]:


print(df.columns)


# In[26]:


columns_to_plot = {
    'White': 'white_bachelors_degree',
    'Black': 'black_bachelors_degree',
    'Hispanic': 'hispanic_bachelors_degree'
}


# In[29]:


fig, ax = plt.subplots()
for race, column in columns_to_plot.items():
    race_data = df[['year', column]].dropna()
    if race == 'White':
        color = 'green'
    elif race == 'Black':
        color = 'red'
    elif race == 'Hispanic':
        color = 'blue'
    ax.scatter(race_data['year'], race_data[column], label=race, color=color, s=30)

legend.get_frame().set_facecolor('white')
legend.get_frame().set_edgecolor('black')
legend.get_frame().set_edgecolor('hispanic')


# In[28]:


ax.set_title('Bachelors Degree')
ax.set_xlabel('Year')
ax.set_ylabel('Income')


# In[19]:


columns_to_plot = {
    'Black': 'black_bachelors_degree',
    'Hispanic': 'hispanic_bachelors_degree'
}


# In[20]:


fig, ax = plt.subplots()

for race, column in columns_to_plot.items():
    race_data = df[['year', column]].dropna()
    color = 'red' if race == 'Black' else 'blue'
    ax.scatter(race_data['year'], race_data[column], label=race, color=color, s=30)
    
legend = ax.legend(title='', loc='upper left', frameon=True)
legend.get_frame().set_facecolor('white')
legend.get_frame().set_edgecolor('black')


# In[ ]:





# In[ ]:




