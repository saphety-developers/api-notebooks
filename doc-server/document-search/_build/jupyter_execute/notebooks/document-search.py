#!/usr/bin/env python
# coding: utf-8

# # Document search
# Use this service to **search documents** in **Saphety's Network**.

# ## Get a token
# Check more detail how to get a token in [Services overview](../../services-overview/notebooks/services-overview.ipynb)  

# In[3]:


# Set Environment
#Integration
server_base_adress = "doc-server-int.saphety.com/Doc.WebApi.Services"
#Quality
#server_base_adress = "doc-server-qa.saphety.com/Doc.WebApi.Services"
#Production
#server_base_adress = "doc-server.saphety.com/Doc.WebApi.Services"


# In[4]:


#Set authorization data
#username = 'username'
#password = 'request_password'

username = 'user_api_doc'
password = 'request_password'


# In[5]:


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
# - **DocNumber**  
# - **DocNumberList**  
# - **SenderEntityCode**  
# - **DestinationEntityCode**   
# - **DocumentDateStart**  
# - **DocumentDateEnd**  
# - **CreationDateStart**  
# - **CreationDateEnd**  
# - **LastChangeDateStart**  
# - **LastChangeDateEnd**  
# - **DueDateStart**  
# - **DueDateEnd**  
# - **TotalPayableStart**  
# - **TotalPayableEnd**  
# - **SenderVatNumber**  
# - **SenderVatNumberCountry**  
# - **DestinationVatNumber**  
# - **DestinationVatNumberCountry**  
# - **SenderDocumentStatusCodes**  
# - **DestinationDocumentStatusCodes**  
# - **DocumentsTypeIds**  
# - **SenderDirectory**  
# - **DestinyDirectory**  
# - **SelfBilling**  
# - **UnreadDocument**  
# - **IgnoreDraftDirectories**  
# - **EntityCodes**  
# - **DocPlatform**  
# - **MetaInfoKey**  
# - **MetaInfoValue**  
# - **ProductIssuerCode**  
# - **ProductCustomerCode**  
# - **ProductGTIN**  
# - **ProductDescription**  
# - **OriginSystemCode**  
# - **OrderNumber**  

# In[8]:


service_url = "https://" + server_base_adress + "/api/Document/search"

# Search criteria data goes in payload as json
payload = {
  'RestrictionCriteria': {
    'DocNumber': 'INVOICE20210615-00',
    'DestinationEntityCode': "PT560333331"
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

