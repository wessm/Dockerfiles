# qgis3

QGIS3 from [QGIS.org](http://qgis.org)

runs as user mischa

```
xhost +
docker run --rm --name qgis3 \
    -it \
    -v ${HOME}:/home/mischa \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --network host \
    --privileged \
    -e DISPLAY=unix$DISPLAY \
    wessm/qgis3
xhost -
```
