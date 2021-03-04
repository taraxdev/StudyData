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
plt.hist(incomes)
plt.show()


# ## Moments

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt

vals = np.random.normal(10, 0.5, 10000)

plt.hist(vals, 50)
plt.show()


# In[4]:


np.mean(vals)


# In[5]:


np.var(vals)


# In[6]:


import scipy.stats as sp
sp.skew(vals)


# In[7]:


sp.kurtosis(vals)


# In[ ]:




