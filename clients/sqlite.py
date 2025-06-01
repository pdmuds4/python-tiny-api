import sqlite3

class SqliteClient(sqlite3.Connection):
    def __init__(self, db_path: str, table_name: str):
        super().__init__(db_path)        
        self.table_name = table_name

