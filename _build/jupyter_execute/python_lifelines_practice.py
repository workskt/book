#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
with open('clinical.tsv') as f:
    header, *lines = f.readlines()
    data = {}
    for line in lines:
        cols = line.strip().split('\t')
        if cols[15] == 'Alive' and re.search(r'\d+', cols[47]): #cols[47] days_to_last_follow_up
            data.setdefault(cols[1], f'{int(cols[47]) // 30}\t0') 
        elif cols[15] == 'Dead' and re.search(r'\d+', cols[9]): #cols[9] days_to_death
            data.setdefault(cols[1], f'{int(cols[9]) // 30}\t1')
        else:
            print(line) #欠損値があれば出力する
    
with open('clinical_edited.tsv', 'w') as out:
    print('T', 'E', sep='\t', file=out)
    for value in data.values():
        print(value, file=out)  


# In[2]:


import pandas as pd
df = pd.read_table('clinical_edited.tsv')


# In[3]:


df


# In[4]:


T = df['T']
E = df['E']


# In[5]:


from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()
kmf.fit(T, event_observed=E, label='lung')
kmf.survival_function_
kmf.plot_survival_function()


# In[6]:


with open('clinical.tsv') as f:
    header, *lines = f.readlines()
    data = {}
    for line in lines:
        cols = line.strip().split('\t')
        if cols[15] == 'Alive' and re.search(r'\d+', cols[47]): #cols[47] days_to_last_follow_up
            if match := re.match('Stage (\w+)', cols[26]):
                stage = match.group(1)
                if stage == 'I' or stage == 'IA' or stage == 'IB' or stage == 'II' or stage == 'IIA' or stage == 'IIB':
                    data.setdefault(cols[1], f'{int(cols[47]) // 30}\t0\tstageI-II') 
                else:
                    data.setdefault(cols[1], f'{int(cols[47]) // 30}\t0\tstageIII-IV') 
        elif cols[15] == 'Dead' and re.search(r'\d+', cols[9]): #cols[9] days_to_death
             if match := re.match('Stage (\w+)', cols[26]):
                stage = match.group(1)
                if stage == 'I' or stage == 'IA' or stage == 'IB' or stage == 'II' or stage == 'IIA' or stage == 'IIB':
                    data.setdefault(cols[1], f'{int(cols[9]) // 30}\t1\tstageI-II') 
                else:
                    data.setdefault(cols[1], f'{int(cols[9]) // 30}\t1\tstageIII-IV') 
        else:
            print(line) #欠損値を出力
    
with open('clinical_group.tsv', 'w') as out:
    print('T', 'E', 'group', sep='\t', file=out)
    for value in data.values():
        print(value, file=out)  


# In[7]:


df = pd.read_table('clinical_group.tsv')


# In[8]:


df


# In[9]:


T12 = df.loc[df['group'] == 'stageI-II', 'T']
E12 = df.loc[df['group'] == 'stageI-II', 'E']

T34 = df.loc[df['group'] == 'stageIII-IV', 'T']
E34 = df.loc[df['group'] == 'stageIII-IV', 'E']


# In[10]:


E12


# In[11]:


from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()

kmf.fit(T12, event_observed=E12, label='stageI-II')
ax = kmf.plot()

kmf.fit(T34, event_observed=E34, label='stageIII-IV')
ax = kmf.plot()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[12]:


from lifelines.datasets import load_waltons
df = load_waltons()


# In[13]:


df


# In[14]:


T = df['T']
E = df['E']


# In[15]:


from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()
kmf.fit(T, event_observed=E)


# In[16]:


kmf.survival_function_
kmf.cumulative_density_
kmf.plot_survival_function()


# In[17]:


kmf.plot_cumulative_density()


# In[18]:


T


# In[19]:


E


# In[20]:


df


# In[21]:


groups = df['group']


# In[22]:


groups


# In[23]:


ix = (groups == 'miR-137')


# In[24]:


ix


# In[25]:


groups == 'miR-137'


# In[26]:


kmf.fit(df.loc[df['group'] == 'control', 'T'], df.loc[df['group'] == 'control', 'E'], label='control')
ax = kmf.plot()

kmf.fit(df.loc[df['group'] == 'miR-137', 'T'], df.loc[df['group'] == 'miR-137', 'E'], label='miR-137')
ax = kmf.plot(ax=ax)


# In[27]:


df.loc[df['E'] == 0]


# In[28]:


import pandas as pd


# In[29]:


df = pd.read_table('clinical.tsv')


# In[30]:


df


# In[31]:


Ta = df.loc[df['vital_status'] == 'Alive' , 'days_to_last_follow_up']


# In[32]:


Ta


# In[33]:


Td = df.loc[df['vital_status'] == 'Dead', 'days_to_death']


# In[34]:


Td


# In[35]:


T = pd.concat([Ta, Td])


# In[36]:


T


# In[37]:


df.loc[df['vital_status'] == 'Alive', 'vital_status'] = 0
df.loc[df['vital_status'] == 'Dead', 'vital_status'] = 1


# In[38]:


Ea = df.loc[df['vital_status'] == 0, 'vital_status']
Ed = df.loc[df['vital_status'] == 1, 'vital_status']


# In[39]:


Ea


# In[40]:


Ed


# In[41]:


E = pd.concat([Ea, Ed])


# In[42]:


E


# In[43]:


from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()
kmf.fit(T, event_observed = E)


# In[ ]:


T.to_csv('T.txt', sep='\t')


# In[ ]:


E.to_csv('E.txt', sep='\t')


# In[ ]:





# In[ ]:




