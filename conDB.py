import psycopg2
from psycopg2 import connect

class ConnectDB():
    def __init__(self, dbname, user, password, host, port):

        # con = connect(dbname='test', user='postgres',
        #               password='0ziro0', host='127.0.0.1', port='8080')
        con = connect(dbname=dbname, user=user,
                      password=password, host=host, port=port)
        try:
            cur = con.cursor()
            cur.execute('select * from users')
        except psycopg2.DatabaseError as err:
            return False
        else:
            con.close()
            return True

