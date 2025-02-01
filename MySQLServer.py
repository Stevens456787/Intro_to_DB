import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None  # Declare connection outside try-except
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ronaldo@254",
            auth_plugin="mysql_native_password"  # Ensure correct authentication
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            connection.commit()  # Apply changes
            print("Database 'alx_book_store' created successfully!")
            cursor.close()
    except mysql.connector.Error as e:  # Specific MySQL error handling
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"General Error: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    create_database()
