'''script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
But safe from MySQL injections!'''

import MySQLdb
import sys


def safe_search_states(username, password, database, state_search):
        # Connect to the MySQL server
        dbase = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor to interact with the database
        cursor = dbase.cursor()

        # Prepare the SQL query with parameters
        results = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        # Execute the SQL query with the provided search_name parameter
        cursor.execute(results, (state_search,))

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

        # Close the cursor and connection
        cursor.close()
        dbase.close()

if __name__ == "__main__":
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        safe_search_states(username, password, database, state_name)
