from tkinter import *
from tkinter import ttk
import pathlib
import logging
from typing import Optional

from bubble_visit.database import Database
from bubble_visit import configuration, journals, database
from bubble_visit.components.settings import Settings
from bubble_visit.components.main_window import MainWindow


VERSION = "0.1.0"

database_connection: Database
main_window: Tk
settings_window: Optional[Toplevel] = None

logging.basicConfig(filename=configuration.data_folder_path() / "bubblevisit.log", level=logging.INFO, format=configuration.LOG_FORMAT)
logger = logging.getLogger(__name__)


def run():
    global database_connection
    global main_window

    configuration.data_folder_path().mkdir(parents=True, exist_ok=True)
    database.connect(configuration.database_path())

    main_window = MainWindow()

    logger.info("Start GUI")

    main_window.after(1, database.add_systems())
    main_window.mainloop()
