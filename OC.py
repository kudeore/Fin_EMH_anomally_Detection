#!/usr/bin/env python
# coding: utf-8

# In[26]:


import requests
import json
import pandas as pd
import pickle


# In[45]:


page = pickle.load(open('page.pkl','rb'))


class option_chain:
    
     
    def get_ce_data(expiry_dt , page):
        ce_values = [data['CE'] for data in page['records']['data'] if "CE" in data and data['expiryDate'] == expiry_dt]
        #pe_values = [data['PE'] for data in page['records']['data'] if "PE" in data and data['expiryDate'] == expiry_dt]
        ce_dt = pd.DataFrame(ce_values).sort_values(['strikePrice'])
        #pe_dt = pd.DataFrame(pe_values).sort_values(['strikePrice'])
        return ce_dt
    
    
    def get_pe_data(expiry_dt , page):
        #ce_values = [data['CE'] for data in page['records']['data'] if "CE" in data and data['expiryDate'] == expiry_dt]
        pe_values = [data['PE'] for data in page['records']['data'] if "PE" in data and data['expiryDate'] == expiry_dt]
        #ce_dt = pd.DataFrame(ce_values).sort_values(['strikePrice'])
        pe_dt = pd.DataFrame(pe_values).sort_values(['strikePrice'])
        return pe_dt
    
    












