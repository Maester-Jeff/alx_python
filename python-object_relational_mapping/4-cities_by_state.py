
import MySQLdb


def list_cities(username, password, database):
        conn = MySQLdb.connect(
            host="localhost", 
            port=3306, 
            user=username, 
            passwd=password, 
            db=database
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cities ORDER BY id ASC")
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        conn.close()

if __name__ == '__main__':
    list_cities('username', 'password', 'database')
