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

<font size="5">[Send PDF invoices **without QRCode** via email](../notebooks/pdf-async-request.ipynb)</font><br>
Use this service to **sign**, **store** and **send** PDF invoices that don’t have a QRCode.
The PDF will be sent by email to your costumers.

<font size="5">[Send PDF invoices **with QRCode** via email](../notebooks/pdf-async-request-embebed-data.ipynb)</font><br>
Use this service to **sign**, **store** and **send** PDF invoices that have a QRCode.
The PDF will be sent by email to your costumers.

<font size="5">[Store PDF invoices **without QRCode**](../notebooks/pdf-async-request-store-only.ipynb)</font><br>
Use this service to **sign** and **store** PDF invoices that **don’t have** a **QRCode**.

<font size="5">[Store PDF invoices **with QRCode**](../notebooks/pdf-async-request-embebed-data-store-only.ipynb)</font><br>
Use this service to **sign** and **store** PDF invoices that **have** an **QRCode**.

<font size="5">[Check invoice **status** in archive](../notebooks/get-document.ipynb)</font><br>
Use this service to **check** an invoice **status** in archive.

<font size="5">[Get invoice PDF or UBL from archive](../notebooks/get-document-formats.ipynb)</font><br>
Use this service to **get** invoice formats from archive.

<font size="5">[Resend PDF invoice email notification](../notebooks/sent-notifications.ipynb)</font><br>
Use this service to **resend** PDF invoices email notification.