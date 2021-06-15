#!/usr/bin/env python
# coding: utf-8

# # Document contents
# Use this service to **get document contents** in **Saphety's Network**.

# ## Get a token
# Check more detail how to get a token in [Services overview](../../services-overview/notebooks/services-overview.ipynb)  

# In[1]:


# Set Environment
#Integration
server_base_adress = "doc-server-int.saphety.com/Doc.WebApi.Services"
#Quality
#server_base_adress = "doc-server-qa.saphety.com/Doc.WebApi.Services"
#Production
#server_base_adress = "doc-server.saphety.com/Doc.WebApi.Services"


# In[2]:


#Set authorization data
#username = 'username'
#password = 'request_password'

username = 'user_api_doc'
password = 'request_password'


# In[3]:


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


# ### Get document contents
# You can specify the following content you want to get:  
# **Document ID**  
# **Format Type**  
# - PDF
# - Original
# - Final
# - Signed
# - Ubl21

# In[20]:


service_url = "https://" + server_base_adress + "/api/Document/content"

# Search criteria data goes in payload as json
payload = {
  'DocumentId': 2833651,
  'Format': 'PDF'
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
# These two fields are truncated for better readability
json_response["Data"]["ContentDataBytes"] = json_response["Data"]["ContentDataBytes"][:100] + '...'
json_response["Data"]["ContentDataText"] = json_response["Data"]["ContentDataText"][:100] + '...'
print(json.dumps(json_response, indent=4))


# ### Streaming document contents
# You can get the document content immediately streamed to your HTTP Response

# In[22]:


# Get the serie Id from the previous serach service
documentId = '2833651'
formatType = 'PDF'
inLine = False
# Build the url
service_url = "https://" + server_base_adress + "/api/Streaming/Document/content/" + documentId + "/" + formatType + "/" + str(inLine)
# Indicate in header the authorization token
headers = { 'Authorization': 'bearer ' + token }
# Use PUT to send the request
response = requests.request("GET", service_url, headers=headers)
print (response)
# Serializethe response
content = response.text
# The document was truncated for better readability
print(content[:500] + '...')

