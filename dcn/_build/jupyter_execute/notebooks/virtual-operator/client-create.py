#!/usr/bin/env python
# coding: utf-8

# # Create client
# Use this service to **add/register** a client into your virtual operator account. 
# 
# ### Service steps
# 1. Get a token from your credentials by calling the service **_Account/getToken_**
# 2. Create your client calling the **_asynchronous_** service **_VirtualOperator/client_**;

# #### Asynchrounous
# The service **_VirtualOperator/client_** is an asynchrounous service.<br>
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

# In[8]:


# Saphety Invoice Network - Integration Environment
server_base_adress = "dcn-solution-qa.saphety.com/Dcn.Business.WebApi"


# In[9]:


import requests
import json

# SIN account service url
service_url = "https://" + server_base_adress + "/api/Account/getToken"

# Example of username and password
username = 'sin_api_vo_documentation_user@saphety.com'
password = 'DocUser2022@'

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

# In[10]:


# Formating the response to json for visualization purposes only
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# In[11]:


# Your token is at:
token = json_response["Data"];
print (token)


# ## 2. Create client
# Now that you have a token you can **add/register** a client. In the service payload you need to supply these parameters: 
# * **IntlVatCode**<br>
#   Set the client Vat Number. Format is countryCode + Vat Number (ex: PT507957547)<br>
# * **CompanyName**<br>
#   Set the client’s name (ex: CLIENT LDA.)<br>
# * **AdressLine**<br>
#   Set the client address (ex: Rua do Cliente nº1 3ºPiso)<br>
# * **City**<br>
#   Set the client city (ex: Lisboa)<br>
# * **ZipCode**<br>
#   Set the client adress zipCode (ex: 1050-233)<br>
# * **ZipArea**<br>
#   Set the client adress area (ex: Lisboa)<br>
# * **CountryCode**<br>
#   Set the client countryCode. Format ISO 3166 Alpha-2 code (ex: PT)<br>
# * **CommercialRecordWebCode**<br>
#   Set the client commercial record web code (Registo commercial, ex:507957547)<br>
# * **LanguageCode**<br>
#   Set the client language. Format is ISO 639-1 (ex:PT)<br>

# ### Build the service endpoint url and payload

# In[12]:


service_url = """{ServerBaseUrl}/api/VirtualOperator/client""".format(
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
      'IntlVatCode': 'PT979420199',
      'CompanyName': 'Virtual Operator Client',
      'AddressLine': 'R. Viriato 13',
      'City': 'Lisboa',
      'ZipCode': '1050-233',
      'ZipArea': 'Lisboa',
      'CountryCode': 'PT',
      'CommercialRecordWebCode': '123456789',
      'LanguageCode': 'PT'
}
request_data=json.dumps(payload)


# <font color=red>\* **Note:** the payload example showed here is a sample created by Saphety.</font>

# ### Call service and get back the response

# In[13]:


# Send the request (POST). The service return a request id
response = requests.request("POST", service_url, data=request_data, headers=headers)

# formating the response to json for visualization purposes only
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# In[14]:


response = json_response["Data"];
errors = json_response["Errors"];

if response == {}:
    print ("Created with success!")
if response != {}:
    print(json.dumps(errors, indent=4))

