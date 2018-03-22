# jupyter-notebook-packages

jupyter notebook with lots of packages and modules

runs as user jovyan

can be run e.g. with

```
docker run --rm -it \
    -p 8888:8888 \
    -v ${HOME}:/home/jovyan/work \
    wessm/jupyter-notebook-packages
```
