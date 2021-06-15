call conda activate api-notebooks

call jupyter-book build doc-server\pull-integration
call Xcopy /E .\doc-server\pull-integration\_build\html ..\doc-client\src\assets\api-docs\pull-integration\