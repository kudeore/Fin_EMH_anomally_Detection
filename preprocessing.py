#!/usr/bin/env python
# coding: utf-8

# In[4]:


from OC import option_chain
import pickle


# In[5]:


page = pickle.load(open('page.pkl','rb'))


# In[6]:


from req import ex_date, keys_ce,keys_pe


# In[7]:


class preprocessing: 
    
    def get_values(ex_date):
        values = []
        for i in ex_date: 
            value= option_chain.get_ce_data(i, page)
            values.append(value)
        return values
    
    def get_values_pe(ex_date):
        values = []
        for i in ex_date: 
            value= option_chain.get_pe_data(i, page)
            values.append(value)
        return values
    
    def get_dict_ce(keys_ce, values):
        dict_ce ={}
        for i in range(len(keys_ce)):
            dict_ce[keys_ce[i]] = values[i]
        return dict_ce
    
    def get_dict_pe(keys_pe, values):
        dict_pe ={}
        for i in range(len(keys_pe)):
            dict_pe[keys_pe[i]] = values[i]
        return dict_pe
        
        
        


# In[8]:


values = preprocessing.get_values(ex_date=ex_date)
values_pe = preprocessing.get_values_pe(ex_date=ex_date)


# In[9]:


ce= preprocessing.get_dict_ce(keys_ce=keys_ce, values=values)


# In[10]:


pe= preprocessing.get_dict_pe(keys_pe=keys_pe, values=values_pe)


# In[ ]:




