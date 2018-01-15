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
    apt-get install -y --no-install-recommends libgeos-dev exiftool && \
    apt-get install -y --no-install-recommends imagemagick \
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
    conda clean -tipsy && fix-permissions $CONDA_DIR && \
	conda install --channel conda-forge --yes 'jupyter_contrib_nbextensions'

