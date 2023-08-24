#script that lists all states from the database hbtn_0e_0_usa.
#Importing mysqldb module.
import MySQLdb
import sys
# function definition for listing the states.
def list_states(username, password, database):
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
        
        # Execute the SQL query to retrieve states
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)
        # Fetch all the rows
        rows = cursor.fetchall()
        # Displaying the results
        for row in rows:
            print(row)
        # Closing the cursor and connection
        cursor.close()
        dbase.close()
# Ensure the module do not execute when imported
if __name__ == "__main__":
    list_states('root', 'root', 'hbtn_0e_0_usa')
