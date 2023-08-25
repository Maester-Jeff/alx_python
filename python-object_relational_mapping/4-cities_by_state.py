
import MySQLdb


def list_cities(username, password, database):
    try:
        conn = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cities ORDER BY id ASC")
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        conn.close()
    except MySQLdb.Error as e:
        print("Error connecting to MySQL database: {}".format(e))


if __name__ == '__main__':
    list_cities('username', 'password', 'database_name')
