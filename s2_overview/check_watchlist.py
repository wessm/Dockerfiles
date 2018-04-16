import psycopg2
import datetime
from download_overview_for_tile import download_overview_for_tile



def check_watchlist():


    password = '4G5K8y3rTz5cHNJF'
    user = 'mwess'

    DB_NAME = 'postgres'
    DB_HOST = 'localhost'
    DB_USER = 'mischa'
    DB_PW = 'mysecretpassword'
    DB_SCHEMA = 'S2basics'


    TBL_NAME = 'watched_tiles'

    folder = '/home/mischa/s2overview'

    connection = psycopg2.connect(host=DB_HOST, database=DB_NAME,user=DB_USER, password=DB_PW)
    cursor = connection.cursor()

    cursor.execute('SELECT date_from, date_to, tile_id FROM {0}.{1} ORDER BY last_checked ASC LIMIT 1'.format(DB_SCHEMA, TBL_NAME))
    res = cursor.fetchone()

    if res is not None:

        download_overview_for_tile(res[2], res[0], res[1])

        cursor.execute('UPDATE {0}.{1} SET last_checked = \'{2}\' '
                       'WHERE tile_id = \'{3}\''.format(DB_SCHEMA, TBL_NAME,
                        datetime.datetime.utcnow(), res[2]))
        connection.commit()





    connection.close()

if __name__ == '__main__':
    check_watchlist()
