#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

data= "https://en.wikipedia.org/wiki/List_of_active_Indian_military_aircraft"
response = requests.get(data)


# In[2]:


response.text


# In[3]:


from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text,'html.parser')


# In[4]:


soup


# In[5]:


tables=soup.find('table',class_='wikitable')


# In[6]:


tables


# In[7]:


fighters={}

for row in tables.find_all('tr')[2:]:
    desc = []
    key = row.find_all('td')[0].text
        
    for i in row.find_all('td')[1:]:
        desc.append(i.text.replace('\n', ''))
        
    fighters[key] = desc


# In[8]:


fighters


# In[9]:


import pandas as pd

df = pd.DataFrame([fighters])

csv_file_path = 'fighters.csv'

df.to_csv(csv_file_path, index=False)


# In[ ]:




