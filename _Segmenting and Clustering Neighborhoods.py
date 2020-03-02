#!/usr/bin/env python
# coding: utf-8

# ### Importing the Librares

# In[70]:


import pandas as pd
import numpy as np


# ### Creating the Canada Neighbourhood  DataFrame, Cleanning and Groupping

# In[169]:


df_canada_raw=pd.read_html('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')

df=pd.DataFrame(df_canada_raw[0])


## Dropping df.Borough=='Not assigned'

df.drop(df[df.Borough=='Not assigned'].index,inplace=True)

## gropping 'Borough' wherer Neighbourhood =='Not assigned'

df['Neighbourhood']= np.where (df['Neighbourhood']=='Not assigned',df['Borough'],df['Neighbourhood'])
 
##gropping post code

df1=df.groupby(['Postcode','Borough']).agg(lambda col: ','.join(col))

##Reindexing

df=df1.reset_index()

df


# In[168]:


df.shape


# In[ ]:





# In[ ]:





# In[ ]:




