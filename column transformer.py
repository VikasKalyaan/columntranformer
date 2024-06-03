#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.compose import ColumnTransformer


# In[ ]:


transformer = ColumnTransformer(transformer=[
    ('tnf1',Simplimputer(),["Fever"]),
    ("tnf2",OrdinarlEncoder(categories = [['Mild','Strong']]),['cough']),
    ('tnf3',OneHotEncoder(sparse = False,drop='first'),['gender','city'])
],remainder = 'passthrough')

