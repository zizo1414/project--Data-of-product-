#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_excel(r"C:\Users\zeyad\OneDrive\Desktop\Sales-Analysis\superstore_sales.xlsx")


# In[3]:


df


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# In[6]:


df.duplicated().sum()


# In[7]:


df.shape


# In[8]:


df.describe()


# In[9]:


df.loc[[1,2,3,4,55],['order_date','segment']]


# In[10]:


df.columns


# In[11]:


df[['order_date','ship_date','discount']]


# In[12]:


df.iloc[[1, 3, 4, 5], :]


# In[13]:


df.loc[[1,2,3,4,5,6,77], ['order_date']]


# In[14]:


sc=df.loc[df['state']=='New South Wales',['segment','country']]


# In[15]:


sc


# In[16]:


df.query("country=='Sweden' and sub_category== 'Art'").reset_index()


# In[17]:


df.dtypes


# In[18]:


z=df.columns[df.columns.str.contains('category')]


# In[19]:


df[z]


# In[20]:


df.iloc[[1,23,88,4,66,77],[3,4,7,8]]


# In[21]:


df['ship_mode'].nunique()


# In[22]:


df.notnull().sum(axis=0)


# In[23]:


df['order_date'].min()


# In[24]:


df['order_date'].max()


# In[25]:


df['month_year']=df['order_date'].dt.strftime('%Y-%m')


# In[26]:


df[['month_year']]


# In[27]:


df_trend=df.groupby('month_year')['sales'].sum().reset_index()


# In[28]:


x=df.groupby('month_year')['sales'].sum().index


# In[29]:


plt.figure(figsize=(15,8))
plt.plot(df['month_year'],df['sales'])
plt.xticks(rotation= 45)


# In[30]:


y=df.groupby('month_year')['sales'].sum().values


# graph show sales over month-year

# In[31]:


plt.figure(figsize=(18,8))
plt.xticks(rotation=45)
plt.plot(df_trend['month_year'],df_trend['sales'])


# In[ ]:





# In[32]:


df_trend


# In[33]:


plt.figure(figsize=(15,8))
plt.xticks(rotation='vertical')
plt.plot(x,y)


# In[34]:


product=df.groupby('product_name')['sales'].sum().reset_index()


# top ten products

# In[35]:


product.sort_values('sales',ascending=False).reset_index().head(10)


# In[36]:


df.groupby('product_name').sum()['sales']


# In[ ]:


df.dtypes


# In[44]:


df.groupby('category')[['sub_category','sales']].sum().reset_index()


# In[43]:


df.groupby(['product_name']).count()['country'].reset_index()


# In[66]:


selling_product=df.groupby(['product_name'])['sales'].sum().reset_index()


# In[56]:


df.dtypes


# In[54]:


df['order_date']=pd.to_datetime(df['order_date'])


# In[60]:


df['ship_date']=pd.to_datetime(df['ship_date'])


# In[67]:


pd.DataFrame(selling_product)


# In[71]:


plt.hist(df['ship_mode'])


# In[72]:


sns.histplot(df['ship_mode'])


# In[76]:


category_profit=df.groupby(['sub_category','category'])['profit'].sum().reset_index()


# In[80]:


category_profit.sort_values('profit',ascending=False).head(10).reset_index()


# In[87]:


df.groupby(['sub_category','category'])[['sales','profit']]\
.agg({'sales':'mean','profit':'sum'})\
.sort_values('profit',ascending=False)


# In[96]:


df['profit'].plot()


# In[99]:


sns.scatterplot(df,x=df['sales'],y=df['profit'],hue='category')


# In[108]:


df.loc[df['profit']!=0] 


# In[ ]:




