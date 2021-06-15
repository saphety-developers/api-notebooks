call conda activate api-notebooks

call jupyter-book build doc-server\document-search
call Xcopy /E .\doc-server\document-search\_build\html ..\doc-client\src\assets\api-docs\document-search\