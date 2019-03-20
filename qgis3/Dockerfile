FROM ubuntu:18.04

ENV TERM linux
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

LABEL maintainer="Michael Wess <michael.wess@boku.ac.at>"

USER root

RUN apt-get update -y && \
	apt-get install -y --no-install-recommends \
		apt-utils \
		sudo \
		nano \
		wget \
		mesa-utils \
		libgl1-mesa-glx \
		software-properties-common \
		gpg-agent && \
	echo "deb http://qgis.org/debian bionic main" >> /etc/apt/sources.list && \
	echo "deb-src http://qgis.org/debian bionic main " >> /etc/apt/sources.list && \
	wget -O - http://qgis.org/downloads/qgis-2017.gpg.key | gpg --import && \
	gpg --fingerprint CAEB3DC3BDF7FB45 && \
	gpg --export --armor CAEB3DC3BDF7FB45 | sudo apt-key add - && \
	apt-get update -y && \
	apt-get install -y --no-install-recommends \
		qgis \
		qgis-providers \
		nvidia-384 \
		nvidia-settings \
		python-qgis && \
	export uid=1000 gid=1000 && \
    mkdir -p /home/mischa && \
    echo "mischa:x:${uid}:${gid}:mischa,,,:/home/mischa:/bin/bash" >> /etc/passwd && \
    echo "mischa:x:${uid}:" >> /etc/group && \
    echo "mischa ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/mischa && \
    chmod 0440 /etc/sudoers.d/mischa && \
    chown ${uid}:${gid} -R /home/mischa && \
	apt-get clean && \
	apt-get purge && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER mischa
ENV HOME /home/mischa

ENV QGIS_DEBUG 5
ENV QGIS_LOG_FILE /proc/self/fd/1
ENV PGSERVICEFILE /project/pg_service.conf
ENV QGIS_PROJECT_FILE /project/project.qgs

ADD start.sh /start.sh
RUN sudo chmod +x /start.sh
CMD ["/start.sh"]


