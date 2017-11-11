FROM ubuntu:16.04

ENV TERM linux
ENV DEBIAN_FRONTEND noninteractive

LABEL maintainer="Michael Wess <michael.wess@boku.ac.at>"

RUN apt-get update -y && apt-get install -y --no-install-recommends apt-utils sudo && apt-get install -y --no-install-recommends nano wget software-properties-common python-software-properties

RUN echo "deb http://qgis.org/debian xenial main" >> /etc/apt/sources.list
RUN echo "deb-src http://qgis.org/debian xenial main " >> /etc/apt/sources.list
RUN wget -O - http://qgis.org/downloads/qgis-2017.gpg.key | gpg --import
RUN gpg --fingerprint CAEB3DC3BDF7FB45
RUN gpg --export --armor CAEB3DC3BDF7FB45 | sudo apt-key add -


RUN apt-get update -y && apt-get install qgis python-qgis -y

# Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/mischa && \
    echo "mischa:x:${uid}:${gid}:mischa,,,:/home/mischa:/bin/bash" >> /etc/passwd && \
    echo "mischa:x:${uid}:" >> /etc/group && \
    echo "mischa ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/mischa && \
    chmod 0440 /etc/sudoers.d/mischa && \
    chown ${uid}:${gid} -R /home/mischa

USER mischa
ENV HOME /home/mischa





ENV QGIS_DEBUG 5
ENV QGIS_LOG_FILE /proc/self/fd/1
ENV PGSERVICEFILE /project/pg_service.conf
ENV QGIS_PROJECT_FILE /project/project.qgs

ADD start.sh /start.sh
RUN sudo chmod +x /start.sh
CMD ["/start.sh"]


