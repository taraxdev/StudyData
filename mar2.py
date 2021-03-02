#!/usr/bin/env python
# coding: utf-8

# In[38]:


# %matplotlib inline
import pandas as pd
import numpy as np
df = pd.read_csv("PastHires.csv")

df[["Previous employers","Hired"]][5:10]


# In[1]:


import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100,20,1000)
plt.hist(incomes,50)
plt.show()


# In[9]:


incomes.std()


# In[16]:


incomes.var()

