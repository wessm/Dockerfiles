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
    apt-get install -y --no-install-recommends r-base r-recommended imagemagick && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_USER

# use notebook-friendly backends in these images
RUN conda install --yes \
    'nb_conda' && \
    conda install --channel conda-forge --yes 'opencv' && \
    conda clean -tipsy && \
    conda install --channel r r-essentials && \
    pip install rpy2 imutils cython fortran-magic

RUN cd /tmp && git clone git://github.com/smarnach/pyexiftool.git && \
	cd pyexiftool && python setup.py install && \
	rm -rf pyexiftool

RUN conda install --channel conda-forge --yes 'jupyter_contrib_nbextensions'

USER $NB_USER

