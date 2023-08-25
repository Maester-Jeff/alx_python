import MySQLdb
import sys

def list_cities(username, password, database):

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
        
        # Execute the SQL query to retrieve all cities and sort by id
        query = "SELECT * FROM cities ORDER BY id ASC"
        cursor.execute(query)
        
        # Fetch all the rows
        rows = cursor.fetchall()
        
        # Display the results
        for row in rows:
            print(row)
        
        # Close the cursor and connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_cities(username, password, database)
