# based on base image
FROM wessm/jupyter-notebook-base

LABEL maintainer="Michael Wess <michael.wess@boku.ac.at>"

USER root

RUN	add-apt-repository 'deb http://mirror.ibcp.fr/pub/CRAN/bin/linux/ubuntu bionic-cran35/' && \
	apt-get update -y && \
	apt-get upgrade -y && \
	apt-get build-dep python-gdal -y && \
	apt-get install -y \
		equivs && \
	printf "Section: misc\nPriority: optional\nStandards-Version: 3.9.2\n\nPackage: gdal-abi-2-2-3\nVersion: 2.2.3\nDepends: libgdal20\nDescription: fake package for qgis which needs a gdal-abi-2-2-3\n" >> gdal_abi.txt && \
	cat gdal_abi.txt && \
	sudo equivs-build gdal_abi.txt && \
	sudo dpkg -i gdal-abi-2-2-3_2.2.3_all.deb && \
	rm -f gdal* && \
	apt-get install -y \
		libproj-dev \
		libgeos-dev \
		libgdal-dev \
		dans-gdal-scripts \
		libv8-3.14-dev \
		nvidia-cuda-toolkit \
		python-gdal && \
	apt-get clean autoclean && \
	apt-get autoremove -y && \
	rm -rf /var/lib/apt/lists/*

USER $NB_USER

RUN conda install GDAL cudatoolkit cudnn -y && \
	pip install mapboxgl && \
	jupyter nbextension enable code_prettify/autopep8 && \
	jupyter nbextension enable varInspector/main && \
	jupyter nbextension enable codefolding/main && \
	jupyter nbextension enable hinterland/hinterland && \
	jupyter nbextension enable runtools/main && \
	jupyter nbextension enable scratchpad/main
