import sqlite3


def init_tables(path):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()

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


def insert_system(address: int, coords: list):
    pass
