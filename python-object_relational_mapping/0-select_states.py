
import MySQLdb

def list_states(username, password, database):
    conn = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    results = cursor.fetchall()
    for result in results:
        print(result)
    cursor.close()
    conn.close()
if __name__ == '__main__':
    list_states('root', 'root', 'hbtn_0e_0_usa')
