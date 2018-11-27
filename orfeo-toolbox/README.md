# orfeo

orfeo toolbox from [ubuntugis-unstable](https://launchpad.net/~ubuntugis/+archive/ubuntu/ubuntugis-unstable)

```
docker run --rm -it \
    -v ${HOME}:/home/data \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e DISPLAY=unix$DISPLAY \
    wessm/orfeo
```
