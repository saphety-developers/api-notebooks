# Configuration and Specification 
## Environments
Saphety Invoice Network API is connected with these environments:

- Sandbox (test)
- Production

**Sandbox environment**  
Used for initial testing purposes. It's a controlled environment, that allows to test API services, but does not persist/archive documents in a database.

In this way, it is possible to test API services, without the risk of sending invoices to customers test environments, or sending notification emails to real customers addresses.

Bear in mind that, because the documents in this environment are not persisted/archived in the database, services will always return results of a mockup invoice, regardless of the document that has been processed. The same will happen with email notifications, in this environment, email notifications generated will always be sent to the user registration email created in Sandbox portal.

If you want to test the API in this environment, you will need to register at Sandbox portal to get your own credentials (username and password) to generate a valid token.

To register and get your credentials for Sandbox portal go here: [Dcn Sandbox](https://dcn-solution.saphety.com/Dcn.Sandbox.Client/public)

**Production environment**  
Production environment represents the live and stable version of the API that serves actual users, businesses, or applications in a real-world setting.

It is the operational state where the API is fully deployed and available for regular use.

If you want to register your company in Saphety Invoice Network solution go here: [Dcn Client](https://www.saphety.com/)

## API Servers Base Address URL
**Sandbox environment**:  
https://dcn-solution.saphety.com/Dcn.Sandbox.WebApi

**Production environment**:  
https://dcn-solution.saphety.com/Dcn.Business.WebApi

## Open API specification (OAS3)
**Sandbox environment**:  
https://dcn-solution.saphety.com/Dcn.Sandbox.WebApi/api/index.html 

**Production environment**:  
https://dcn-solution.saphety.com/Dcn.Business.WebApi/api/index.html  
https://invoicenetwork.saphety.com/IN2.Notifications.WebApi/swagger/index.html  
https://dcn-solution.saphety.com/IN2.WebStore.WebApi/swagger/index.html  
https://dcn-solution.saphety.com/IN2.IntegrationAccess.WebApi/swagger/index.html