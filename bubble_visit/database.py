import sqlite3
import pathlib
import logging

from bubble_visit import configuration, journals

logging.basicConfig(filename=configuration.data_folder_path() / "database.log", level=logging.INFO, format=configuration.LOG_FORMAT)
logger = logging.getLogger(__name__)


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
        """, (name,))

        self.connection.commit()

    def clear_journals(self):
        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM journals")

        self.connection.commit()

    def has_journal(self, name: str) -> bool:
        cursor = self.connection.cursor()

        result = cursor.execute("""
            SELECT name FROM journals WHERE name = ?
        """, (name,))

        name = result.fetchone()

        return name is not None


connection: Database = None


def connect(path):
    global connection

    connection = Database(path)


def refresh_systems():
    connection.clear_journals()
    connection.clear_systems()
    add_systems()


def add_systems():
    logger.info("Looking for new systems to add")

    journal_dir = pathlib.Path(journals.get_windows_path()).expanduser()

    if not journal_dir.exists() or not journal_dir.is_dir():
        return

    journal_paths = []
    for path in journal_dir.iterdir():
        if not path.is_file():
            continue

        if journals.is_journal_file(path.name):
            journal_paths.append(path)

    # sort journal paths by oldest to newest
    journal_paths.sort(key=lambda file: file.stat().st_mtime)

    new_journals = []
    for path in journal_paths:
        if connection.has_journal(path.name):
            continue

        new_journals.append(path)

    logger.info(f"Found {len(new_journals)} new journals")

    for i in range(len(new_journals)):
        logger.debug(f"Getting systems from journal: '{new_journals[i].name}'")
        add_systems_from_journal(new_journals[i])

        if i < len(new_journals) - 1:  # don't add most recent journal to database in case it's still being modified
            connection.insert_journal(new_journals[i].name)

    logger.info("Finished adding new systems")


def add_systems_from_journal(journal_path):
    for event in journals.read_events(journal_path):
        if event["event"] != "FSDJump":
            continue

        connection.insert_system(event["SystemAddress"], event["StarPos"])

