##
# geodata/gdal
#

# Ubuntu 14.04 Trusty Tahyr
FROM ubuntu:trusty

LABEL maintainer="Michael Wess <michael.wess@boku.ac.at>"

# Install the application.
ADD . /usr/local/src/gdal-docker/
ADD gdalcopyproj.py /usr/bin/
RUN chmod +x /usr/bin/gdalcopyproj.py && /usr/local/src/gdal-docker/build.sh

# Externally accessible data is by default put in /data
WORKDIR /data
VOLUME ["/data"]

# Output version and capabilities by default.
CMD gdalinfo --version && gdalinfo --formats && ogrinfo --formats
