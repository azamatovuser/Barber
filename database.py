import sqlite3


class Database:
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.cursor = self.db.cursor()

    def create_table_product(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS product(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(221),
                price INT,
                image VARCHAR(221)                
            )
        """)
        self.db.commit()

    def add_product(self, name, price, image):
        self.cursor.execute("""
            INSERT INTO product(name, price, image)
            VALUES (?, ?, ?)
        """, (name, price, image))
        self.db.commit()

    def get_products(self):
        result = self.cursor.execute("""
            SELECT * FROM product
        """)
        return result.fetchall()

    def close_database(self):
        self.db.close()
