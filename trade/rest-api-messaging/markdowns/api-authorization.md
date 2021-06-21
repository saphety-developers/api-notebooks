# API Authorization
These services use Basic Authentication.
To obtain your authentication data please contact you project manager in Saphety.

The authentication data provided by Saphety will be as following:
- **UserId:** \<Contr Code>\<VAT> (ie: PT507957547)
- **Password:** \<Secure_Password>, (ie:Saph3tY#_2019)

The following example illustrates how to build your authorization header:
- 1. Concatenate your \<UserId> with \<“:”> and your \<Password>
- 2. Convert the resulting value into base64