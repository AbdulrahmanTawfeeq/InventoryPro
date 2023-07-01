import sqlite3

from config import get_db_name


class DatabaseManager:
    # Use get_db_name() to retrieve the database name
    DB_NAME = get_db_name()

    def __init__(self):
        self.conn = sqlite3.connect(f'db/{DatabaseManager.DB_NAME}')
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customer (
                customer_id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                phone TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL,
                description TEXT,
                customer_id INTEGER,
                FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
            )
        """)

        self.conn.commit()

    def close_connection(self):
        self.conn.close()
