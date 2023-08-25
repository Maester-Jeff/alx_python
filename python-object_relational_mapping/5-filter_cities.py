import sys
import MySQLdb

def list_cities_by_state(username, password, dbname, state_name):

    try:
        # Connect to the MySQL server
        dbase = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=dbname
        )

        # Create a cursor to interact with the database
        cursor = dbase.cursor()

        # Execute the query to fetch cities of the specified state
        results = "SELECT cities.name \
                FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC"
        cursor.execute(results, (state_name,))

        # Fetch all the results
        rows = cursor.fetchall()

        # Display the results as a comma-separated string
        cities_list = ', '.join([row[0] for row in rows])
        print(cities_list)

        # Close the cursor and the database connection
        cursor.close()
        dbase.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: {} <username> <password> <dbname> <state_name>"
            .format(sys.argv[0])
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    list_cities_by_state(username, password, dbname, state_name)
