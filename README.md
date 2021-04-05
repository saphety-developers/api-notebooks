# Saphety Api-notebooks
#Requirements
- Anaconda: https://docs.anaconda.com/anaconda/install/
- Jupyter-Lab: https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
- Have a environment with 3.7 version of Python (See in #Environments)

*For the next actions, please run "Anaconda Prompt"*
#Environments
- Create: conda create -n api-notebooks python=3.7 -y
- Select: conda activate api-notebooks
- Install jupyter-book: pip install jupyter-book pandas plotly sphinx-thebe

- Intall jupyter-lab: conda install -c conda-forge jupyterlab

#Jupyter-Book
- Create: jupyter-book create new-book

#Jupyter-Lab
- Run:
	> D:
	> cd Git\api-notebooks
	> jupyter-lab
	
- Build:
	Double-click on "build.bat"

	OR MANUAL Build
	
	> D:
	> cd Git\api-notebooks
	> conda activate api-notebooks
	> jupyter-lab build folder-name
	
	OR AUTO Build
	
	> D:
	> cd Git\api-notebooks
	> build
	
	Last command example: > jupyter-lab build dcn-sandbox
	This command will build our books, creating a new folder "_build" on your selected folder
	
#Commit to GitHub - command
> D:
> cd Git\api-notebooks
> git push github master
