#!/bin/bash

USER_ID=`ls -lahn /home | tail -1 | awk {'print $3'}`
GROUP_ID=`ls -lahn /home | tail -1 | awk {'print $4'}`
USER_NAME=`ls -lah /home/ | tail -1 | awk '{print $9}'`

sudo groupadd -g $GROUP_ID qgis
#sudo useradd --shell /bin/bash --uid $USER_ID --gid $GROUP_ID $USER_NAME
export LD_LIBRARY_PATH=/usr/lib
sudo /usr/bin/qgis
