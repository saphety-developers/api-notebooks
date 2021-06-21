#!/usr/bin/env python
# coding: utf-8

# # Send messages to Saphety (ReceiveMessage)
# Although this service is called ReceiveMessage, it allows you to send a message to Saphety’s network;   
# The method name (ReceiveMessage) is given from Saphety’s network perspective.   
# The following example shows how to send a file to Saphety. This file is just an example; its content can be any commercial document (Order, Invoice etc.).

# In[33]:


fileText = '<invoice><number>inv001<number><date>2019-04-19</date><value>115.00</value></invoice>'


# First read the file content and convert to it Base64. Following is:

# In[34]:


fileBase64 = 'PGludm9pY2U+DQo8bnVtYmVyPmludjAwMTxudW1iZXI+DQo8ZGF0ZT4yMDE5LTA0LTE5PC9kYXRlPg0KPHZhbHVlPjExNSwwMDwvdmFsdWU+DQo8L2ludm9pY2U+'


# The file content encoded in Base64 is transmitted in the Base64Data element.

# ### Create the request object
# The request object have the following values:
# - **Sender**   
# Your UserId (Partner Id)
# - **Receiver**   
# Saphety WS endpoint: QA urn:netdoc:qa; PRD: urn:netdoc:prd
# - **ContentType**   
# File content type, ex: application/xml
# - **Base64Data**   
# File contents encoded in Base64
# - **MessageId**   
# A message identifier for control, use a GUID
# - **Filename**   
# The filename being transferred

# In[35]:


# Set Environment
#Integration
#server_base_adress = "saphetydoc-int.saphety.com/TradeHttp/MessageServiceRest"
#Quality
server_base_adress = "www-qa.netdocs.com.pt/TradeHttp/MessageServiceRest"
#Production
#server_base_adress = "ws.netdocs.com.pt/TradeHttp/MessageServiceRes"


# In[38]:


#Set authorization data
authorization = 'PT500111111:Saphety#_2021'
token = 'UFQ1MDAxMTExMTE6U2FwaGV0eSNfMjAyMQ=='
service_url = "https://" + server_base_adress + "/ReceiveMessage"


# ### Service Response from ReceiveMessage
# For a successful request, the http code for the result is 200   
# Following is a response body for a success call to Receive Message:

# In[45]:


## Get a JWT token from your username and password
import requests
import json

payload = {
    'Sender': 'PT500111111',
    'Receiver': 'urn:netdoc:qa',
    'ContentType': 'application/xml',
    'Base64Data': fileBase64,
    'MessageId': 'de10ebd5-eef5-421e-9ee5-f08f59dfa327',
    'Filename':'invoice001.xml'
}
# Payload goes in json, serialize the payloal object to json
request_data=json.dumps(payload)
# Indicate in header that payload is json
headers = {
    'Authorization': 'Basic ' + token,
    'Content-type': 'application/json'
}
# POST request to get a token
response = requests.request("POST", service_url, data=request_data, headers=headers)
# Serializethe response
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# Pay attention that for an error request the http code of the result is 200.    
# It is required to check the response content for possible errors:

# In[46]:


## Get a JWT token from your username and password
import requests
import json

payload = {
    'Sender': 'PT500111111',
    'Receiver': 'urn:netdoc:qa',
    'ContentType': 'application/xml',
    'Base64Data': 'fileBase64',
    'MessageId': 'de10ebd5-eef5-421e-9ee5-f08f59dfa327',
    'Filename':'invoice001.xml'
}
# Payload goes in json, serialize the payloal object to json
request_data=json.dumps(payload)
# Indicate in header that payload is json
headers = {
    'Authorization': 'Basic ' + token,
    'Content-type': 'application/json'
}
# POST request to get a token
response = requests.request("POST", service_url, data=request_data, headers=headers)
# Serializethe response
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# ## Retrieve messages from Saphety (GetMessageData)
# Saphety web services act like a mailbox for your incoming messages.   
# It is a pool system and you have to pool the messages that are stored in your message queue.   
# You need to performer the following steps:   
# 1. Query your queue to retrieve the list of messages available to download (note that any of this messages can be any document type, ORDERS, INVOICE, DESADV, STATUS, etc); for each message you will obtain the message identifier (Message ID). This is done using the service **ListQueuedMessageIds**.  
# 2. With the previous Message ID, you can obtain your message content. This is done using the service **GetMessageData**.
# 3. After downloading a message, you need to mark it as “read”, so that message is removed from your queue. This is done using the service **ChangeQueuedToProcessed**

# ## Retrieving messages from the message queue
# ### Calling the service ListQueuedMessageIds
# This service is called with a simple GET with the following url parameters:

# In[57]:


print('https://' + server_base_adress + '/ListQueuedMessageIds?Receiver={receiver}')


# Where **{receiver}** is your **UserId** in Saphety network.   
# This will list all messages that are available to download.   
# This service also support additional fields capabilities such as the “**Sender**”. Consult the Swagger documentation to more details.   
# Sample request:

# In[86]:


receiver = 'PT500111111' 
# Build the url
service_url = 'https://' + server_base_adress + '/ListQueuedMessageIds?Receiver=' + receiver;
# Use GET to send the request
response = requests.request("GET", service_url, headers=headers)
# Serializethe response
json_response = json.loads(response.text)
# The result is cutted for better readability
json_response["ResultData"]["MessageIds"] = json_response["ResultData"]["MessageIds"][:2];
print(json.dumps(json_response, indent=4))


# The previous response indicate you have 2 messages available to download with the Message Id:

# In[87]:


for message in json_response["ResultData"]["MessageIds"]:
    print(json.dumps(message["MessageId"], indent=4))


# ### Calling the service GetMessageData
# To retrieve the message content, you need to call the **GetMessageData** as following:

# In[88]:


print('https://' + server_base_adress + '/GetMessageData?Receiver={receiver}&MessageId={messageId}&Sender={sender}')


# In[89]:


receiver = 'PT500111111'
messageId = '20210608142029.91a7f766-c2eb-4dd3-9274-520c2b28a806@L-QA-FES02'
sender = '5600000002186'
# Build the url
service_url = 'https://' + server_base_adress + '/GetMessageData?Receiver=' + receiver + '&MessageId=' + messageId + '&Sender=' + sender;
# Use GET to send the request
response = requests.request("GET", service_url, headers=headers)
# Serializethe response
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# The **ContentType** indicate the file type being download (ex: XML, Text, CSV, etc) and the content itself is encoded in Base64 in the **Base64Data**.

# ### Calling the service ChangeQueuedToProcessed
# After retrieving the documents from your queue, it is required to mark then as **processed**. This operation removes the document from the queue.

# In[90]:


service_url = "https://" + server_base_adress + "/ChangeQueuedToProcessed"
payload = {
    'Sender': sender,
    'Receiver': receiver,
    'MessageId': messageId
}
# Payload goes in json, serialize the payloal object to json
request_data=json.dumps(payload)
# Indicate in header that payload is json
headers = {
    'Authorization': 'Basic ' + token,
    'Content-type': 'application/json'
}
# POST request to get a token
response = requests.request("POST", service_url, data=request_data, headers=headers)
# Serializethe response
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))

