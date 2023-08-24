'''Script that lists all states with a name starting with 
N (upper N) from the database hbtn_0e_0_usa.'''

import MySQLdb

import sys

# Function definition for listing the states.
def states_with_N(username, password, database):

        # Connect to the MySQL server
        dbase = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        # Creating a cursor for the database
        cursor = dbase.cursor()
        # Executing the SQL query to retrieve states starting with 'N' and sorted by id
        results = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(results)
        # Fetching all the rows
        rows = cursor.fetchall()
        # Displaying the results
        for row in rows:
            print(row)
        # Closing the cursor and connection
        cursor.close()
        dbase.close()
# Ensure the module do not execute when imported
if __name__ == "__main__":
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        states_with_N(username, password, database)
