#!/usr/bin/python3
import sys
import MySQLdb

def list_cities(username, password, dbname):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=dbname)

        # Create a cursor to interact with the database
        cursor = db.cursor()

        # Execute the query to fetch cities along with their state names
        query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
        """
        cursor.execute(query)

        # Fetch all the results
        results = cursor.fetchall()

        # Display the results
        for row in results:
            print(row)

        # Close the cursor and the database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <dbname>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    list_cities(username, password, dbname)
