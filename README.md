# NbGrader

## Elevinstallation
pip install nbgrader
jupyter nbextension install --sys-prefix --py nbgrader --overwrite
jupyter nbextension enable --sys-prefix --py nbgrader
jupyter serverextension enable --sys-prefix --py nbgrader
jupyter nbextension disable –sys-prefix assignment_list/main –section=tree
jupyter serverextension disable –sys-prefix nbgrader.server_extensions.assignment_list
jupyter nbextension disable --sys-prefix create_assignment/main
jupyter nbextension disable --sys-prefix formgrader/main --section=tree
jupyter serverextension disable --sys-prefix nbgrader.server_extensions.formgrader

## Lärarinstallation
pip install nbgrader
jupyter nbextension install --sys-prefix --py nbgrader --overwrite
jupyter nbextension enable --sys-prefix --py nbgrader
jupyter serverextension enable --sys-prefix --py nbgrader