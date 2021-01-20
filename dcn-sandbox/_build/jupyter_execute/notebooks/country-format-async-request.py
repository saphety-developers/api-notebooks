#!/usr/bin/env python
# coding: utf-8

# # Send invoices using legal format
# The Portuguese governament defined the XML **UBL CIUS-PT** has the format to interchange electronic invoices with the public administration.  
# The tecnhical specifications for the CIUS-PT are defined by eSPAP. [Legal format documnetion documentation here at eSPAP](https://www.espap.gov.pt/spfin/normas/Paginas/normas.aspx)  
# [A CIUS-PT validator is available here](https://doc-server.saphety.com/Doc.Client/public/CIUSvalidation/PT?language=pt)
# 
# If your billing system is able to generate this format, you can use Saphety's Invoice Network (SIN) services to delivery your invoices and store them according to all legal requirements.  
# Be sure that you use the [CIUS-PT validator](https://doc-server.saphety.com/Doc.Client/public/CIUSvalidation/PT?language=pt) to garantee that your invoices are in accordance to the tecnhical specifications defined by eSPAP.
# 
# ## CountryFormatAsyncRequest
# This is the SIN web service for processing and delivering invoices in CIUS-PT format.
# This service should be used in the following cases:
# 
# * Your customer is a public administration entity that requires to receive the invoice in the Portuguese legal format (**CIUS-PT**)
# * Your customer is a company that requires receiving the invoice in a specific standard format (**non CIUS-PT**) such as a retail company, banking institutions etc..
# * You want a full automation on sending invoices directly from your billing system
# * You want to control the delivery status of the invoices to yous customer
# * You want to garantee that your invoices are in accordance to all legal requirements such as digital signature, repository storage, delivery methos etc..
# 
# ### Service steps
# 1. Get a token from your SIN credentials by calling the service **_Account/getToken_**
# 2. Send your invoice calling the **asynchronous** service **_CountryFormatAsyncRequest/processDocument_**; the legal invoice format (CIUS-PT) is sent in the payload
# 3. Check to success of your request using the received *request id* at **_CountryFormatAsyncRequest/{RequestId}_**
# 4. Once the request has finished successfully you get back a *document id*; check the invoice integration status on your customer at service **_OutboundFinancialDocument_/{DocumentId}**
# 

# ### Services considerations
# All services can be consulted using the Open API Specification (OAS3):  
# [API specification](https://dcn-solution-qa.saphety.com/Dcn.Business.WebApi/api/index.html) at https://dcn-solution-qa.saphety.com/Dcn.Business.WebApi/api/index.html

# #### Asynchrounous
# The service **_CountryFormatAsyncRequest/processDocument_** is an asynchrounous service. An invoice can take a few seconds to process (validate, sign, send to your costumer).  
# Since this is an integration API thousands of requests can be sent at the same time. For each request you receive immediatly a request id. Use it to query the request status.

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

# ## Get a token (Account/getToken)
# You have been given credentials when registering in SIN.  
# Use those credentials to get a token at.
# ```
# https://<ServerBaseAddress>/api/Account/getToken
# ```

# In[46]:


# Integration environment
server_base_adress = "dcn-solution-int.saphety.com/Dcn.Business.WebApi"
# Quality environment
#server_base_adress = "dcn-solution-qa.saphety.com/Dcn.Business.WebApi"
# Production environemnt
#server_base_adress = "dcn-solution.saphety.com/Dcn.Business.WebApi"
# SANDBOX - Integration environment
#server_base_adress = "dcn-solution-int.saphety.com/Dcn.Sandbox.WebApi"


# In[47]:


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


# In[48]:


# formating the response to json for visualization purposes only
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# In[49]:


# your token is at:
token = json_response["Data"];
print (token)


# ## Send invoice request (CountryFormatAsyncRequest/processDocument)
# No that you have token you can send an invoice in the legal format (CISU-Pt)

# ### Bulild the service endpoint url
# In the service url you need to supply 2 paramenters:
# 1. Invoice issuer NIF **_\<IssuerNIF>_** (prefixed with the country code)  
#     Must be the NIF of the registered company in SIN (ex: PT507957547). This NIF will be matched against the account registration in SIN for authorization purposes.
# 2. The document type **_\<DocumentType>_** must be one of the following
#     1. **INVOICE**
#     2. **CREDIT_NOTE**
# 
# ```
# https://<ServerBaseUrl>/CountryFormatAsyncRequest/processDocument/<IssuerNIF>/<DocumentType>/PT
# ```
# For sending an invoice the service endpoint becomes (example):
# ```
# https://<ServerBaseUrl>/CountryFormatAsyncRequest/processDocument/PT507957547/INVOICE/PT
# ```

# In[50]:


# SIN service url form sending invoices requires issuer NIF and country and the document type
issuer_nif = "PT507957547"
document_type = "INVOICE"

service_url = """{ServerBaseUrl}/api/CountryFormatAsyncRequest/processDocument/{IssuerNIF}/{DocumentType}/PT""".format(
    ServerBaseUrl=server_base_adress,
    IssuerNIF=issuer_nif,
    DocumentType=document_type
)
service_url = "https://" + service_url
print (service_url)


# ### Prepare the payload according to legal invoice format (CIUS-PT)
# The legal invoice format in Portugal (CIUS-PT) is defined by eSPAP.  
# [Legal format documnetion documentation here at eSPAP](https://www.espap.gov.pt/spfin/normas/Paginas/normas.aspx)  
# [A CIUS-PT validator is available here](https://doc-server.saphety.com/Doc.Client/public/CIUSvalidation/PT?language=pt)

# In[51]:


# request boby must be a valid CIUS-PT
body_cius_pt = """<?xml version="1.0" encoding="utf-8"?>
<ubl:Invoice xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" 
xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:ubl="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2">
  <cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:feap.gov.pt:CIUS-PT:2.0.0</cbc:CustomizationID>
  <cbc:ID>INVOICE-API-DOC-00001</cbc:ID>
  <cbc:IssueDate>2020-12-31</cbc:IssueDate>
  <cbc:DueDate>2019-01-28</cbc:DueDate>
  <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>
  <cbc:DocumentCurrencyCode>EUR</cbc:DocumentCurrencyCode>
  <cac:OrderReference>
    <cbc:ID>ORD-001</cbc:ID>
  </cac:OrderReference>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cbc:EndpointID schemeID="EM">sin_api_documentation_user@saphety.com</cbc:EndpointID>
      <cac:PartyIdentification>
        <cbc:ID schemeID="0001">PT507957547</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyIdentification>
        <cbc:ID schemeID="0088">5600000455210</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Saphety</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Rua Viriato, 13 - 2.º Piso</cbc:StreetName>
        <cbc:CityName>LISBOA</cbc:CityName>
        <cbc:PostalZone>2860-358</cbc:PostalZone>
        <cbc:CountrySubentity>1050-233</cbc:CountrySubentity>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO3166-1">PT</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:CompanyID>PT507957547</cbc:CompanyID>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Saphety</cbc:RegistrationName>
        <cbc:CompanyID schemeID="0001">507957547</cbc:CompanyID>
      </cac:PartyLegalEntity>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="0001">PT507641230</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>FIREFLY - INFORMÁTICA E INTEGRAÇÃO</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Alam. Bonifácio Lázaro Lozano Nr. 13 Piso 0 B</cbc:StreetName>
        <cbc:PostalZone>2780-125</cbc:PostalZone>
        <cbc:CountrySubentity>PT</cbc:CountrySubentity>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO3166-1">PT</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:CompanyID>PT507641230</cbc:CompanyID>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>FIREFLY - INFORMÁTICA E INTEGRAÇÃO</cbc:RegistrationName>
      </cac:PartyLegalEntity>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:Delivery>
    <cac:DeliveryLocation>
      <cbc:ID schemeID="0001">PT507641230</cbc:ID>
      <cac:Address>
        <cbc:StreetName>Alam. Bonifácio Lázaro Lozano Nr. 13 Piso 0 B</cbc:StreetName>
        <cbc:CityName>Oeiras</cbc:CityName>
        <cbc:PostalZone>2780-125</cbc:PostalZone>
        <cbc:CountrySubentity>PT</cbc:CountrySubentity>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO3166-1">PT</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:DeliveryLocation>
    <cac:DeliveryParty>
      <cac:PartyName>
        <cbc:Name>FIREFLY - INFORMÁTICA E INTEGRAÇÃO</cbc:Name>
      </cac:PartyName>
    </cac:DeliveryParty>
  </cac:Delivery>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="EUR">23.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="EUR">100.00</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="EUR">23.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>23.00</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="EUR">100.00</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="EUR">100.00</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="EUR">123.00</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="EUR">123.00</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="C62">10.00</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="EUR">100.00</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Name>Item 1</cbc:Name>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>23.00</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="EUR">10.00</cbc:PriceAmount>
    </cac:Price>
  </cac:InvoiceLine>
</ubl:Invoice>
"""


# ### Call service and get back the request id

# In[52]:


# build the request
headers = {
    'Content-Type': 'application/xml',
    'Authorization': 'bearer ' + token
    }
# POST request to send the invoice
response = requests.request("POST", service_url, data=body_cius_pt, headers=headers)


# In[53]:


# formating the response to json for visualization purposes only
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))


# In[54]:


# your request id is at:
request_id = json_response["Data"];
print ('The request id to query on service status: ' + request_id)


# ## Check to success of your request (CountryFormatAsyncRequest/{RequestId})
# Query the system using this *request id* in order to get the status (success or error) of your request

# ### Bulild the service endpoint url
# In the service url you need to supply the request id received
# 
# ```
# https://<ServerBaseUrl>/CountryFormatAsyncRequest/<RequestId>
# ```

# In[55]:


# SIN service url for retrieving the status of a process

service_url = """{ServerBaseUrl}/api/CountryFormatAsyncRequest/{RequestId}""".format(
    ServerBaseUrl=server_base_adress,
    RequestId=request_id
)
service_url = "https://" + service_url
print (service_url)


# ### Check your request status

# In[63]:


# build the request
headers = {
    'Authorization': 'bearer ' + token
    }
# POST request to send the invoice
response = requests.request("GET", service_url, headers=headers)
# formating the response to json for visualization purposes only
json_response = json.loads(response.text)


# In[64]:


# Your status:
status = json_response["Data"]
outbound_financial_document_id = None
#print(json.dumps(json_response, indent=4))

#request status (Queued, Running, Error, Finished)
request_status = json_response["Data"]["AsyncStatus"]

if request_status == "Queued":
    print ("Your request in queue to be processed check the status again in a few seconds...")
if request_status == "Running":
    print ("Your request is runnig check the status again in a few seconds...")
if request_status == "Error":
    print ("Your request has finished with the following errors:")
    error_list=json_response["Data"]["ErrorList"]
    print(error_list)
    print ("Correct the errros and sublit the document again")
elif request_status == "Finished":
    print ("Your request has finished.")
    outbound_financial_document_id = json_response["Data"]["OutboundFinancialDocumentId"]
    print("You have created the outbound document id: " + outbound_financial_document_id)
else:
    print("Your request status: " + request_status);

# the final status Finished and Error
if request_status != "Finished" and request_status != "Error":
    print("Your is not finished yet: " + request_status)


# ## Check the invoice integration status (OutboundFinancialDocument/{DocumentId})
# With the received outbound finantial document id you can query the system for document integration status
# 

# ### Bulild the service endpoint url
# In the service url you need to supply the outbfinancialdocument received
# 
# ```
# https://<ServerBaseUrl>/OutboundFinancialDocument/<OutboundFinancialDocumentId>
# ```

# In[65]:


if not outbound_financial_document_id:
     print("Your do not have a valid document id. Make sure the service CountryFormatAsyncRequest finished successfully last known status: " + request_status)
else:
    # SIN service url for retrieving inforfation on invoice previously sent
    service_url = """{ServerBaseUrl}/api/OutboundFinancialDocument/{OutboundFinancialDocumentId}""".format(
        ServerBaseUrl=server_base_adress,
        OutboundFinancialDocumentId=outbound_financial_document_id
    )
    service_url = "https://" + service_url
    print (service_url)


# In[66]:


# build the request
headers = {
    'Authorization': 'bearer ' + token
    }
# POST request to send the invoice
response = requests.request("GET", service_url, headers=headers)

# formating the response to json for visualization purposes only
json_response = json.loads(response.text)


# In[67]:


integration_status = json_response["Data"]["IntegrationStatus"]

#integration status (Sent, Received,...)

if integration_status == "Sent":
    print ("Sent: Your invoice has been sucessfully processed ans sent to your customer.")
if integration_status == "Received":
    print ("Received: Your invoice has been received by your customer.")
else:
    print("Your invoice integration status: " + integration_status);

#print(json.dumps(json_response, indent=4))


# **Use the OutboundFinancialDocumentId for any future checks on the invoice.**
