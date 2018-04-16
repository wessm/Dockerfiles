from huey import RedisHuey, crontab
import psycopg2
import sentinelsat
from collections import OrderedDict
import os
import re
import time
import requests
import subprocess
import shlex
import ConfigPaeser

#  initialize huey
huey = RedisHuey('download_overview_for_tile')


def load_config(section, key):
    Config = ConfigParser()
    Config.read('./config.cfg')
    return Config.get(section, key)






def download_file(url, local_filename):
    #local_filename = '/home/jovyan/work/Projects/S2_basics/' + url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

@huey.task()
def download_overview_for_tile(tile, date_from, date_to):


    S2_USER = load_config('S2', 'USER')
    S2_PASSWORD = load_config('S2', 'PASSWORD')




    DB_NAME = load_config('PostGIS', 'DB_NAME')
    DB_HOST =  load_config('PostGIS', 'BH_HOST')
    DB_USER = load_config('PostGIS', 'DB_USER')
    DB_PW  load_config('PostGIS', 'DB_PW')
    DB_SCHEMA = load_config('PostGIS', 'DB_SCHEMA')

    TBL_NAME = load_config('PostGIS', 'TBL_NAME_OVERVIEW')

    folder = load_config('general', 'BASE_FOLDER')


    query_kwargs = {
        'platformname': 'Sentinel-2',
        'producttype': 'S2MSI1C',
        'date': (date_from, date_to) }




    api = sentinelsat.SentinelAPI(S2_USER, S2_PASSWORD, 'https://scihub.copernicus.eu/dhus')


    products = OrderedDict()
    kw = query_kwargs.copy()
    kw['tileid'] = tile
    pp = api.query(**kw)
    products.update(pp)

    products = list(products.items())

    for p in products:
        tileid = p[1]['tileid']

        nr = re.findall('\d+', tileid)[0]
        strn = tileid.replace(nr, '')
        t1 = strn[0]
        t2 = strn[1:]

        footprint = p[1]['footprint']
        date = p[1]['datatakesensingstart']





        connection = psycopg2.connect(host=DB_HOST, database=DB_NAME,user=DB_USER, password=DB_PW)
        cursor = connection.cursor()

        #  check if it is already in table
        cursor.execute('SELECT uuid from {0}.{1} WHERE uuid = \'{2}\''.format(
            DB_SCHEMA, TBL_NAME, p[0]))
        res = cursor.fetchone()

        if res is None:



            base_url = 'http://sentinel-s2-l1c.s3-website.eu-central-1.amazonaws.com/tiles'

            url = '{0}/{1}/{2}/{3}/{4}/{5}/{6}/0/preview.jp2'.format(base_url,
               nr, t1, t2, date.year, date.month, date.day)

            r = requests.get(url)


            if r.status_code == 200:




                print('downloading {0}'.format(p[0]))
                download_file(url, '{0}/tmp.jp2'.format(folder))

                subfolder = '{0}/{1}/{2}/{3}/{4}/{5}/0'.format(nr,
                                    t1, t2, date.year, date.month, date.day)

                if not os.path.exists('{0}/{1}'.format(folder, subfolder)):
                    os.makedirs('{0}/{1}'.format(folder, subfolder))

                filename = '{0}_{1}.tif'.format(tileid, date.strftime('%Y%m%dT%H-%H-%S'))


                with open(os.devnull, 'wb') as devnull:
                    subprocess.check_call(shlex.split(
                        '/usr/bin/gdalwarp -q -t_srs epsg:4326 -r cubic -ot Byte '
                               '-dstnodata "0 0 0" -co "COMPRESS=LZW" -overwrite '
                               '{0}/tmp.jp2 {0}/{1}/{2}'.format(folder,
                               subfolder, filename)), stdout=devnull, stderr=devnull)

                os.remove('{0}/tmp.jp2'.format(folder))


                if os.path.exists('{0}/{1}/{2}'.format(folder, subfolder, filename)):
                    cursor.execute('INSERT INTO {12}.{13} ('
                            'uuid, '
                            'time, '
                            'product_filename, '
                            'cloudcover, '
                            'orbitdirection, '
                            'size, '
                            'tile_id, '
                            'orbitnumber, '
                            'relativeorbitnumber, '
                            'datatakeid, '
                            'identifier, '
                            'footprint, filename) VALUES (\'{0}\', \'{1}\', \'{2}\', '
                               '{3}, \'{4}\', \'{5}\', \'{6}\', {7}, {8}, '
                               '\'{0}\', \'{10}\', ST_GeomFromText(\'{11}\', '
                               '4326), \'{14}\')'.format(
                                p[0],
                                p[1]['datatakesensingstart'],
                                p[1]['filename'],
                                p[1]['cloudcoverpercentage'],
                                p[1]['orbitdirection'],
                                p[1]['size'],
                                tileid,
                                p[1]['orbitnumber'],
                                p[1]['relativeorbitnumber'],
                                p[1]['s2datatakeid'],
                                p[1]['identifier'],
                                p[1]['footprint'],
                                DB_SCHEMA,
                                TBL_NAME,
                                filename
                            ))

                    connection.commit()
                time.sleep(1)
            else:
                print('{0} already exists in table'.format(p[0]))


    if connection:
        connection.close()





