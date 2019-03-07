# based on official jupyter image, modified for me
FROM jupyter/scipy-notebook

LABEL maintainer="Michael Wess <michael.wess@boku.ac.at>"

USER root

# libav-tools for matplotlib anim
RUN apt-get update -y && \
	apt-get upgrade -y && \
	apt-get install -y --no-install-recommends \
		software-properties-common \
		apt-utils && \
	apt-add-repository "deb http://cran.rstudio.com/bin/linux/ubuntu $(lsb_release -sc)/" -y &&  \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
	add-apt-repository ppa:ubuntugis/ppa && \
    apt-add-repository ppa:marutter/rdev -y && \
	add-apt-repository -y ppa:opencpu/jq && \
	add-apt-repository ppa:johanvdw/saga-gis -y && \
  	apt-get update && \
  	apt-get install --no-install-recommends -y \
		libjq-dev \
		saga \
		software-properties-common \
		apt-utils \
		libreadline-dev \
		dans-gdal-scripts \
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
	apt-get autoremove -y
    #rm -rf /var/lib/(apt,dpkg,cache,log)/

USER $NB_USER

# use notebook-friendly backends in these images
RUN conda install --yes \
    	'nb_conda' \
		'line_profiler' && \
    conda clean -tipsy && \
	fix-permissions $CONDA_DIR && \
    conda install --channel conda-forge --yes \
		'jupyter_contrib_nbextensions' && \
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

