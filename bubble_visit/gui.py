from tkinter import *
from tkinter import ttk
import pathlib

from bubble_visit.database import Database
from bubble_visit import configuration


VERSION = "0.1.0"

database_connection: Database


def insert_system():
    database_connection.insert_system(123456789, [1.0, 2.0, 3.0])


def run():
    global database_connection

    pathlib.Path(configuration.data_folder_path()).mkdir(parents=True, exist_ok=True)
    database_connection = Database(configuration.database_path())

    window = Tk()
    window.title("Bubble Visit")
    window.option_add("*tearOff", FALSE)

    frame = ttk.Frame(window, padding=10)
    frame.pack()

    system_count_frame = ttk.Frame(frame, padding=10)
    system_count_frame.pack()

    sector_sys_label = ttk.Label(system_count_frame, text="Visited systems in sector: 0")
    sector_sys_label.pack()

    bounds_sys_label = Label(system_count_frame, text="Visited systems in bounds: 0")
    bounds_sys_label.pack()

    button = ttk.Button(frame, text="Mark sector as finished")
    button.pack()

    insert_system_button = ttk.Button(frame, text="Insert system", command=insert_system)
    insert_system_button.pack()

    menubar = Menu(window)
    window["menu"] = menubar

    menu_file = Menu(menubar)
    menu_file.add_command(label="Test")

    menubar.add_cascade(menu=menu_file, label="File")

    window.mainloop()
