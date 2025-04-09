import os
import mysql.connector

def main():
    db_config = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': int(os.getenv('DB_PORT', 3306)),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'database': os.getenv('DB_NAME', '')
    }

    try:
        #connect to db using our config
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        #prove the database has tables
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(table[0])
        #show there is data in the table
        cursor.execute("SELECT * FROM Recipes;")
        recipes = cursor.fetchall()
        print("rows in the recipes:")
        for r in recipes:
            print(r)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    main()
