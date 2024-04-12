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
    except IndexError:
        sys.exit(1)

    DB_CONFIG = {
        "user": f"{username}",
        "db": f"{database}",
        "password": f"{password}",
        "port": 3306,
    }

    try:
        db = MySQLdb.connect(**DB_CONFIG)
        cursor = db.cursor()
        
        cursor.execute("SELECT * FROM states ORDER BY id ASC;")
        
        result = cursor.fetchall()
        for item in result:
            print(item)
        
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


