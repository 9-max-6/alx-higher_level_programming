#!/usr/bin/python3
"""
A module using the MySQLdb
"""
import sys
import MySQLdb

if __name__ == '__main__':
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        name = sys.argv[4]
    except NameError:
        sys.exit(1)

    DB_CONFIG = {
            "user": username,
            "password": password,
            "database": database,
            "port": 3306,
        }

    try:
        db = MySQLdb.connect(**DB_CONFIG)
        cursor = db.cursor()
        query1 = "SELECT * FROM states"
        query2 = " WHERE name = %s ORDER BY id ASC;"
        query = query1 + query2
        cursor.execute(query, (name,))
        responses = cursor.fetchall()

        for response in responses:
            print(response)
    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        try:
            if cursor:
                cursor.close()
            if db:
                db.close()
        except NameError:
            pass
