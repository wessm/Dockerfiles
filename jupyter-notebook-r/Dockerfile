# based on base image
FROM wessm/jupyter-notebook-base:latest

LABEL maintainer="Michael Wess <michael.wess@boku.ac.at>"

USER $NB_USER

RUN	conda install --channel conda-forge --yes \
    'opencv' && \
    conda install --quiet --channel r --yes \
    'r-raster' \
    'r-base' \
    'r-irkernel=0.7*' \
    'r-plyr=1.8*' \
    'r-devtools=1.12*' \
    'r-tidyverse=1.0*' \
    'r-shiny=0.14*' \
    'r-rmarkdown=1.2*' \
    'r-forecast=7.3*' \
    'r-rsqlite=1.1*' \
    'r-reshape2=1.4*' \
    'r-nycflights13=0.2*' \
    'r-caret=6.0*' \
    'r-rcurl=1.95*' \
    'r-crayon=1.3*' \
    'r-randomforest=4.6*' \
    'r-hexbin=1.27*' \
    'r-rgeos' \
    'r-jsonlite' \
    'r-rcurl' \
    'r-plyr' && \
    conda clean -tipsy && fix-permissions $CONDA_DIR && \
    pip install rpy2
	#Rscript -e 'install.packages("geojsonio", repo="https://cran.r-project.org/")'
