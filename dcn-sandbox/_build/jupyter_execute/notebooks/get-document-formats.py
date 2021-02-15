#!/usr/bin/env python
# coding: utf-8

# # Get invoice PDF or UBL format from archive
# 
# ## Get a token (Account/getToken)
# You have been given credentials when registering in SIN.  
# Use those credentials to get a token at.
# ```
# https://<ServerBaseAddress>/api/Account/getToken
# ```

# In[1]:


# Integration environment
#server_base_adress = "dcn-solution-int.saphety.com/Dcn.Business.WebApi"
# Quality environment
#server_base_adress = "dcn-solution-qa.saphety.com/Dcn.Business.WebApi"
# Production environemnt
#server_base_adress = "dcn-solution.saphety.com/Dcn.Business.WebApi"
# SANDBOX - Integration environment
server_base_adress = "dcn-solution-int.saphety.com/Dcn.Sandbox.WebApi"


# In[2]:


import requests
import json

# SIN account service url
service_url = "https://" + server_base_adress + "/api/Account/getToken"

# the username and password you registerd in SIN
username = 'sin_api_documentation_user@saphety.com'
password = 'request_password'

# auhtentication data goes in payload as json
payload = {
      'Username': username,
      'Password': password
}
# payload goes in json, serialize the payloal object to json
request_data=json.dumps(payload)
# indicate in header that payload is json
headers = {
    'content-type': 'application/json'
    }
# POST request to get a token
response = requests.request("POST", service_url, data=request_data, headers=headers)


# In[3]:


# formating the response to json for visualization purposes only
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# In[4]:


# your token is at:
token = json_response["Data"];
print (token)


# ## Get a List of Document Formats storage by DocumentId (OutboundFinancialDocument/documentFormats/{documentId})

# ### Build the service endpoint url
# In the service url you need to supply the outbfinancialdocument received
# 
# ```
# https://<ServerBaseUrl>/OutboundFinancialDocument/documentFormats/<OutboundFinancialDocumentId>
# ```

# In[5]:


# SIN service url for retrieving inforfation on invoice previously sent
service_url = """{ServerBaseUrl}/api/OutboundFinancialDocument/documentFormats/{OutboundFinancialDocumentId}""".format(
    ServerBaseUrl=server_base_adress,
    OutboundFinancialDocumentId="fc5e547d-8537-4e05-97d5-1159c62efd6f"
)
service_url = "https://" + service_url
print (service_url)


# ### Call the service to get the formats
# You will call the service endpoint url

# In[6]:


# build the request
headers = {
    'Authorization': 'bearer ' + token
    }
# POST request to send the invoice
response = requests.request("GET", service_url, headers=headers)

# formating the response to json for visualization purposes only
json_response = json.loads(response.text)
print(json.dumps(json_response["Data"], indent=4))


# ### Read the service response
# Now you need to read the service response to format all document formats and get the end file

# In[16]:


# for loop to see all Data
formats = json_response["Data"];
for format in formats:
    if format["FormatType"] == "pdf":
        print ("PDF: " + format["DocumentLink"] + "\n");
    if format["FormatType"] == "final":
        print ("Final: " + format["DocumentLink"] + "\n");
    if format["FormatType"] == "ubl21":
        print ("UBL: " + format["DocumentLink"] + "\n");
    if format["FormatType"] == "signed":
        print ("Signed: " + format["DocumentLink"] + "\n");

