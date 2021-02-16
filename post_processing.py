#!/usr/bin/env python
# coding: utf-8

# In[1]:


from preprocessing import preprocessing
import pandas as pd
import req
import pickle


# In[3]:


page = pickle.load(open('page.pkl','rb'))


# In[4]:


from req import ex_date, keys_ce,keys_pe,nc,np


# In[5]:



values = preprocessing.get_values(ex_date=ex_date)
ce = preprocessing.get_dict_ce(keys_ce=keys_ce, values=values)
values_pe = preprocessing.get_values_pe(ex_date=ex_date)
pe = preprocessing.get_dict_pe(keys_pe=keys_pe, values=values_pe)


# In[6]:


class post_processing: 
    def call_calender_spread():
        #page= option_chain.page()
        #values = preprocessing.get_values(ex_date=ex_date)
        #ce = preprocessing.get_dict_ce(keys_ce=keys_ce, values=values)
        K = list(ce.values())
        N1=[]
        for m in range (0,6):
            for i in range (len(K[m])):
                for k in range(m+1,6):
                    for j in range(len(K[k])):
                        if K[m]["strikePrice"][i] == K[k]["strikePrice"][j] and  K[k]["askPrice"][j] - K[m]["bidprice"][i] < nc  and K[k]["askPrice"][j] >0:
                            x=[K[m]["strikePrice"][i] , K[k]["strikePrice"][j] ,K[m]["expiryDate"][i], K[k]["expiryDate"][j] ,
                               K[m]["bidprice"][i] ,  K[k]["askPrice"][j] ]
                            N1.append(x)
        N2 = pd.DataFrame(data=N1, columns= ("strike1_ce", "strike2_ce","expry1", "expry2","ce1", "ce2"))
        N2["diffrence"] = N2["ce2"]-N2["ce1"]
        N2 = N2.sort_values(by=["diffrence"], ascending=True)
        print('Call Calender Spread: ')
        return N2
    
    def put_calender_spread():
        #page= option_chain.page()
        #values_pe = preprocessing.get_values_pe(ex_date=ex_date)
       #pe = preprocessing.get_dict_pe(keys_pe=keys_pe, values=values_pe)
        K = list(pe.values())
        N3=[]
        for m in range (0,6):
            for i in range (len(K[m])):
                for k in range(m+1,6):
                    for j in range(len(K[k])):
                        if K[m]["strikePrice"][i] == K[k]["strikePrice"][j] and  K[k]["askPrice"][j] - K[m]["bidprice"][i] < nc  and K[k]["askPrice"][j] >0:
                            x=[K[m]["strikePrice"][i] , K[k]["strikePrice"][j] ,K[m]["expiryDate"][i], K[k]["expiryDate"][j] ,
                               K[m]["bidprice"][i] ,  K[k]["askPrice"][j] ]
                            N3.append(x)
        N4 = pd.DataFrame(data=N3, columns= ("strike1_pe", "strike2_pe","expry1", "expry2","pe1", "pe2"))
        N4["diffrence"] = N4["pe2"]-N4["pe1"]
        N4 = N4.sort_values(by=["diffrence"], ascending=True)
        #print('Call Calender Spread: ')
        return N4
    
    def verticle_call_spread():
        #page= option_chain.page()
        #values = preprocessing.get_values(ex_date=ex_date)
        #ce = preprocessing.get_dict_ce(keys_ce=keys_ce, values=values)
        K = list(ce.values())
        N5=[]
        for m in range (0,6):
            for i in range (len(K[m])):
                for k in range(m,6):
                    for j in range(len(K[k])):
                        if K[m]["strikePrice"][i] > K[k]["strikePrice"][j] and  K[k]["askPrice"][j] - K[m]["bidprice"][i] < np  and K[k]["askPrice"][j] >0:
                            x=[K[m]["strikePrice"][i] , K[k]["strikePrice"][j] ,K[m]["expiryDate"][i], K[k]["expiryDate"][j] ,
                               K[m]["bidprice"][i] ,  K[k]["askPrice"][j] ]
                            N5.append(x)
                            
        N6 = pd.DataFrame(data=N5, columns= ("strike1_ce", "strike2_ce","expry1", "expry2","ce1", "ce2"))
        N6["diffrence"] = N6["ce2"]-N6["ce1"]
        N6 = N6.sort_values(by=["diffrence"], ascending=True)
        #print('Verticle Call Spread: ')
        return N6
    
    def verticle_put_spread():
        N7=[]
        K = list(pe.values())
        for m in range (0,6):
            for i in range (len(K[m])):
                for k in range(m,6):
                    for j in range(len(K[k])):
                        if K[m]["strikePrice"][i] < K[k]["strikePrice"][j] and  K[k]["askPrice"][j] - K[m]["bidprice"][i] < np  and K[k]["askPrice"][j] >0:
                            x=[K[m]["strikePrice"][i] , K[k]["strikePrice"][j] ,K[m]["expiryDate"][i], K[k]["expiryDate"][j] ,
                               K[m]["bidprice"][i] ,  K[k]["askPrice"][j] ]
                            N7.append(x)
        N8 = pd.DataFrame(data=N7, columns= ("strike_pe", "strike_pe","expry1", "expry2","pe1", "pe2"))
        N8["diffrence"] = N8["pe2"]-N8["pe1"]
        N8 = N8.sort_values(by=["diffrence"], ascending=True)
        return N8







