from db.database_manager import DatabaseManager


class CustomerModel:
    def __init__(self, customer_id=None, name=None, email=None, phone=None):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def save(self):
        db_manager = DatabaseManager()
        db_manager.cursor.execute("""
            INSERT INTO customer (name, email, phone)
            VALUES (?, ?, ?)
        """, (self.name, self.email, self.phone))
        self.customer_id = db_manager.cursor.lastrowid
        db_manager.conn.commit()
        db_manager.close_connection()

    def update(self):
        db_manager = DatabaseManager()
        db_manager.cursor.execute("""
            UPDATE customer
            SET name = ?, email = ?, phone = ?
            WHERE customer_id = ?
        """, (self.name, self.email, self.phone, self.customer_id))
        db_manager.conn.commit()
        db_manager.close_connection()

    def delete(self):
        db_manager = DatabaseManager()
        db_manager.cursor.execute("""
            DELETE FROM customer
            WHERE customer_id = ?
        """, (self.customer_id,))
        db_manager.conn.commit()
        db_manager.close_connection()

    @staticmethod
    def get_all():
        db_manager = DatabaseManager()
        db_manager.cursor.execute("SELECT * FROM customer")
        rows = db_manager.cursor.fetchall()
        db_manager.close_connection()
        return [CustomerModel(*row) for row in rows]

    @staticmethod
    def get_by_id(customer_id):
        db_manager = DatabaseManager()
        db_manager.cursor.execute("SELECT * FROM customer WHERE customer_id = ?", (customer_id,))
        row = db_manager.cursor.fetchone()
        db_manager.close_connection()
        if row:
            return CustomerModel(*row)
        return None
