#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import python libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv("D:\Machine Learning dataset\googleplaystore.csv",encoding='unicode_escape')


# In[3]:


df.shape


# In[4]:


df.info()


# In[5]:


pd.isnull(df).sum()


# In[6]:


df.dropna(inplace=True)


# In[7]:


pd.isnull(df).sum()


# In[8]:


df.info()


# In[9]:


df.rename(columns={'Installs':'Download','Genres':'Generation'})


# In[10]:


df.shape


# In[11]:


df.columns


# In[12]:


df.groupby(['App'],as_index=False)['Category'].sum().sort_values(by='Category',ascending=True)


# In[13]:


df.groupby(['App'],as_index=False)['Rating'].sum().sort_values(by='Rating',ascending=True)


# In[14]:


df.groupby(['App'],as_index=False)['Reviews'].sum().sort_values(by='Reviews',ascending=True)


# In[15]:


df.groupby(['App'],as_index=False)['Installs'].sum().sort_values(by='Installs',ascending=True)


# In[45]:


ax = sns.countplot(x='Android Ver',data=df)

sns.set(rc={'figure.figsize':(40,25)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[17]:


df.groupby(['Android Ver'],as_index=False)['Last Updated'].sum().sort_values(by='Last Updated',ascending=False)


# In[18]:


foo = pd.DataFrame(columns =['Android Ver','Last Updated'])
for i in range(5):
    bar = np.random.normal(i,2,10)
    for j,b in enumerate(bar):#enumerate()a built-in function in python that allows you to keep track of the number of iterations 
        foo.loc[i*10+j] = ['no'+str(i),b]


# In[19]:


result = foo.explode('Android Ver','Last Updated').reset_index(drop=True)
result = result.assign(Names=result['Android Ver'].astype('category'),Values=result['Last Updated'].astype(np.float32))

sns.set(rc={'figure.figsize':(19,7)})
sns_plot = sns.violinplot(x='Android Ver', y='Last Updated', data=result)


# In[20]:


x = sns.countplot(x='Content Rating',data=df)

sns.set(rc={'figure.figsize':(29,17)})
for bars in x.containers:
    ax.bar_label(bars)


# In[21]:


df.groupby(['Content Rating'],as_index=False)['Genres'].sum().sort_values(by='Genres',ascending=True)


# In[22]:


foo = pd.DataFrame(columns =['Content Rating','Genres'])
for i in range(5):
    bar = np.random.normal(i,2,10)
    for j,b in enumerate(bar):#enumerate()a built-in function in python that allows you to keep track of the number of iterations 
        foo.loc[i*10+j] = ['no'+str(i),b]


# In[23]:


result = foo.explode('Content Rating','Genres').reset_index(drop=True)
result = result.assign(Names=result['Content Rating'].astype('category'),Values=result['Genres'].astype(np.float32))

sns_plot = sns.violinplot(x='Content Rating', y='Genres', data=result)


# In[46]:


rc = sns.countplot(x='Price',data=df)

sns.set(rc={'figure.figsize':(40,25)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[25]:


df.groupby(['Price'],as_index=False)['Genres'].sum().sort_values(by='Genres',ascending=True)


# In[26]:


foo = pd.DataFrame(columns =['Price','Genres'])
for i in range(5):
    bar = np.random.normal(i,2,10)
    for j,b in enumerate(bar):#enumerate()a built-in function in python that allows you to keep track of the number of iterations 
        foo.loc[i*10+j] = ['no'+str(i),b]


# In[27]:


result = foo.explode('Price','Genres')#.reset_index(drop=True)
result = result.assign(Names=result['Price'].astype('category'),Values=result['Genres'].astype(np.float32))

# sns.set(rc={'figure.figsize':(19,7)})
sns_plot = sns.violinplot(x='Price', y='Genres', data=result)


# In[28]:


df.groupby(['App'],as_index=False)['Price'].sum().sort_values(by='Price',ascending=True)


# In[29]:


foo = pd.DataFrame(columns =['App','Price'])
for i in range(5):
    bar = np.random.normal(i,2,10)
    for j,b in enumerate(bar):#enumerate()a built-in function in python that allows you to keep track of the number of iterations 
        foo.loc[i*10+j] = ['no'+str(i),b]


# In[30]:


result = foo.explode('App','Price').reset_index(drop=True)
result = result.assign(Names=result['App'].astype('category'),Values=result['Price'].astype(np.float32))

sns.set(rc={'figure.figsize':(19,7)})
sns_plot = sns.violinplot(x='App', y='Price', data=result)


# In[31]:


jk = sns.countplot(x='Installs',data=df)
sns.set(rc={'figure.figsize':(23,9)})
# for bars in jk.containers:
#     jk.bar_label(bars)


# In[32]:


# df.groupby(['Installs'],as_index=False)['Type'].sum().sort_values(by='Type',ascending=False)


# In[33]:


foo = pd.DataFrame(columns =['Installs','Type'])
for i in range(19):
    bar = np.random.normal(i,2,10)
    for j,b in enumerate(bar):#enumerate()a built-in function in python that allows you to keep track of the number of iterations 
        foo.loc[i*10+j] = ['no'+str(i),b]


# In[34]:


result = foo.explode('Type').reset_index(drop=True)
result = result.assign(Names=result['Installs'].astype('category'),Values=result['Type'].astype(np.float32))

sns.set(rc={'figure.figsize':(20,7)})
sns_plot = sns.violinplot(x='Installs', y='Type', data=result)


# In[35]:


jk = sns.countplot(x='Rating',data=df)

sns.set(rc={'figure.figsize':(19,5)})
for bars in jk.containers:
    jk.bar_label(bars)


# In[36]:


# df.groupby(['Rating'],as_index=False)['Reviews'].sum().sort_values(by='Reviews',ascending=False)


# In[37]:


playdata = df.groupby(['Rating'],as_index=False)['Reviews'].sum().sort_values(by='Reviews',ascending=True).head()

sns.set(rc={'figure.figsize':(40,5)})
sns.barplot(data=playdata,x='Rating',y='Reviews')


# In[38]:


foo = pd.DataFrame(columns =['Rating','Reviews'])
for i in range(19):
    bar = np.random.normal(i,2,10)
    for j,b in enumerate(bar):#enumerate()a built-in function in python that allows you to keep track of the number of iterations 
        foo.loc[i*10+j] = ['no'+str(i),b]


# In[39]:


result = foo.explode('Rating','Reviews').reset_index(drop=True)
result = result.assign(Names=result['Rating'].astype('category'),Values=result['Reviews'].astype(np.float32))

sns.set(rc={'figure.figsize':(20,7)})
sns_plot = sns.violinplot(x='Rating', y='Reviews', data=result)


# In[40]:


df.groupby(['Android Ver'],as_index=False)['Current Ver'].sum().sort_values(by='Current Ver',ascending=True).head(7)


# In[42]:


foo = pd.DataFrame(columns =['Android Ver','Current Ver'])
for i in range(19):
    bar = np.random.normal(i,2,10)
    for j,b in enumerate(bar):#enumerate()a built-in function in python that allows you to keep track of the number of iterations 
        foo.loc[i*10+j] = ['no'+str(i),b]


# In[43]:


result = foo.explode('Android Ver','Current Ver')#.reset_index(drop=True)
result = result.assign(Names=result['Android Ver'].astype('category'),Values=result['Current Ver'].astype(np.float32))

sns.set(rc={'figure.figsize':(20,7)})
sns_plot = sns.violinplot(x='Android Ver', y='Current Ver', data=result)


# In[ ]:





# In[ ]:





# In[ ]:




