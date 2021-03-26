#!/usr/bin/env python
# coding: utf-8

# # Resend PDF invoice email notification
# Use this service to **resend** PDF invoices email notification.
# 
# ### Service steps
# 1. Get a token from your credentials by calling the service **_Account/getToken_**;
# 2. Resend notifications calling the service **_OutboundFinancialDocumentMaintnance/sendAditionalNotifications_**;
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
# Credentials have be given to you, according to your registration at **SANDBOX** or **Saphety Invoice Network**:
# * For **Test purposes**, the **_user_** and **_password_** defined at **SANDBOX** registration<br>
# or
# * For **Production**, the **_user_** and **_password_** defined at **Saphety Invoice Network** registration
# 
# Use those credentials to get a token at:
# ```
# https://<ServerBaseAddress>/api/Account/getToken
# ```

# In[11]:


# SANDBOX - Test Environment
server_base_adress = "dcn-solution.saphety.com/Dcn.Sandbox.WebApi"

# Saphety Invoice Network - Production Environment
#server_base_adress = "dcn-solution.saphety.com/Dcn.Business.WebApi"


# In[12]:


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


# <font color=red>\* **Note:** the credentials (user and password) in this documentation were created by Saphety and can only be used in the SANDBOX environment. For tests we recommend that you use the credentials you obtained when registering with the SANDBOX.</font>

# In[13]:


# formating the response to json for visualization purposes only
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# In[14]:


# your token is at:
token = json_response["Data"];
print (token)


# ## 2. Resend PDF invoice notifications (OutboundFinancialDocumentMaintnance/sendAditionalNotifications)

# ### Build the service endpoint url
# In the service url you don't need to supply anything.
# 
# ```
# https://<ServerBaseUrl>/OutboundFinancialDocumentMaintnance/sendAditionalNotifications
# ```

# In[15]:


# SIN service ur
service_url = """{ServerBaseUrl}/api/OutboundFinancialDocumentMaintnance/sendAditionalNotifications""".format(
    ServerBaseUrl=server_base_adress
)
service_url = "https://" + service_url
print (service_url)


# ### Build the service body
# In the service body you need to supply some data.
# 
# * **OutboundFinancialDocumentId**<br>
#   Set the OutboundFinancialDocumentId to your document.<br>
# * **DestinationEmails**
#   * _Email_: Set the client/receiver email address to send the notification
#   * _SendAttachment_: Set whether the PDF is sent as an attachment in the notification. Allowed values for this parameter: True, False.
#   * _LanguageCode_: Set the notification language. Format is ISO 639-1 (ex: pt)

# In[16]:


#headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'bearer ' + token
    }
# payload as json
payload = {
  'OutboundFinancialDocumentId': 'fc5e547d-8537-4e05-97d5-1159c62efd6f',
  'DestinationEmails': [{
    'Email': 'sin_api_documentation_user@saphety.com',
    'SendAttachment': True,
    'LanguageCode': 'PT'
  }]
}
request_data=json.dumps(payload)


# <font color=red>\* **Note :** in the Sandbox environment, the notifications are sent only for the user registration email, even if within the service payload are displayed other email addresses.</font>

# ### Call the service resend notifications
# You will call the service endpoint url

# In[17]:


# Send the request (POST).
response = requests.request("POST", service_url, data=request_data, headers=headers)

# formating the response to json for visualization purposes only
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# ### Read the service response
# Now you need to read the service response and see the email send

# In[18]:


# for loop to see all Data
formats = json_response["Data"];
print(json.dumps(formats, indent=4))

