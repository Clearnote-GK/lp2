#!/usr/bin/env python
# coding: utf-8

# In[55]:


x = 2
lr = 0.01
precision =0.000001
previous_step_size =1
max_iter = 10000
iters= 0
gf=lambda x: (x+3)**2


# In[56]:


import matplotlib.pyplot as plt


# In[57]:


gd=[]


# In[58]:


while precision< previous_step_size and iters < max_iter:
    prev=x
    x = x-lr*gf(prev)
    previous_step_size = abs(x-prev)
    iters += 1
    print('iteration:',iters,'Value',x)
    gd.append(x)


# In[ ]:





# In[59]:


print('local minima', x)


# In[60]:


plt.plot(gd)


# In[ ]:




