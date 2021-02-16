#!/usr/bin/env python
# coding: utf-8

# In[15]:


from preprocessing import preprocessing
from OC import option_chain
from req import ex_date, keys_ce,keys_pe,nc
from post_processing import post_processing
import numpy as np
import os
#from intro_to_flask import app


# In[16]:



#CCS


# In[17]:


from flask import Flask, render_template
import pickle
import requests
import json
from flask import Response
from io import StringIO


# In[18]:


#pickle.dump(CCS, open('model.pkl','wb'))


# In[19]:


#model = pickle.load(open('model.pkl','rb'))
#model


# In[20]:


app = Flask(__name__,template_folder='template')
@app.route('/')
def home():
    return render_template('index.html')
    

    


# In[21]:


@app.route('/CCS', methods= ['GET'] )
def CCS2():
    CCS = post_processing.call_calender_spread()
    #call_calende_spread= (model)
    #output = StringIO()
    #call_calende_spread.to_csv(output)
    return render_template('simple.html',  tables=[CCS.to_html(classes='data', header="true")])


# In[22]:


@app.route('/PCS', methods= ['GET'] )
def PCS():
    PCS = post_processing.put_calender_spread()
    #call_calende_spread= (model)
    #output = StringIO()
    #call_calende_spread.to_csv(output)
    return render_template('simple_put.html',  tables=[PCS.to_html(classes='data', header="true")])


# In[23]:


@app.route('/VCS', methods= ['GET'] )
def VCS():
    VCS = post_processing.verticle_call_spread()
    #call_calende_spread= (model)
    #output = StringIO()
    #call_calende_spread.to_csv(output)
    return render_template('simple_VCS.html',  tables=[VCS.to_html(classes='data', header="true")])


# In[24]:


@app.route('/VPS', methods= ['GET'] )
def VPS():
    VPS = post_processing.verticle_put_spread()
    #call_calende_spread= (model)
    #output = StringIO()
    #call_calende_spread.to_csv(output)
    return render_template('simple_VPS.html',  tables=[VPS.to_html(classes='data', header="true")])


# In[25]:


if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)


# In[ ]:




