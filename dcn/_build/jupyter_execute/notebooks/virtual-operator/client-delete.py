#!/usr/bin/env python
# coding: utf-8

# # Delete client
# Use this service to **delete** a registered client from your virtual operator account. 
# 
# ### Service steps
# 1. Get a token from your credentials by calling the service **_Account/getToken_**
# 2. Delete your registered client calling the **_asynchronous_** service **_VirtualOperator/client/{clientIntlVatCode}_**;

# #### Asynchrounous
# The service **_VirtualOperator/client/{clientIntlVatCode}_** is an asynchrounous service.<br>
# Since this is an integration API, thousands of requests can be sent at the same time.<br>

# #### Response structure from server
# When a request is well formed and the authentication data is correct the system responds with a message envelope as follows: 
# 
# ```Javascript
# {
# 	"CorrelationId": "<GUID>", /* for correlation purposes */
# 	"IsValid": true,           /* false in case of erros */
# 	"Errors": [],              /* if empty is a good signal */
# 	"Data": "<Service Response Data>"   /* the data retuned ex: token, invoice status .. dependent on the service called */
# }
# ```
# 

# ## 1. Get a token (Account/getToken)
# * For **Test purposes**, the **_user_** and **_password_** defined at **Saphety Invoice Network - Quality environment**<br>
# or
# * For **Production**, the **_user_** and **_password_** defined at **Saphety Invoice Network - Production environment**
# 
# Use those credentials to get a token at:
# ```
# https://<ServerBaseAddress>/api/Account/getToken
# ```

# In[1]:


# Saphety Invoice Network - Integration Environment
server_base_adress = "dcn-solution-qa.saphety.com/Dcn.Business.WebApi"


# In[2]:


import requests
import json

# SIN account service url
service_url = "https://" + server_base_adress + "/api/Account/getToken"

# Example of username and password
username = 'sin_api_vo_documentation_user@saphety.com'
password = 'request_password'

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


# <font color=red>\* **Note:** the credentials (user and password) in this documentation were created by Saphety and can only be used in the Saphety Invoice Network - Quality environment. For tests we recommend that you use your own credentials.</font>

# In[3]:


# Formating the response to json for visualization purposes only
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# In[4]:


# Your token is at:
token = json_response["Data"];
print (token)


# ## 2. Delete client
# Now that you have a token you can **delete** a registered client. In the service payload you need to supply these parameters: 
# * **clientIntlVatCode**<br>
#   Set the client Vat Number. Format is countryCode + Vat Number (ex: PT507957547)<br>

# ### Build the service endpoint url and payload

# In[5]:


clientIntlVatCode = "PT979420199"

service_url = """{ServerBaseUrl}/api/VirtualOperator/client/{clientIntlVatCode}""".format(
    ServerBaseUrl=server_base_adress,
    clientIntlVatCode=clientIntlVatCode
)
service_url = "https://" + service_url
print ('Service url: ' + service_url)

#headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'bearer ' + token
    }


# <font color=red>\* **Note:** the payload example showed here is a sample created by Saphety.</font>

# ### Call service and get back the response

# In[6]:


# Send the request (POST). The service return a request id
response = requests.request("DELETE", service_url, headers=headers)

# formating the response to json for visualization purposes only
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# In[7]:


response = json_response["Data"];
errors = json_response["Errors"];

if response == {}:
    print ("Deleted with success!")
if response != {}:
    print(json.dumps(errors, indent=4))

