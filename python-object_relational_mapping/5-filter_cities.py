import MySQLdb
import sys

def list_cities_by_state(username, password, database, state_name):
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
        query = "SELECT cities.id, cities.name, states.name \
                 FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s \
                 ORDER BY cities.id ASC"
        
        # Execute the SQL query with the provided state_name parameter
        cursor.execute(query, (state_name,))
        
        # Fetch all the rows
        results = cursor.fetchall()
        
        # Display the results as a comma-separated string
        cities_list = ', '.join([row[0] for row in results])
        print(cities_list)
        
        # Close the cursor and connection
        cursor.close()
        dbase.close()

if __name__ == "__main__":
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        list_cities_by_state(username, password, database, state_name)
