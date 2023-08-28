#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[46]:


df = pd.read_table('irisdata.txt')


# In[47]:


df


# In[48]:


plt.figure()
sns.stripplot(x=df['target'], y=df['sepal length (cm)'])


# In[40]:


df


# In[42]:


import re
with open('clinical.tsv') as f:
    header, *lines = f.readlines()
    data = {}
    for line in lines:
        cols = line.strip().split('\t')
        data.setdefault(cols[1], line.strip()) #lineには改行コードが残っているので、strip()で除く
    
with open('clinical_unique.tsv', 'w') as out:
    print(header.strip(), file=out) #headerには改行コードが残っているので、strip()で除く
    for caseid, info in data.items():
        print(info, file=out)


# In[71]:


df = pd.read_table('clinical_unique.tsv')
df.columns


# In[74]:


plt.figure()
sns.stripplot(x=df['vital_status'], y=df['age_at_diagnosis'], hue = df['ajcc_pathologic_stage'], dodge=True, jitter=0.2)


# In[4]:


import pandas as pd
df = pd.read_table('jhu-usc.edu_LUSC.HumanMethylation450.4.lvl-3.TCGA-43-6771-01A-11D-1818-05.gdc_hg38.txt')


# In[5]:


df


# In[14]:


df.columns


# In[25]:


df.loc[df['Gene_Symbol'].str.contains('TP53;') ]


# In[ ]:




