#  geodata/gdal as base image
FROM geodata/gdal

LABEL maintainer="Michael Wess <michael.wess@boku.ac.at>"

# use gdalcopyproj
ADD gdalcopyproj.py /usr/bin/
RUN chmod +x /usr/bin/gdalcopyproj.py


RUN useradd -ms /bin/bash mischa
USER mischa
