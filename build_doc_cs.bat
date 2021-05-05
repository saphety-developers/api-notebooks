call conda activate api-notebooks

call jupyter-book build doc-server\certified-software
call Xcopy /E .\doc-server\certified-software\_build\html ..\doc-client\src\assets\api-docs\certified-software\