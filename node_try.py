#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pixiedust_node


# In[2]:


get_ipython().run_cell_magic('node', '', '\nconst SALES_TAX = 0.975\n\nconsole.log(SALES_TAX)')


# In[3]:


get_ipython().run_cell_magic('node', '', "\nfunction HelloPerson(name) {\n    console.log(`Hello, ${name}.`);\n}\nHelloPerson('Rome')")


# In[4]:


npm.install('axios')


# In[5]:


get_ipython().run_cell_magic('node', '', "const axios = require('axios');")


# In[6]:


get_ipython().run_cell_magic('node', '', "\naxios.get('https://api.github.com/users/ireneyap68').then(response => {\n    console.log(response.data)\n})")


# In[ ]:




