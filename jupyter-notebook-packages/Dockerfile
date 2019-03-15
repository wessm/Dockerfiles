# based on base image
FROM wessm/jupyter-notebook-r

LABEL maintainer="Michael Wess <michael.wess@boku.ac.at>"

USER root

RUN	add-apt-repository 'deb http://mirror.ibcp.fr/pub/CRAN/bin/linux/ubuntu bionic/' && \
	apt-get update -y && \
	apt-get upgrade -y && \
	apt-get build-dep python-gdal -y && \
	apt-get install -y \
		libgdal1-dev \
		libproj-dev \
		libgeos-dev \
		libgdal-dev \
		libgdal1i \
		libv8-3.14-dev \
		python-gdal && \
	apt-get clean autoclean && \
	apt-get autoremove -y && \
	rm -rf /var/lib/apt/lists/*

USER $NB_USER

RUN conda install GDAL -y && \
	pip install mapboxgl && \
	jupyter nbextension enable code_prettify/autopep8 && \
	jupyter nbextension enable varInspector/main && \
	jupyter nbextension enable codefolding/main && \
	jupyter nbextension enable hinterland/hinterland && \
	jupyter nbextension enable runtools/main && \
	jupyter nbextension enable scratchpad/main
