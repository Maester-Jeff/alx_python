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
        results = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(results)
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
    if len(sys.argv) != 4:
        print("<mysql_username> <mysql_password> <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states(username, password, database)
