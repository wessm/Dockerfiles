# based on packages notebook
FROM wessm/jupyter-notebook-packages

LABEL maintainer="Michael Wess <michael.wess@boku.ac.at>"

#USER root

#RUN	add-apt-repository 'deb http://mirror.ibcp.fr/pub/CRAN/bin/linux/ubuntu xenial/' && \
#	apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
#	apt-get update -y && \
#	apt-get upgrade -y && \
#	apt-get build-dep python-gdal -y && \
#	apt-get install -y \
#		libgdal1-dev \
#		libproj-dev \
#		libgeos-dev \
#		libgdal-dev \
#		libgdal1i \
#		libv8-3.14-dev \
#		python-gdal && \
#	apt-get clean autoclean && \
#	apt-get autoremove -y && \
#	rm -rf /var/lib/apt/lists/*

USER $NB_USER

RUN pip install gdal \
		rasterstats \
		fiona \
		shapely

