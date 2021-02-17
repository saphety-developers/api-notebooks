# API Services
Please consult the API services specification and orchestration.

### Services considerations
All API services can be consulted using the **Open API Specification (OAS3)**:

**For Tests purposes**<br>
API specification of Test environment at [API specification](https://dcn-solution.saphety.com/Dcn.Sandbox.WebApi/api/index.html)<br>
<font color=red>\*must use the credentials (user and pw) defined at your **API-SANDBOX Portal** registration</font>

**For Production**<br>
API specification of Production environment at [API specification](https://dcn-solution.saphety.com/Dcn.Business.WebApi/api/index.html)<br>
<font color=red>\*must use the credentials (user and pw) defined at **Saphety Invoice Network** registration</font>

## Services
<font size="5">[Send invoices using legal format](../notebooks/country-format-async-request.ipynb)</font><br>
Use this service to **send** invoices in Portuguese legal format CIUS-PT.

<font size="5">[Send PDF invoices **without QRCode** via email](../notebooks/pdf-async-request.ipynb)</font><br>
Use this service to **sign** and **send** PDF invoices by email to your costumers.

<font size="5">[Send PDF invoices **with QRCode** via email](../notebooks/pdf-async-request-embebed-data.ipynb)</font><br>
Use this service to **sign** and **send** PDF invoices with QRCode by email to your costumers.

<font size="5">[Get invoice formats from archive](../notebooks/get-document-formats.ipynb)</font><br>
Use this service to **get** all invoice formats from archive for your processed document.