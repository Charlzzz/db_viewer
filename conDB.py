import psycopg2
from psycopg2 import connect


def conn():
    con = connect(
    dbname='test', user='postgres',
    host='localhost', password='0ziro0')
    try:
        cur = con.cursor()
        cur.execute('select * from users')
    except psycopg2.DatabaseError as err:
        return False
    else:
        con.close()
        return True

def get_prop()