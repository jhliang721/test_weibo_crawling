#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
res = requests.get('https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26q%3D%23%E9%A6%99%E5%A5%88%E5%84%BF%23&page_type=searchall&page=3')
jd = res.json()


# In[6]:


import pandas
articles = [rec['mblog'] for rec in jd['data']['cards'] if rec.get('mblog')]
df = pandas.DataFrame(articles)


# In[39]:


df['text']


# In[50]:


import requests
articles = []
for i in range(1,10):
    res = requests.get('https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26q%3D%23%E9%A6%99%E5%A5%88%E5%84%BF%23&page_type=searchall&page={}'.format(i))
    jd = res.json()
    articles.extend( [rec['mblog'] for rec in jd['data']['cards'] if rec.get('mblog')] )

df = pandas.DataFrame(articles)


# In[51]:


len(df)


# In[61]:


df.to_excel(r'H:\caroltest.xlsx',index=False)


# In[ ]:




