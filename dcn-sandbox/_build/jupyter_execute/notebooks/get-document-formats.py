#!/usr/bin/env python
# coding: utf-8

# # Get invoice PDF or UBL format from archive
# Use this service to **get** all invoice formats from archive for your processed document.
# 
# ### Service steps
# 1. Get a token from your credentials by calling the service **_Account/getToken_**;
# 2. Get all invoice formats calling the service **_OutboundFinancialDocument/documentFormats/{documentId}_**;
# 
# #### Response structure from server
# When a request is well formed and the authentication data is correct the system responds with a message envelope as follows: 
# 
# ```Javascript
# {
# 	"CorrelationId": "<GUID>", /* for correlation purposes */
# 	"IsValid": true,           /* false in case of erros */
# 	"Errors": [],              /* if empty is a good signal */
# 	"Data": "<Service Response Data>"   /* the data retuned ex: token, invoice status, dependent on the service called */
# }
# ```

# ## 1. Get a token (Account/getToken)
# Credentials have be given to you, according to your registration at **API-SANDBOX Portal** or **Saphety Invoice Network**:
# * For **Test purposes**, the **_user_** and **_password_** defined at **API-SANDBOX Portal** registration<br>
# or
# * For **Production**, the **_user_** and **_password_** defined at **Saphety Invoice Network** registration
# 
# Use those credentials to get a token at:
# ```
# https://<ServerBaseAddress>/api/Account/getToken
# ```

# In[1]:


# SANDBOX - Test Environment
server_base_adress = "dcn-solution.saphety.com/Dcn.Sandbox.WebApi"

# Saphety Invoice Network - Production Environment
#server_base_adress = "dcn-solution.saphety.com/Dcn.Business.WebApi""


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


# <font color=red>\* **Note:** the credentials (user and password) in this documentation were created by Saphety and can only be used in the API-SANDBOX environment. For tests we recommend that you use the credentials you obtained when registering with the API-SANDBOX Portal.</font>

# In[3]:


# formating the response to json for visualization purposes only
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# In[4]:


# your token is at:
token = json_response["Data"];
print (token)


# ## 2. Get a List of Document Formats storage by DocumentId (OutboundFinancialDocument/documentFormats/{documentId})

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

