#!/usr/bin/python3
"""
Module - Connects to MySQL database using MySQLdb and retrieves
the first entry from the 'states' table.
"""
import MySQLdb
import sys
if __name__ == '__main__':
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
    except IndexError:
        sys.exit(0)

    DB_CONFIG = {
        "user": f"{username}",
        "db": f"{database}",
        "password": f"{password}",
        "port": 3306,
    }

    try:
        db = MySQLdb.connect(**DB_CONFIG)
        cursor = db.cursor()
        query = "SELECT cities.name \
            FROM states \
                JOIN cities \
                    ON cities.state_id = states.id \
                        WHERE states.name = %s;"
        cursor.execute(query, (state_name, ))

        results = cursor.fetchall()
        for i in range(len(results)):
            if i != len(results) - 1:
                print(results[i][0], end=" ")
            else:
                print(results[i][0], end="")
        print("")

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        try:
            if cursor:
                cursor.close()
            if db:
                db.close()
        except NameError:
            pass
