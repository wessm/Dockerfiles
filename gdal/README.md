# gdal

based on the [GDAL-Docker](https://github.com/geo-data/gdal-docker) images; just added the gdalcopyproj.py function to copy projections


```
docker run -it --rm \
    -v ${HOME}:/data \
    wessm/gdal gdalcopyproj.py [data]
```

