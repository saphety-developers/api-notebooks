#!/usr/bin/env python
# coding: utf-8

# # Count clients
# Use this service to **count** the registered clients from your virtual operator account. 
# 
# ### Service steps
# 1. Get a token from your credentials by calling the service **_Account/getToken_**
# 2. Count your registered clients calling the **_asynchronous_** service **_VirtualOperator/client/count_**;

# #### Asynchrounous
# The service **_VirtualOperator/client/count_** is an asynchrounous service.<br>
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
# Credentials have be given to you, according to your registration at **SANDBOX** or **Saphety Invoice Network**:
# * For **Test purposes**, the **_user_** and **_password_** defined at **SANDBOX** registration<br>
# or
# * For **Production**, the **_user_** and **_password_** defined at **Saphety Invoice Network** registration
# 
# Use those credentials to get a token at:
# ```
# https://<ServerBaseAddress>/api/Account/getToken
# ```

# In[1]:


# Saphety Invoice Network - Integration Environment
server_base_adress = "dcn-solution-int.saphety.com/Dcn.Business.WebApi"


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


# <font color=red>\* **Note:** the credentials (user and password) in this documentation were created by Saphety and can only be used in the API-SANDBOX environment. For tests we recommend that you use the credentials you obtained when registering with the API-SANDBOX Portal.</font>

# In[3]:


# Formating the response to json for visualization purposes only
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# In[4]:


# Your token is at:
token = json_response["Data"];
print (token)


# ## 2. Count clients
# Now that you have a token you can **count** your registered clients. In the service payload you need to supply these parameters:
# * **CompanyName**<br>
#   Set the client’s name (ex: CLIENT LDA.)<br>
# * **IntlVatCode**<br>
#   Set the client Vat Number. Format is countryCode + Vat Number (ex: PT507957547)<br>
# * **CreationDateFrom**<br>
#   Set a start date to narrow your search. Format is dd/mm/yyyy (ex: 01/01/2021)<br>
# * **CreationDateTo**<br>
#   Set an end date to narrow your search. Format is dd/mm/yyyy (ex: 01/01/2031)<br>

# ### Build the service endpoint url and payload

# In[11]:


service_url = """{ServerBaseUrl}/api/VirtualOperator/client/count""".format(
    ServerBaseUrl=server_base_adress
)
service_url = "https://" + service_url
print ('Service url: ' + service_url)

#headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'bearer ' + token
    }
# payload as json
payload = {
    'CompanyName': 'Virtual Operator Client',
    'IntlVatCode': 'PT979420199',
    'CreationDateFrom': '01/01/2021',
    'CreationDateTo': '01/01/2031',
}
request_data=json.dumps(payload)


# <font color=red>\* **Note:** the payload example showed here is a sample created by Saphety.</font>

# ### Call service and get back the response

# In[12]:


# Send the request (POST). The service return a request id
response = requests.request("POST", service_url, data=request_data, headers=headers)

# formating the response to json for visualization purposes only
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# In[12]:


response = json_response["Data"];
print(json.dumps(response, indent=4))

