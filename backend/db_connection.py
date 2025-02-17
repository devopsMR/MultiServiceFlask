import mysql.connector
from mysql.connector import Error
from flask.cli import load_dotenv
import os

load_dotenv()

# Database configuration (from .env file)
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}


# Ensure the database and table exist
def initialize_database():
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )
        cursor = connection.cursor()

        # Create the database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")

        # Connect to the database and create the table
        connection.database = DB_CONFIG["database"]
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS processed_texts (
                id INT AUTO_INCREMENT PRIMARY KEY,
                text VARCHAR(255) UNIQUE NOT NULL,
                reversed_text VARCHAR(255) NOT NULL
            )
        ''')
        connection.commit()
    except Error as e:
        print(f"Error initializing database: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Fetch reversed text from the database if it exists
def get_reversed_text_from_db(text):
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        query = "SELECT reversed_text FROM processed_texts WHERE text = %s"
        cursor.execute(query, (text,))
        result = cursor.fetchone()
        return result[0] if result else None
    except Error as e:
        print(f"Error fetching text from database: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Insert text and reversed text into the database
def insert_text_into_db(text, reversed_text):
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        query = "INSERT INTO processed_texts (text, reversed_text) VALUES (%s, %s)"
        cursor.execute(query, (text, reversed_text))
        connection.commit()
    except Error as e:
        print(f"Error inserting text into database: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Initialize the database
initialize_database()
