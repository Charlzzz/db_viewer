import psycopg2
from psycopg2 import connect


def conn(dbname, user, password, host, port):

    # con = connect(dbname='test', user='postgres',
    #               password='0ziro0', host='127.0.0.1', port='5432')
    con = connect(dbname=dbname, user=user,
                  password=password, host=host, port=port)
    try:
        cur = con.cursor()
        cur.execute('select * from users')
    except psycopg2.DatabaseError as err:
        print("wtf")
        return False
    else:
        print('all right')
        add_db_to_text(dbname, user, password, host, port)
        con.close()
        return True

def add_db_to_text(dbname, user, password, host, port):
    list_db = [dbname, user, password, host, port]
    with open('D:\\list_db_viewer.txt', 'a', encoding='utf-8') as prop_db:
        prop_db.write(' '.join(list_db) + '\n')
        prop_db.close()



