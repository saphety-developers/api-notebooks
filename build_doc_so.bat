call conda activate api-notebooks

call jupyter-book build doc-server\services-overview
call Xcopy /E .\doc-server\services-overview\_build\html ..\doc-client\src\assets\api-docs\services-overview\