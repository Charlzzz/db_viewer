import psycopg2
from psycopg2 import connect


def conn(dbname, user, password, host, port):

    try:
        con = connect(dbname=dbname, user=user,
                      password=password, host=host, port=port)

        cur = con.cursor()
        cur.execute('select * from users')
    except psycopg2.DatabaseError as err:
        print("wtf")
        # con.close()
        return False
    else:
        print('all right')
        # add_db_to_text(dbname, user, password, host, port)
        con.close()
        return True

def add_db_to_text(dbname, user, password, host, port):
    list_db = [dbname, user, password, host, port]
    with open('D:\\list_db_viewer.txt', 'a', encoding='utf-8') as prop_db:
        prop_db.write(' '.join(list_db) + '\n')
        prop_db.close()



