#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests

from bs4 import BeautifulSoup


# In[4]:


url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"


# In[5]:


response = requests.get(url)


# In[6]:


soup = BeautifulSoup(response.text, 'html.parser')


# In[7]:


soup


# In[8]:


#extracting the table.

tables=soup.find('table',class_='wikitable')


# In[9]:


tables


# In[11]:


for i in tables.find_all('tr')[2:]:
    print(i)


# In[12]:


states=[]

for i in tables.find_all('tr')[2:]:
    states.append(i.find('a').text)


# In[13]:


states


# In[ ]:




