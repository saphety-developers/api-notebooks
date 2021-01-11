call conda activate api-notebooks

call jupyter-book build dcn-sandbox
call Xcopy /E .\dcn-sandbox\_build\html ..\dcn-sandbox-client\src\assets\api-docs\