# jupyter-notebook-base

fully functional jupyter notebook, based on [jupyter/scipy-notebook](https://hub.docker.com/r/jupyter/scipy-notebook/)


icludes:

* R
* gdal
* imagemagick
* contrib-extension for juptyter-notebook

runs as user jovyan

can be run e.g. with

```
docker run --rm -it \
    -p 8888:8888 \
    -v ${HOME}:/home/jovyan/work \
    wessm/jupyter-notebook-opencv
```
