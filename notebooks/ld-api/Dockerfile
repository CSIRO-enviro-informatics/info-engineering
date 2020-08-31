ARG JUPYTER_IMAGE=jupyter/minimal-notebook:54462805efcb
FROM $JUPYTER_IMAGE
#FROM jupyter/minimal-notebook

USER root
RUN apt-get install -y build-essential gcc
RUN apt-get update
RUN apt-get install -y  libpq-dev python-dev
RUN apt install -y  graphviz

USER jovyan


# Add permanent pip/conda installs, data files, other user libs here
# e.g., RUN pip install jupyter_dashboards
COPY requirements.txt /tmp/
RUN ls /tmp
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt
RUN python -m pip install jupyterthemes
RUN python -m pip install --upgrade jupyterthemes
RUN python -m pip install jupyter_contrib_nbextensions
RUN jupyter contrib nbextension install --user
# enable the Nbextensions
RUN jupyter nbextension enable contrib_nbextensions_help_item/main
RUN jupyter nbextension enable autosavetime/main
RUN jupyter nbextension enable codefolding/main
RUN jupyter nbextension enable code_font_size/code_font_size
RUN jupyter nbextension enable code_prettify/code_prettify
RUN jupyter nbextension enable collapsible_headings/main
RUN jupyter nbextension enable comment-uncomment/main
RUN jupyter nbextension enable gist_it/main
RUN jupyter nbextension enable hide_input/main
RUN jupyter nbextension enable spellchecker/main
RUN jupyter nbextension enable toggle_all_line_numbers/main


# Add notebooks to the docker image
#COPY *.ipynb /home/jovyan/
#COPY *.csv /home/jovyan/
#COPY env-template /home/jovyan/.env


USER root

# Add permanent apt-get installs and other root commands here
# e.g., RUN apt-get install npm nodejs
