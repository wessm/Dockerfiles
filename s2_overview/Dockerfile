FROM ubuntu:16.04

LABEL maintainer="Michael Wess <michael.wess@boku.ac.at>"

USER root

RUN apt-get update -y && \
	apt-get upgrade -y && \
	apt-get install -y --no-install-recommends \
		postgis \
		gcc \
		gdal-bin \
		libgdal-dev \
		libgeos-dev \
		python-dev \
		libpython-dev \
		libproj-dev \
		python-gdal \
		wget \
		sudo \
		python-pip \
		imagemagick && \
	apt-get clean autoclean && \
	apt-get autoremove -y && \
	rm -rf /var/lib/apt/lists/*


RUN useradd --password 'password' \
	--uid 1000 \
	--create-home \
	--no-log-init \
	--shell /bin/bash \
	mischa

RUN adduser mischa sudo

USER mischa

WORKDIR /home/mischa

RUN cd ~ && \
	wget http://download.redis.io/redis-stable.tar.gz && \
	tar xvzf redis-stable.tar.gz && \
	cd redis-stable && \
	make

USER root

RUN cd /home/mischa/redis-stable && \
	make install

RUN pip install --upgrade pip && \
	pip install setuptools && \
	apt-get update -y && \
	apt-get install -y --no-install-recommends \
		dpkg-dev \
		g++ \
		libc6-dev \
		make \
		python3-dev \
		python3-pip \
		libgcc1 \
		libxml2-dev \
		zlib1g-dev


RUN pip install \
	redis \
	huey \
	psycopg2-binary \
	imutils \
	shapely \
	rasterstats \
	fiona \
	pygeoj \
	gdal \
	geopandas \
	pyshp \
	sentinelhub \
	sentinelsat


USER mischa


ADD *.py /home/mischa/
ADD *.cfg /home/mischa/

RUN mkdir /home/mischa/s2overview

#CMD ["redis-server","--daemonize","yes"]
ENTRYPOINT /usr/local/bin/redis-server --daemonize yes && /usr/local/bin/huey_consumer.py download_overview_for_tile.huey -k process -w 1 --logfile=/home/mischa/huey.log
#ENTRYPOINT /bin/bash


