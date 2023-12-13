from .connection import Database


def init_database():
    try:
        db = Database()
        session = db.connect()
        Database.Base.metadata.create_all(bind=Database._engine)
        return session
    except ValueError as e:
        print(f"Error: {e}")

