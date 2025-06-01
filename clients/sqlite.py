import sqlite3

class SqliteClient(sqlite3.Connection):
    def __init__(self, db_path: str):
        super().__init__(db_path)
