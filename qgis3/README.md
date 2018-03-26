# qgis

QGIS from [QGIS.org](http://qgis.org)

runs as user mischa

```
xhost +
docker run --rm --name qgis \
    -it \
    -v ${HOME}:/home/mischa \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e DISPLAY=unix$DISPLAY \
    wessm/qgis
xhost -
```
