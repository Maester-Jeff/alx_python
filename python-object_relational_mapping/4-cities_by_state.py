#!/usr/bin/python3
import sys
import MySQLdb

def list_cities(username, password, dbname):
        # Connect to the MySQL server
        dbase = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=dbname)

        # Create a cursor to interact with the database
        cursor = dbase.cursor()

        # Execute the query to fetch cities along with their state names
        results = "SELECT cities.id, cities.name, states.name \
                FROM cities \
                JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC"
        cursor.execute(results)

        # Fetch all the results
        results = cursor.fetchall()

        # Display the results
        for row in results:
            print(row)

        # Close the cursor and the database connection
        cursor.close()
        dbase.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    list_cities(username, password, dbname)
