# Welcome to Saphety Invoice Network API
## Scope
Be compliant to all legal standards while issuing invoices and guaranteeing timely delivery to customers is pivotal for every company's billing operations.  Our API was created to send invoices compliant with legal requirements and ensuring their delivery to the customers (receivers).

**Type of invoices**:
- Send Electronic invoices using Portuguese legal format (**UBL2.1**, **CIUS-PT** and **XML**), to **B2G** & **B2B** customers (receivers).
- Send PDF invoices with a qualified digital certificate, to **B2B** & **B2C** customers (receivers).

## Purpose
The purpose of our API is to offer a standardized method to send invoices (legal format and PDF) programmatically.  
By leveraging our API, developers can seamlessly integrate e-invoicing capabilities into their software applications, improving billing efficiency and reducing manual processes associated with traditional invoicing methods.

Our RESTful interface is designed to streamline the process of sending and managing electronic invoices for businesses of all sizes.

**This technical guide**:
- serves as a blueprint for seamlessly integrating any software with the Saphety Invoice Network API, empowering your billing system with the full capabilities of this API.
- aims to provide comprehensive information and guidance on integrating our API into your applications for efficient e-invoicing solutions, so, after reading this book you should be able to fully automate any system integration with "Saphety Invoice Network API".

## Legal Framework
**Electronic invoices**  
In Portugal, the obligation to send electronic invoices for public entities is regulated by **Law-decree no. 123/2018, of December 28**, which was transposed into national legislation by **Directive 2014/55/EU** of the **European Parliament and of the Council**, relating electronic invoicing in public contracts.

This obligation applies to large companies from **January 1st/2021**, and for small, medium and micro companies from **January 1st/2024**.

Technical specifications for UBL2.1 CIUS-PT XML format was defined by eSPap and they are published here: [eSPap - SPFin - Fatura Eletrónica ](https://www.espap.gov.pt/FrontEnd/Paginas/Areas/SP_Fin/SP_Fin_NormasFEAP_tpl_1.aspx)  

**PDF invoices**
From **January 1st/2024**, sending invoices in PDF format, must be done using the authentication of documents through a **Qualified Digital Certificate**, otherwise, they cease to have legal validity.

To ensure compliance with this legal obligation (**Law-decree no. 28/2029**), Sovos/Saphety provides electronic signature service with a qualified certificate, which will ensure the authentication of all PDF invoices sent by your company.