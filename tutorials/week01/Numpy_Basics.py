#!/usr/bin/env python
# coding: utf-8

# # Numpy Basics
# 

# In[2]:


import numpy as np


# ### Numpy Array Initialization

# In[19]:


a = np.array([1,2,3,4,5], dtype='int64')
print(a)
print(a.shape)
print(a.size)
print(a.dtype)


# In[4]:


b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print(b)
print(b.shape)
print(b.size)


# In[5]:


c = np.ones((2,2))
c


# In[6]:


d = np.zeros(c.shape)
d


# In[7]:


e = np.identity(3)
e


# In[20]:


f = np.linspace(0, 9, 20)
f


# ### Numpy Array Indexing

# In[9]:


print(b)


# In[10]:


print(b[0,0])
print(b[1,2])
print(b[2,4])


# In[11]:


print(b[:,0])
print(b[0,:])


# In[12]:


print(b[0,2:])
print(b[0,2:4])
print(b[0,2:-1])


# ## Statistics

# In[13]:


stats_array = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9], [10, 11, 12]])
stats_array


# In[14]:


print(np.min(stats_array))
print(np.max(stats_array))


# In[15]:


print(np.min(stats_array, axis=0))
print(np.max(stats_array, axis=1))


# In[16]:


print(np.sum(stats_array))
print(np.sum(stats_array, axis=0))
print(np.sum(stats_array, axis=1))


# ## Copying a Numpy Array

# In[17]:


a = np.array([1, 2, 3])
a


# In[18]:


b = a
b[2] = 10
print(a)
print(b)


# In[12]:


a = np.array([1, 2, 3])
c = a.copy()
c[2] = 10
print(a)
print(c)

