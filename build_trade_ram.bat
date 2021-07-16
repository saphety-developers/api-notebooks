call conda activate api-notebooks

call jupyter-book build trade\rest-api-messaging
call Xcopy /E .\trade\rest-api-messaging\_build\html ..\doc-client\src\assets\api-docs\rest-api-messaging\