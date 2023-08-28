#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Counter
from collections import Counter
a = [0, 1, 2, 3, 3, 3, 4, 4]
print(Counter(a))
print(Counter(a).most_common(2))

b = 'This is a pen.'
print(Counter(b))


# In[2]:


#defaultditc() 存在しないキーの時にエラー出してくれないのでsetdefaultのほうがすき
from collections import defaultdict
a = defaultdict(int)
a['sample1'] = 100
print(a)

b = defaultdict(list)
b['sample1'].append(200)
print(b)

c = defaultdict(lambda: dict())
c['sample1']['TP53'] = 300
c['sample1']['KRAS'] = 500
print(c)


# In[3]:


#__sizeof__() 単位はbyte
a = 'test'
print(a.__sizeof__())


# In[ ]:




