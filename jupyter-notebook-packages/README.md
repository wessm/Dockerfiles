# jupyter-notebook-packages

jupyter notebook with lots of packages and modules, based on my [jupyter-notebook-base](https://hub.docker.com/r/wessm/jupyter-notebook-base/)


runs as user jovyan

can be run e.g. with

```
docker run --rm -it \
    -p 8888:8888 \
    -v ${HOME}:/home/jovyan/work \
    wessm/jupyter-notebook-packages
```
