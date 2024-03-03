from tkinter import *
from tkinter import ttk
import pathlib
import logging

from bubble_visit.database import Database
from bubble_visit import configuration, journals
from bubble_visit.components.coordinates import SectorCoordinates


VERSION = "0.1.0"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

database_connection: Database
main_window: Tk

logging.basicConfig(filename=configuration.data_folder_path() / "bubblevisit.log", level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def refresh_systems():
    database_connection.clear_journals()
    database_connection.clear_systems()
    add_systems()


def run():
    global database_connection
    global main_window

    configuration.data_folder_path().mkdir(parents=True, exist_ok=True)
    database_connection = Database(configuration.database_path())

    main_window = Tk()
    main_window.title("Bubble Visit")
    main_window.option_add("*tearOff", FALSE)

    frame = ttk.Frame(main_window, padding=10)
    frame.pack()

    coordinates = SectorCoordinates(frame)
    coordinates.pack()

    system_count_frame = ttk.Frame(frame, padding=10)
    system_count_frame.pack()

    sector_sys_label = ttk.Label(system_count_frame, text="Visited systems in sector: 0")
    sector_sys_label.pack()

    bounds_sys_label = Label(system_count_frame, text="Visited systems in bounds: 0")
    bounds_sys_label.pack()

    button = ttk.Button(frame, text="Mark sector as finished")
    button.pack()

    setup_menu()

    logger.info("Start GUI")

    main_window.after(1, add_systems)
    main_window.mainloop()


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
        if database_connection.has_journal(path.name):
            continue

        new_journals.append(path)

    logger.info(f"Found {len(new_journals)} new journals")

    for i in range(len(new_journals)):
        logger.debug(f"Getting systems from journal: '{new_journals[i].name}'")
        add_systems_from_journal(new_journals[i])

        if i < len(new_journals) - 1:  # don't add most recent journal to database in case it's still being modified
            database_connection.insert_journal(new_journals[i].name)

    logger.info("Finished adding new systems")


def add_systems_from_journal(journal_path):
    for event in journals.read_events(journal_path):
        if event["event"] != "FSDJump":
            continue

        database_connection.insert_system(event["SystemAddress"], event["StarPos"])


def setup_menu():
    menubar = Menu(main_window)
    main_window["menu"] = menubar

    menu_file = Menu(menubar)
    menu_file.add_command(label="Refresh system data", command=refresh_systems)

    menubar.add_cascade(menu=menu_file, label="File")
