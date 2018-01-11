# based on official jupyter image, modified for me
FROM jupyter/scipy-notebook

LABEL maintainer="Michael Wess <michael.wess@boku.ac.at>"

USER root

# libav-tools for matplotlib anim
RUN apt-get update -y && \
    apt-get --yes --no-install-recommends install software-properties-common libreadline-dev && \
    apt-add-repository "deb http://cran.rstudio.com/bin/linux/ubuntu $(lsb_release -sc)/" -y &&  \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
    apt-add-repository ppa:marutter/rdev -y && \
    apt-get update && \
    apt-get install -y --no-install-recommends exiftool && \
    apt-get install -y --no-install-recommends r-base r-recommended imagemagick \
	fonts-dejavu \
    tzdata \
    gfortran \
	gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_USER

# use notebook-friendly backends in these images
RUN conda install --yes \
    'nb_conda' 'line_profiler' && \
    conda install --channel conda-forge --yes 'opencv' && \
	conda install --quiet --yes \
    'r-base=3.3.2' \
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
	'r-randomforest=4.6*' && \
    conda clean -tipsy && fix-permissions $CONDA_DIR && \
    pip install rpy2 imutils cython fortran-magic

RUN cd /tmp && git clone git://github.com/smarnach/pyexiftool.git && \
	cd pyexiftool && python setup.py install && \
	rm -rf pyexiftool

RUN conda install --channel conda-forge --yes 'jupyter_contrib_nbextensions'

USER $NB_USER

