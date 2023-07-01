from db.database_manager import DatabaseManager


class ProductModel:
    def __init__(self, product_id=None, name=None, price=None, description=None, customer_id=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.customer_id = customer_id

    def save(self):
        db_manager = DatabaseManager()
        db_manager.cursor.execute("""
            INSERT INTO products (name, price, description, customer_id)
            VALUES (?, ?, ?, ?)
        """, (self.name, self.price, self.description, self.customer_id))
        self.product_id = db_manager.cursor.lastrowid
        db_manager.conn.commit()
        db_manager.close_connection()

    def update(self):
        db_manager = DatabaseManager()
        db_manager.cursor.execute("""
            UPDATE products
            SET name = ?, price = ?, description = ?, customer_id = ?
            WHERE product_id = ?
        """, (self.name, self.price, self.description, self.customer_id, self.product_id))
        db_manager.conn.commit()
        db_manager.close_connection()

    def delete(self):
        db_manager = DatabaseManager()
        db_manager.cursor.execute("""
            DELETE FROM products
            WHERE product_id = ?
        """, (self.product_id,))
        db_manager.conn.commit()
        db_manager.close_connection()

    @staticmethod
    def get_all():
        db_manager = DatabaseManager()
        db_manager.cursor.execute("SELECT * FROM products")
        rows = db_manager.cursor.fetchall()
        db_manager.close_connection()
        return [ProductModel(*row) for row in rows]

    @staticmethod
    def get_by_id(product_id):
        db_manager = DatabaseManager()
        db_manager.cursor.execute("SELECT * FROM products WHERE product_id = ?", (product_id,))
        row = db_manager.cursor.fetchone()
        db_manager.close_connection()
        if row:
            return ProductModel(*row)
        return None
