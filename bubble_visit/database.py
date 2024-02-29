import sqlite3


class Database:
    connection = None

    def __init__(self, path):
        self.connection = sqlite3.connect(path)

    def init_tables(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sectors (
                offset_x INTEGER NOT NULL,
                offset_y INTEGER NOT NULL,
                offset_z INTEGER NOT NULL,
                completed INTEGER NOT NULL,
                systems INTEGER NOT NULL,
                
                PRIMARY KEY(offset_x, offset_y, offset_z)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS systems (
                address INTEGER PRIMARY KEY,
                pos_x REAL NOT NULL,
                pos_y REAL NOT NULL,
                pos_z REAL NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS journals (
                name TEXT PRIMARY KEY
            )
        """)

    def insert_system(self, address: int, coords: list):
        cursor = self.connection.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO systems (address, pos_x, pos_y, pos_z) VALUES(?, ?, ?, ?)
        """, (address, coords[0], coords[1], coords[2]))

        self.connection.commit()

    def clear_systems(self):
        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM systems")

        self.connection.commit()

    def insert_journal(self, name: str):
        cursor = self.connection.cursor()

        cursor.execute("""
            INSERT INTO journals (name) VALUES(?)
        """, name)

        self.connection.commit()

    def clear_journals(self):
        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM journals")

        self.connection.commit()

    def has_journal(self, name: str) -> bool:
        cursor = self.connection.cursor()

        result = cursor.execute("""
            SELECT name FROM journals WHERE name = ? 
        """, name)

        name = result.fetchone()

        return name is not None
