call conda activate api-notebooks

call jupyter-book clean -a dcn
call jupyter-book build dcn
call Xcopy /E .\dcn\_build\html ..\dcn-client\src\assets\api-docs\