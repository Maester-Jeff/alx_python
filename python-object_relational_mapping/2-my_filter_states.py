'''Script that takes in an argument and displays all values in the
 states table of hbtn_0e_0_usa where name matches the argument.'''

import MySQLdb

import sys


# Function definition for listing the states.
def searched_states(username, password, database, state_name_searched):

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
        # Executing the SQL query to retrieve states.
        results = (
                "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC"
                .format(state_name_searched)
        )
        cursor.execute(results)
        # Fetching all the rows
        rows = cursor.fetchall()
        # Displaying the results
        for row in rows:
            print(row)
        # Closing the cursor and connection
        cursor.close()
        dbase.close()
# Ensuring the module do not execute when imported
if __name__ == "__main__":
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name_searched = sys.argv[4]
        searched_states(username, password, database, state_name_searched)
