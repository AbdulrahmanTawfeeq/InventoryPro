from app import App
from db.database_manager import DatabaseManager

if __name__ == '__main__':
    try:
        db_manager = DatabaseManager()
        db_manager.create_tables()
        db_manager.close_connection()
        app = App()
        app.run()
    except Exception as e:
        # Handle exceptions gracefully
        print(f"An error occurred: {e.with_traceback()}")
