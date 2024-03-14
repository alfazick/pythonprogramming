# database.py

class Database:
    def __init__(self,db_path) -> None:
        self.db_path = db_path

    def connect(self):
        print(f"Connecting to database at {self.db_path}")

