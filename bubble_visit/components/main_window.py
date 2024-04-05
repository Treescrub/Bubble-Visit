import tkinter
from tkinter import ttk
from tkinter import *
import bubble_visit.database as database

from bubble_visit.components.coordinates import SectorCoordinates
from bubble_visit.components.system_counts import SystemCounts
from bubble_visit.components.settings import Settings


class MainWindow(tkinter.Tk):
    settings_window = None

    def __init__(self):
        super().__init__()

        self.title("Bubble Visit")
        self.option_add("*tearOff", FALSE)

        frame = ttk.Frame(self, padding=10)
        frame.pack()

        coordinates = SectorCoordinates(frame)
        coordinates.grid(row=0, column=0)

        system_counts = SystemCounts(frame)
        system_counts.grid(row=0, column=1)

        button = ttk.Button(frame, text="Mark sector as finished")
        button.grid(row=1, column=0)

        self.setup_menu()

    def setup_menu(self):
        menubar = Menu(self)
        self["menu"] = menubar

        menu_file = Menu(menubar)
        menu_file.add_command(label="Refresh system data", command=database.refresh_systems)
        menu_file.add_command(label="Settings", command=self.open_settings)

        menubar.add_cascade(menu=menu_file, label="File")

    def on_settings_close(self):
        if not self.settings_window:
            return

        self.settings_window.destroy()
        self.settings_window = None

    def open_settings(self):
        if self.settings_window:
            self.settings_window.lift()
            return

        self.settings_window = Settings(self)
        self.settings_window.protocol("WM_DELETE_WINDOW", self.on_settings_close)
