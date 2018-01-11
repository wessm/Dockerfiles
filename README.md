# Dockerfiles

Dockerfile repo; automatically built at https://hub.docker.com/u/wessm/







## jupyter-notebook-opencv

based on jupyter/scipy-notebook;

icludes:
* opencv from conda-forge
* R + python bindings
* exiftool + python bindings
* imagemagick
* cython
* conda extension for juptyter-notebook

runs as user jovyan


can be run e.g. with

```
docker run --rm -it \
	-p 8888:8888 \
	-v ${HOME}:/home/jovyan/work \
    wessm/jupyter-notebook-opencv
```




## qgis

QGIS from http://qgis.org

runs as user mischa

```
xhost +
docker run  --rm --name qgis \
	-i -t \
	-v ${HOME}:/home/mischa \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-e DISPLAY=unix$DISPLAY \
	wessm/qgis
xhost -
```




## orfeo

orfeo toolbox from ubuntugis-unstable


```
docker run --rm -it \
	-v ${HOME}:/home/data \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-e DISPLAY=unix$DISPLAY \
    wessm/orfeo
```
