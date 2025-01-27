import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your host
            user="root",       # Replace with your username
            password="Ronaldo@254"  # Replace with your password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            cursor.close()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            connection.close()
            print("Connection to MySQL closed.")

if __name__ == "__main__":
    create_database()
