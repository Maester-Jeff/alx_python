import MySQLdb
import sys


def list_states(username, password, database):
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
        dbase.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states(username, password, database)
