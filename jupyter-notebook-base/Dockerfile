# based on official jupyter image, modified for me
FROM jupyter/scipy-notebook

LABEL maintainer="Michael Wess <michael.wess@boku.ac.at>"

USER root

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && \
	apt-get upgrade -y && \
	apt-get install -y --no-install-recommends \
		software-properties-common \
		apt-utils \
		dirmngr \
		gpg-agent && \
	apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
	apt-add-repository "deb http://cran.rstudio.com/bin/linux/ubuntu $(lsb_release -sc)-cran35/" -y &&  \
    	add-apt-repository ppa:ubuntugis/ubuntugis-unstable && \
  	apt-get update && \
  	apt-get install --no-install-recommends -y \
		libjq-dev \
		software-properties-common \
		apt-utils \
		libreadline-dev \
		libgdal20 \
    	libgeos-dev \
		exiftool \
		libgdal-dev \
   		imagemagick \
    	fonts-dejavu \
    	tzdata \
    	gfortran \
		postgis \
		gdal-bin \
    	gcc && \
    apt-get clean autoclean && \
	apt-get autoremove -y && \
	rm -rf /var/lib/apt/lists/* && \
	printf '{"NotebookApp": {"password": "sha1:9c7660f55344:3ba6b9bdb6696defb487e4b14d15985251b28afd"}}' >> /home/jovyan/.jupyter/jupyter_notebook_config.json && \
	conda install --yes \
    	'nb_conda' \
		'conda-build' \
		'line_profiler' && \
    conda install --channel conda-forge --yes \
		'jupyter_contrib_nbextensions' && \
	conda build purge-all && \
	conda clean --all && \
	fix-permissions $CONDA_DIR && \
	pip install \
		psycopg2-binary \
		pyshp \
		geopandas \
		shapely \
		imutils \
		cython \
		fortran-magic \
		autopep8 yapf && \
	cd /tmp && \
	git clone git://github.com/smarnach/pyexiftool.git && \
    cd pyexiftool && \
	python setup.py install && \
    cd .. && \
	rm -rf pyexiftool

