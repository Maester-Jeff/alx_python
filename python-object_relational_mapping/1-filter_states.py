'''
import MySQLdb
import sys

def list_states(username, password, database):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        
        # Create a cursor to interact with the database
        cursor = connection.cursor()
        
        # Execute the SQL query to retrieve states sorted by id
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)
        
        # Fetch all the rows
        rows = cursor.fetchall()
        
        # Display the results
        for row in rows:
            print(row)
        
        # Close the cursor and connection
        cursor.close()
        connection.close()
        
    except MySQLdb.Error as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states(username, password, database)
'''

import MySQLdb

def filter_states(username, password, database):
    conn = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    results = cursor.fetchall()
    for result in results:
        print(result)
    cursor.close()
    conn.close()

if __name__ == '__main__':
    filter_states('root', 'root', 'hbtn_0e_0_usa')