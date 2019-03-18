# based on base image
FROM wessm/jupyter-notebook-base:latest

LABEL maintainer="Michael Wess <michael.wess@boku.ac.at>"

USER $NB_USER

RUN	conda install --channel conda-forge --yes \
    'opencv' && \
    conda install --quiet --channel r --yes \
    'r-raster' \
    'r-base' \
    'r-irkernel' \
    'r-plyr' \
    'r-devtools' \
    'r-tidyverse' \
    'r-shiny' \
    'r-rmarkdown' \
    'r-forecast' \
    'r-rsqlite' \
    'r-reshape2' \
    'r-nycflights13' \
    'r-caret' \
    'r-rcurl' \
    'r-crayon' \
    'r-randomforest' \
    'r-hexbin' \
    'r-rgeos' \
    'r-jsonlite' \
    'r-rcurl' \
    'r-plyr' && \
    fix-permissions $CONDA_DIR && \
    pip install rpy2
