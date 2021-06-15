#!/usr/bin/env python
# coding: utf-8

# # Document pull
# Use this service to **pull documents**.

# ## Get a token
# Check more detail how to get a token in [Services overview](../../services-overview/notebooks/services-overview.ipynb)  

# In[ ]:


# Set Environment
#Integration
server_base_adress = "doc-server-int.saphety.com/Doc.WebApi.Services"
#Quality
#server_base_adress = "doc-server-qa.saphety.com/Doc.WebApi.Services"
#Production
#server_base_adress = "doc-server.saphety.com/Doc.WebApi.Services"


# In[ ]:


#Set authorization data
#username = 'username'
#password = 'request_password'

username = 'user_api_doc'
password = 'request_password'


# In[28]:


## Get a JWT token from your username and password
import requests
import json

service_url = "https://" + server_base_adress + "/api/Account/token"

# Auhtentication data goes in payload as json
payload = {
      'Username': username,
      'Password': password
}
# Payload goes in json, serialize the payloal object to json
request_data=json.dumps(payload)
# Indicate in header that payload is json
headers = {
    'content-type': 'application/json'
    }
# POST request to get a token
response = requests.request("POST", service_url, data=request_data, headers=headers)
# Serializethe response
json_response = json.loads(response.text)
# Your token is at:
token = json_response["Data"];
print ('Your authorization token:' + token)


# ### About the restriction criteria
# You can specify the following restriction creteria:  
# - **SenderEntityCode**  
# Place here the Sender enity code
# - **DestinationEntityCode**  
# Place here the Destination enity code
# - **CreationDateStart**  
# Place here the creation date start range you want to search
# - **CreationDateEnd**   
# Place here the creation date end range you want to search
# - **DeliveredDateStart**  
# Place here the delivered date start range you want to search
# - **DeliveredDateEnd**  
# Place here the delivered date end range you want to search
# - **DeliveredStatus**  
# This field is **true** or **false**

# In[47]:


service_url = "https://" + server_base_adress + "/api/DocumentPull/OutboundShippments/search"

# Search criteria data goes in payload as json
payload = {
  'RestrictionCriteria': {
    'SenderEntityCode': 'PT507957547',
    'DestinationEntityCode': 'PT560333331',
    'CreationDateStart': '2021-06-13 00:00:00',
    'CreationDateEnd': '2021-06-16 00:00:00',
    'DeliveredStatus': False
  },
  'PageNumber': 0,
  'RowsPerPage': 20
}
# Payload goes in json, serialize the payloal object to json
request_data=json.dumps(payload)
# Indicate in header the authorization token
headers = {
    'content-type': 'application/json',
     'Authorization': 'bearer ' + token
    }
# POST request to get a token
response = requests.request("POST", service_url, data=request_data, headers=headers)
print (response)
# Serializethe response
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# ## Get document content by id
# To get the document content use the service: _**/api/DocumentPull/OutboundShippments/{id}**_  
# - **Id**  
# Id is the system identification for the document

# In[52]:


# Get the serie Id from the previous serach service
documentId = 'ac09853c-3cff-40af-865f-77192e9e3c81' 
# Build the url
service_url = "https://" + server_base_adress + "/api/DocumentPull/OutboundShippments/" + documentId
# Indicate in header the authorization token
headers = { 'Authorization': 'bearer ' + token }
# Use PUT to send the request
response = requests.request("GET", service_url, headers=headers)
print (response)
# Serializethe response
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# In[ ]:




