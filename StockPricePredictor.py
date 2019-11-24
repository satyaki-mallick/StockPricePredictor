#!/usr/bin/env python
# coding: utf-8

# API key for AlphaVantage -
# UQSM8TNHTJPRG0IK

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NSE:%20RELIANCE&apikey=UQSM8TNHTJPRG0IK

# TCS Stock Price - https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NSE:TCS&apikey=UQSM8TNHTJPRG0IK

# RELIANCE Stock Price - https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NSE:RELIANCE&apikey=UQSM8TNHTJPRG0IK

# Optional Param - outputsize=compact. Strings compact and full

# In[48]:


import json
import requests
import pandas as pd


# In[8]:


resp = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NSE:RELIANCE&apikey=UQSM8TNHTJPRG0IK')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))


# In[9]:


print(resp.text)


# In[38]:


json_string = resp.text
parsed_json = json.loads(json_string)

parsed_json["Time Series (Daily)"]


# In[46]:


everyday_data = parsed_json["Time Series (Daily)"]
size = 0
open_price_list = []
close_price_list = []
volume_list = []
for day_data in everyday_data:
    size += 1
    open_price_list.append(everyday_data[day_data]["1. open"])
    close_price_list.append(everyday_data[day_data]["4. close"])
    volume_list.append(everyday_data[day_data]["5. volume"])


# In[51]:


df = pd.DataFrame(list(zip(open_price_list, close_price_list, volume_list)), 
               columns =['OPEN', 'CLOSE', 'VOLUME']) 


# In[52]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




