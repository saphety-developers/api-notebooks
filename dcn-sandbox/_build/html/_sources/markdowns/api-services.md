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
<font size="5">[Send electronic invoices using legal format](../notebooks/country-format-async-request.ipynb)</font><br>
Use this service to **send** eletronic invoices in Portuguese legal format CIUS-PT.

<font size="5">[Send PDF invoice, <b>by standard</b> email notification](../notebooks/pdf-async-request.ipynb)</font><br>
Use this service to **sign**, **store** and **send** PDF invoices.
The PDF invoice will be sent by email to your costumer using the predefined content layout.

<font size="5">[Send PDF invoice, <b>by customized</b> email notification](../notebooks/pdf-async-request-customized-email.ipynb)</font><br>
Use this service to **sign**, **store** and **send** PDF invoices.
The PDF invoice will be sent by email to your costumer using a cutomized contetn layout.

<font size="5">[Store PDF invoices](../notebooks/pdf-async-request-store-only.ipynb)</font><br>
Use this service to **sign** and **store** PDF invoices.
The PDF invoice will be signed and stored, and not sent to your costumers.

<font size="5">[Get invoice **status** in archive](../notebooks/get-document.ipynb)</font><br>
Use this service to **get** an invoice **status** in archive.

<font size="5">[Get invoice **status transitions** in archive ](../notebooks/get-document-status-transitions.ipynb)</font><br>
Use this service to **get** an invoice **status transitions** in archive.

<font size="5">[Get invoice PDF or UBL from archive](../notebooks/get-document-formats.ipynb)</font><br>
Use this service to **get** invoice formats from archive.

<font size="5">[Resend invoice by email notification](../notebooks/new-sent-notifications.ipynb)</font><br>
Use this service to **resend** invoices by email notification.

<font size="5">[Get integrated destinations](../notebooks/get-destinations.ipynb)</font><br>
Use this service to **get** all or filtred integrated destinations.

<font size="5">[Get invoice **permalinks**](../notebooks/get-document-permalinks.ipynb)</font><br>
Use this service to **get** an invoice **download permalinks**.

<font size="5">[Get company subscriptions](../notebooks/get-subscriptions.ipynb)</font><br>
Use this service to **get** all your **company subscriptions**.

<font size="5">[Get company subscription features](../notebooks/get-document-permalinks.ipynb)</font><br>
Use this service to **get company subscription features** information.

<font size="5">[Get company plan information](../notebooks/get-plan.ipynb)</font><br>
Use this service to **get company plan** information.

<font size="5">[Get company custom plan information](../notebooks/get-custom-plan.ipynb)</font><br>
Use this service to **get company custom plan** information.