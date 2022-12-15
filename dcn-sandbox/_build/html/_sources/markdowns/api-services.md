# API Services
Please consult the API services specification and orchestration.

### Services considerations
All API services can be consulted using the **Open API Specification (OAS3)**:

**For Tests purposes**<br>
API specification of Test environment at [API specification](https://dcn-solution.saphety.com/Dcn.Sandbox.WebApi/api/index.html)<br>
<font color=red>\*must use the credentials (user and pw) defined at your **SANDBOX** registration</font>

**For Production**<br>
API specification of Production environment at [API specification](https://dcn-solution.saphety.com/Dcn.Business.WebApi/api/index.html)<br>
<font color=red>\*must use the credentials (user and pw) defined at **Saphety Invoice Network** registration</font>

## Services
<font size="5">[Send invoices using legal format](../notebooks/country-format-async-request.ipynb)</font><br>
Use this service to **send** invoices in Portuguese legal format CIUS-PT.

<font size="5">[Send PDF invoices by email](../notebooks/pdf-async-request.ipynb)</font><br>
Use this service to **sign**, **store** and **send** PDF invoices.
The PDF invoice will be sent by email to your costumer.

<font size="5">[Store PDF invoices](../notebooks/pdf-async-request-store-only.ipynb)</font><br>
Use this service to **sign** and **store** PDF invoices.
The PDF invoice will be signed and stored, and not sent to your costumers.

<font size="5">[Check invoice **status** in archive](../notebooks/get-document.ipynb)</font><br>
Use this service to **check** an invoice **status** in archive.

<font size="5">[Check invoice **status transitions** in archive ](../notebooks/get-document-status-transitions.ipynb)</font><br>
Use this service to **check** an invoice **status transitions** in archive.

<font size="5">[Get invoice PDF or UBL from archive](../notebooks/get-document-formats.ipynb)</font><br>
Use this service to **get** invoice formats from archive.

<font size="5">[Resend invoice by email notification (***Deprecated***)](../notebooks/sent-notifications-deprecated.ipynb)</font><br>
***This service is deprecated and will be removed on June 30, 2023***. Use the [(New) Resend invoice by email notification](../notebooks/new-sent-notifications.ipynb) service instead.

<font size="5">[(New) Resend invoice by email notification](../notebooks/new-sent-notifications.ipynb)</font><br>
Use this service to **resend** invoices by email notification.

<font size="5">[Get integrated destinations](../notebooks/get-destinations.ipynb)</font><br>
Use this service to **get** all or filtred integrated destinations.

<font size="5">[Get invoice **email tracking ids**](../notebooks/get-destinations.ipynb)</font><br>
Use this service to **get** invoice's **email tracking ids**.

<font size="5">[Get invoice **permalinks**](../notebooks/get-document-permalinks.ipynb)</font><br>
Use this service to **get** an invoice **download permalinks**.