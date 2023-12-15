# API Environments
The **Saphety Invoice Network API** is connected to two environments:
* Test (Sandbox)
* Production (Saphety Invoice Network)

## Sandbox environment
The first step to start testing the API is to register at **sandbox** to get your own credentials (username and password) to generate a valid token to test the API in test environment.

With these credentials you are able to test the API, simulating the scenarios as if you were in a Production environment.

Through **sandbox**, you can have access to:
* test API endpoints
* access to API documentation
* additional fields mapping guide for UBL CIUS-PT.xml

**Sandbox** is a controlled environment, that allows to test all services, but **does not** persist/archive documents in a database. In this way, it is possible to test all services, without the risk of sending invoices to the test environments of the receiving entities, or sending emails to real addresses of the receiving entities.

Bear in mind that, because the documents in this **sandbox environment are not** persisted/archived in the database, some services (e.g: **_Get Invoice PDF - UBL from archive_** or **_Check Invoice status in archive_**) will always return results of a mockup invoice from Saphety, regardless of the document that has been processed. The same will happen with email notifications, that is, in the **sandbox** environment, email notifications generated in some services **will always be sent** to the user registration email address on the **sandbox**.

To register on the **sandbox** access here: [Sandbox portal](https://dcn-solution.saphety.com/Dcn.Sandbox.Client/public)


## Production environment
After you have finished developing and testing the **API**, the next step will be to register the issuing company (aka supplier) at **Saphety Invoice Network** in **Production** environment. 

The registration must be done by the issuing entity (aka as supplier) that will use the **API** services. This entity must be registered and must subscribe a plan to start send documents.

To register on the **Saphety Invoice Network platform** access here: [Saphety Invoice Network](https://www.saphety.com/)

The credentials obtained in this registration (user and password) will be the ones you must use to generate a valid token for **API** services in the **Production** environment.